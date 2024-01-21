from collections import Counter
from typing import Dict


class Metric:
    # {
    #     "NAMESPACE": {
    #         "METRICNAME" : {
    #             "Dimensions": ["", ""]
    #         }
    #     },
    # }
    METRICS: Dict[str, Dict[str, Dict[str, list[str]]]] = {
        "AWS/EC2": {
            "CPUUtilization": {
                "Dimensions": ["InstanceId"],
            }
        },
        "AWS/ApplicationELB": {
            "RequestCount": {
                "Dimensions": ["Resource"],
            }
        },
        "AWS/Lambda": {
            "Errors": {
                "Dimensions": ["FunctionName", "Resource"],
            }
        },
    }

    STATS: list[str] = []

    @classmethod
    def check_namespace(cls, namespace: str) -> bool:
        return namespace in cls.METRICS

    @classmethod
    def check_metric_name(cls, namespace: str, metric_name: str) -> bool:
        return metric_name in cls.METRICS[namespace]

    @classmethod
    def check_dimensions(
        cls, namespace: str, metric_name: str, dimensions: list[str]
    ) -> bool:
        return Counter(cls.METRICS[namespace][metric_name]["Dimensions"]) == Counter(
            dimensions
        )
