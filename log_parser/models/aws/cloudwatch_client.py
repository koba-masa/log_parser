from models.aws import BaseClient


class CloudWatchClient(BaseClient):
    def __init__(self, region: str) -> None:
        options = {"region_name": region}
        super().__init__("cloudwatch", options)
