import boto3
import unicodedata
import uuid
from models import settings
from typing import Any, Dict, List


class BaseClient:
    def __init__(self, service_name: str, options: Dict[str, str]) -> None:
        options["service_name"] = service_name
        options["aws_access_key_id"] = self.__access_key_id()
        options["aws_secret_access_key"] = self.__secret_access_key()

        self.client = boto3.client(**options)
        if self.__role_arn():
            self.client = self.switch_role(options)

    def switch_role(self, options: Dict[str, str]) -> List[Any]:
        sts_client = boto3.client(
            "sts",
            aws_access_key_id=self.__access_key_id(),
            aws_secret_access_key=self.__secret_access_key(),
        )

        response = sts_client.assume_role(
            RoleArn=self.__role_arn(),
            RoleSessionName=str(uuid.uuid1()),
            DurationSeconds=3600,
            SerialNumber=self.__mfa_device_arn(),
            TokenCode=self.__input_mfa_token(),
        )

        session = boto3.Session(
            aws_access_key_id=response["Credentials"]["AccessKeyId"],
            aws_secret_access_key=response["Credentials"]["SecretAccessKey"],
            aws_session_token=response["Credentials"]["SessionToken"],
        )

        del options["aws_access_key_id"]
        del options["aws_secret_access_key"]

        return session.client(**options)

    def __access_key_id(self) -> str:
        return settings.SETTINGS["aws_access_key"]

    def __secret_access_key(self) -> str:
        return settings.SETTINGS["aws_secret_access_key"]

    def __role_arn(self) -> str:
        return settings.SETTINGS.get("aws_role_arn")

    def __mfa_device_arn(self) -> str:
        return settings.SETTINGS["aws_mfa_arn"]

    def __input_mfa_token(self) -> str:
        input_value = input(f"Enter MFA code for {self.__mfa_device_arn()}: ").strip()
        return unicodedata.normalize("NFKC", input_value)
