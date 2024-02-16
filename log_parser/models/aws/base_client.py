import boto3
from models import settings
from typing import Dict


class BaseClient:
    def __init__(self, service_name: str, options: Dict[str, str]) -> None:
        options["service_name"] = service_name
        options["aws_access_key_id"] = settings.SETTINGS["aws_access_key"]
        options["aws_secret_access_key"] = settings.SETTINGS["aws_secret_access_key"]

        self.client = boto3.client(**options)
