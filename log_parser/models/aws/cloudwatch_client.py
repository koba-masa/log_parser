import boto3
from models import settings


class CloudWatchClient:
    def __init__(self, region: str) -> None:
        self.client = boto3.client(
            "cloudwatch",
            aws_access_key_id=settings.SETTINGS["aws_access_key"],
            aws_secret_access_key=settings.SETTINGS["aws_secret_access_key"],
            region_name=region,
        )
