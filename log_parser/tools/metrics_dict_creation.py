import os
import sys
from typing import Dict

from models.aws.cloudwatch import Metric
from models.aws.cloudwatch import MetricClient
from models import settings


class MetricsDictCreation:
    OUTPUT_FILENAME: str = "metrics_dict.json"

    def __init__(self, config_path: str, output_dir: str) -> None:
        settings.load_config(config_path)
        self.config = settings.SETTINGS["tools"]["metrics_dict_creation"]
        self.output_dir = output_dir
        self.metrics = Metric.METRICS
        self.cloudwatch_client = MetricClient(self.config["region"])

    def execute(self) -> None:
        for namespace in self.config["namespaces"]:
            metrics = self.cloudwatch_client.list_metrics(namespace)
            for metric in metrics:
                namespace = metric["Namespace"]
                metric_name = metric["MetricName"]
                dimensions = metric["Dimensions"]
                self.__append_metrics_dict(namespace, metric_name, dimensions)

        self.__output_result()

    def __append_metrics_dict(
        self, namespace: str, metric_name: str, dimensions: list[Dict[str, str]]
    ) -> None:
        dimension_keys = [dimension["Name"] for dimension in dimensions]
        if namespace not in self.metrics:
            self.metrics[namespace] = {
                metric_name: {
                    "Dimensions": dimension_keys,
                }
            }
            return

        metrics = self.metrics[namespace]
        if metric_name not in metrics:
            metrics[metric_name] = {
                "Dimensions": dimension_keys,
            }
            return

        return

    def __output_result(self) -> None:
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        with open(f"{self.output_dir}/{self.OUTPUT_FILENAME}", "w") as f:
            f.write(str(self.metrics))


if __name__ == "__main__":
    if not len(sys.argv) == 1:
        print("Usage: python log_parser/tools/metrics_dict_creation.py <config_path>")
        sys.exit(1)

    config_path = sys.argv[1]
    MetricsDictCreation(config_path, "tmp/results").execute()
