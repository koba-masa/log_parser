from typing import Any
from models.aws import S3Client

import csv
import gzip
import io
import os
import datetime


# https://docs.aws.amazon.com/ja_jp/elasticloadbalancing/latest/application/load-balancer-access-logs.html
class ApplicationLoadBalancer:
    HEADER = [
        "filename",
        "type",
        "time",
        "elb",
        "client:port",
        "target:port",
        "request_processing_time",
        "target_processing_time",
        "response_processing_time",
        "elb_status_code",
        "target_status_code",
        "received_bytes",
        "sent_bytes",
        "request",
        "user_agent",
        "ssl_cipher",
        "ssl_protocol",
        "target_group_arn",
        "trace_id",
        "domain_name",
        "chosen_cert_arn",
        "matched_rule_priority",
        "request_creation_time",
        "actions_executed",
        "redirect_url",
        "error_reason",
        "target:port_list",
        "target_status_code_list",
        "classification",
        "classification_reason",
    ]
    INDEX_OF_REQUEST_CREATION_TIME = 22

    def __init__(self, base_output_dir: str, config: dict[str, Any]) -> None:
        self.base_output_dir = base_output_dir
        self.config = config
        self.s3_client = S3Client()

    def execute(self) -> None:
        self.validate_config()
        self.__create_output_dir(self.base_output_dir)

        self.bucket_location = self.s3_client.get_bucket_location(self.config["bucket"])

        start_datetime, end_datetime = self.create_range(self.config["target_datetime"])

        keys = self.__get_keys(self.config["prefix"], start_datetime, end_datetime)

        if len(keys) == 0:
            return

        data = []
        for key in keys:
            encoded_data = self.s3_client.download(self.config["bucket"], key)
            decoded_data = gzip.decompress(encoded_data).decode()
            data.extend(self.__process_data(key, decoded_data))

        data = sorted(data, key=lambda x: x[self.INDEX_OF_REQUEST_CREATION_TIME])

        self.__output_result(data)

    def validate_config(self) -> None:
        pass

    def create_range(
        self, target_datetime: str
    ) -> tuple[datetime.datetime, datetime.datetime]:
        target = datetime.datetime.strptime(target_datetime, "%Y/%m/%d %H:%M")
        start_datetime = target + datetime.timedelta(minutes=-5)
        end_datetime = target + datetime.timedelta(minutes=5)

        return start_datetime, end_datetime

    def __create_output_dir(self, output_dir: str) -> None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def __get_keys(
        self,
        prefix: str,
        start_datetime: datetime.datetime,
        end_datetime: datetime.datetime,
    ) -> list[str]:
        processed_keys = []
        base_prefix = self.config["prefix"]

        prefixes = list(
            set(
                [
                    self.__create_prefix(base_prefix, start_datetime),
                    self.__create_prefix(base_prefix, end_datetime),
                ]
            )
        )

        keys = []
        for prefix in prefixes:
            tmp = self.s3_client.list_object_v2(self.config["bucket"], prefix)
            if len(tmp) == 0:
                print(f"No objects found.: {prefix}")
                continue

            keys.extend(tmp)

        for key in keys:
            # prefix/AWSLogs/aws-account-id/elasticloadbalancing/region/yyyy/mm/dd/aws-account-id_elasticloadbalancing_region_app.load-balancer-id_end-time_ip-address_random-string.log.gz
            target = key.split("/")[-1]
            # aws-account-id_elasticloadbalancing_region_app.load-balancer-id_end-time_ip-address_random-string.log.gz
            target = target.split("_")[4]
            # end-time
            end_time = datetime.datetime.strptime(target, "%Y%m%dT%H%MZ")
            if start_datetime <= end_time <= end_datetime:
                processed_keys.append(key)

        return processed_keys

    def __create_prefix(self, base_prefix: str, datetime: datetime.datetime) -> str:
        return "{}/AWSLogs/{}/elasticloadbalancing/{}/{}/{}/{}/".format(
            base_prefix,
            self.config["account_id"],
            self.config["region"],
            datetime.year,
            datetime.month,
            datetime.day,
        )

    def __process_data(self, key: str, data: str) -> list[list[str]]:
        rows = []

        csv_data = csv.reader(io.StringIO(data), delimiter=" ", quotechar='"')
        for row in csv_data:
            processed_row = self.__add_object_url_to_row(key, row)
            rows.append(processed_row)

        return rows

    def __add_object_url_to_row(self, key: str, row: list[str]) -> list[str]:
        object_url = f"https://s3.{self.bucket_location}.amazonaws.com/{self.config['bucket']}/{key}"
        processed_row = [object_url]
        processed_row.extend(row)

        return processed_row

    def __output_result(self, rows: list[list[str]]) -> None:
        filename = f"{self.base_output_dir}/{self.config['name']}.tsv"
        with open(filename, "w") as f:
            f.write(f"{'\t'.join(self.HEADER)}\n")
            for row in rows:
                f.write(f"{'\t'.join(row)}\n")
