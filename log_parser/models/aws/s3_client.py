import boto3
from models import settings
from typing import List


class S3Client:
    def __init__(self) -> None:
        self.client = boto3.client(
            "s3",
            aws_access_key_id=settings.SETTINGS["aws_access_key"],
            aws_secret_access_key=settings.SETTINGS["aws_secret_access_key"],
            endpoint_url=self.__endpoint_url(),
        )

    def list_object_v2(
        self, bucket: str, prefix: str, max_per_page: int = 1000
    ) -> List[str]:
        results = []

        response = self.client.list_objects_v2(
            Bucket=bucket,
            Prefix=prefix,
            MaxKeys=max_per_page,
        )

        if "Contents" in response:
            results.extend([content["Key"] for content in response["Contents"]])

        while response["IsTruncated"]:
            continuation_token = response["NextContinuationToken"]

            response = self.client.list_objects_v2(
                Bucket=bucket,
                Prefix=prefix,
                MaxKeys=max_per_page,
                ContinuationToken=continuation_token,
            )

            if "Contents" in response:
                results.extend([content["Key"] for content in response["Contents"]])

        return results

    def __endpoint_url(self) -> str:
        endpoint_url = settings.SETTINGS.get("aws_endpoint_url", None)
        endpoint_url = None if endpoint_url == "" else endpoint_url
        return endpoint_url
