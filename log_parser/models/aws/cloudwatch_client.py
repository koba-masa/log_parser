import boto3
import datetime
from models import settings
from typing import Any, List, Dict


class CloudWatchClient:
    def __init__(self, region: str) -> None:
        self.client = boto3.client(
            "cloudwatch",
            aws_access_key_id=settings.SETTINGS["aws_access_key"],
            aws_secret_access_key=settings.SETTINGS["aws_secret_access_key"],
            region_name=region,
        )

    def get_metric_data(
        self,
        metric_data_queries: List[Dict[str, Any]],
        start_time: datetime.datetime,
        end_time: datetime.datetime,
    ) -> Dict[str, Any]:
        return self.client.get_metric_data(
            MetricDataQueries=metric_data_queries,
            StartTime=start_time,
            EndTime=end_time,
        )
