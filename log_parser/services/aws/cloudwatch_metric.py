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

        for config_metric in self.config["metrics"]:
            if not self.__check_metric_validation(config_metric):
                continue

            response = self.cloudwatch_client.get_metric_data(
                self.metric_data_queries(config_metric),
                start_time,
                end_time,
            )

            shaped_results = self.__shape(response["MetricDataResults"][0], tz)
            sorted_results = sorted(shaped_results, key=lambda x: x[0])
            deleted_timestamp_results = [result[1:] for result in sorted_results]

            self.output_result(
                self.base_output_dir,
                f"{config_metric['id']}.tsv",
                deleted_timestamp_results,
            )

    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch/client/get_metric_data.html
    def metric_data_queries(
        self, config_metric: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        dimensions = [
            {"Name": dimension["name"], "Value": dimension["value"]}
            for dimension in config_metric["dimensions"]
        ]
        return [
            {
                "Id": config_metric["id"],
                "AccountId": f"{self.config['account_id']}",
                "MetricStat": {
                    "Metric": {
                        "Namespace": config_metric["namespace"],
                        "MetricName": config_metric["name"],
                        "Dimensions": dimensions,
                    },
                    "Period": self.config['period'],
                    "Stat": config_metric["stat"],
                    # "Unit": "Seconds"|"Microseconds"|"Milliseconds"|"Bytes"|"Kilobytes"|"Megabytes"|"Gigabytes"|"Terabytes"|"Bits"|"Kilobits"|"Megabits"|"Gigabits"|"Terabits"|"Percent"|"Count"|"Bytes/Second"|"Kilobytes/Second"|"Megabytes/Second"|"Gigabytes/Second"|"Terabytes/Second"|"Bits/Second"|"Kilobits/Second"|"Megabits/Second"|"Gigabits/Second"|"Terabits/Second"|"Count/Second"|"None"
                },
                # "Expression": "string",
                # "Label": "string",
                # "ReturnData": True|False,
                # "Period": 123,
            }
        ]

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

    def __shape(
        self, metric_data_result: Dict[str, Any], timezone: Any
    ) -> list[list[str]]:
        timestamps = metric_data_result["Timestamps"]
        values = metric_data_result["Values"]

        shaped_results = []

        for i in range(len(timestamps)):
            timestamp = datetime.strptime(
                f"{timestamps[i]}", self.TIMESTAMP_FORMAT["result"]
            ).astimezone(timezone)

            shaped_results.append(
                [
                    timestamp.strftime("%Y%m%d%H%M%S"),
                    timestamp.strftime("%Y/%m/%d"),
                    timestamp.strftime("%H:%M:%S"),
                    f"{values[i]}",
                ]
            )

        return shaped_results
