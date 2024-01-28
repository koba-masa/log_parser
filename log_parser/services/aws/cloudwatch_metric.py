from services.aws import AWSBase

from datetime import datetime
from typing import Any, Dict, List
from models.aws.cloudwatch import MetricClient
from models.aws.cloudwatch import Metric

import pytz


class CloudWatchMetric(AWSBase):
    TIMESTAMP_FORMAT = {"config": "%Y/%m/%d %H:%M:%S", "result": "%Y-%m-%d %H:%M:%S%z"}

    def __init__(self, base_output_dir: str, config: Dict[str, Any]) -> None:
        self.base_output_dir = base_output_dir
        self.config = config
        self.cloudwatch_client = MetricClient(self.config["region"])

    def execute(self) -> None:
        tz = pytz.timezone(self.config["timezone"])
        start_time = datetime.strptime(
            self.config["start_time"], self.TIMESTAMP_FORMAT["config"]
        ).astimezone(tz)
        end_time = datetime.strptime(
            self.config["end_time"], self.TIMESTAMP_FORMAT["config"]
        ).astimezone(tz)

        response = self.cloudwatch_client.get_metric_data(
            self.metric_data_queries(),
            start_time,
            end_time,
        )

        shaped_results = self.__create_base_result(response["MetricDataResults"], tz)
        shaped_results = self.__shape(shaped_results, response["MetricDataResults"], tz)

        sorted_result_keys = sorted(shaped_results.keys())
        deleted_timestamp_results = [shaped_results[key] for key in sorted_result_keys]

        self.output_result(
            self.base_output_dir,
            f"{self.config['filename']}.tsv",
            deleted_timestamp_results,
        )

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_metric_data.html
    def metric_data_queries(self) -> List[Dict[str, Any]]:
        queries = []

        for metric in self.config["metrics"]:
            if not self.__check_metric_validation(metric):
                # TODO: 例外を投げる
                continue

            dimensions = [
                {"Name": dimension["name"], "Value": dimension["value"]}
                for dimension in metric["dimensions"]
            ]

            queries.append(
                {
                    "Id": metric["id"],
                    "AccountId": f"{self.config['account_id']}",
                    "MetricStat": {
                        "Metric": {
                            "Namespace": metric["namespace"],
                            "MetricName": metric["name"],
                            "Dimensions": dimensions,
                        },
                        "Period": self.config["period"],
                        "Stat": metric["stat"],
                        # "Unit": "Seconds"|"Microseconds"|"Milliseconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None"
                    },
                    # "Expression": "string",
                    # "Label": "string",
                    # "ReturnData": True|False,
                    # "Period": 123,
                }
            )
        return queries

    def __check_metric_validation(self, config_metric: Dict[str, Any]) -> bool:
        id = config_metric["id"]

        namespace = config_metric["namespace"]
        if not Metric.check_namespace(namespace):
            print(f"[ERROR] Invalid namespace: {id}")
            return False

        metric_name = config_metric["name"]
        if not Metric.check_metric_name(namespace, metric_name):
            print(f"[ERROR] Invalid metric name: {id}")
            return False

        dimensions = [dimension["name"] for dimension in config_metric["dimensions"]]
        if not Metric.check_dimensions(namespace, metric_name, dimensions):
            print(f"[ERROR] Invalid dimensions: {id}")
            return False

        return True

    def __create_base_result(
        self, results: List[Dict[str, Any]], timezone: Any
    ) -> Dict[str, List[str]]:
        data = {}
        dummy_data = ["0.0"] * len(results)
        for result in results:
            for timestamp in result["Timestamps"]:
                converted = datetime.strptime(
                    f"{timestamp}",
                    self.TIMESTAMP_FORMAT["result"],
                ).astimezone(timezone)

                row_key = converted.strftime("%Y%m%d%H%M%S")
                data[row_key] = [
                    converted.strftime("%Y/%m/%d"),
                    converted.strftime("%H:%M:%S"),
                ] + dummy_data

        return data

    def __shape(
        self,
        shaped_results: Dict[str, list[str]],
        metric_data_results: List[Dict[str, Any]],
        timezone: Any,
    ) -> Dict[str, List[str]]:
        for i, result in enumerate(metric_data_results):
            values = result["Values"]

            for j, timestamp in enumerate(result["Timestamps"]):
                row_key = (
                    datetime.strptime(f"{timestamp}", self.TIMESTAMP_FORMAT["result"])
                    .astimezone(timezone)
                    .strftime("%Y%m%d%H%M%S")
                )

                shaped_results[row_key][2 + i] = f"{values[j]}"

        return shaped_results
