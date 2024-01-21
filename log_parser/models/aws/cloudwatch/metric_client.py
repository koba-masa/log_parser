import datetime
from typing import Any, List, Dict

from models.aws import CloudWatchClient


class MetricClient(CloudWatchClient):
    def __init__(self, region: str) -> None:
        super().__init__(region)

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
