from models import settings
from services.aws import CloudWatchMetric

import json
import pytest
import os

BASE_OUTPUT_DIR = "tmp/tests/results/202312300121"


def read_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


@pytest.fixture(scope="function")
def described_instance(mocker):
    def _described_instance(metric_data):
        config = settings.SETTINGS["aws_cloudwatch_metric"][0]

        loaded_metric_data = None
        with open(metric_data) as f:
            loaded_metric_data = json.load(f)

        instance = CloudWatchMetric(BASE_OUTPUT_DIR, config)
        instance.cloudwatch_client = mocker.Mock()
        instance.cloudwatch_client.get_metric_data.return_value = loaded_metric_data

        return instance

    return _described_instance


@pytest.mark.parametrize(
    ["metric_data", "expected_result"],
    [
        pytest.param(
            "tests/files/services/aws/cloudwatch/metrics/applicationelb_requestcount_sum.json",
            "tests/files/services/aws/cloudwatch/metrics/applicationelb_requestcount_sum.tsv",
        ),
    ],
)
def test_execute(delete_dir, described_instance, metric_data, expected_result):
    described_instance(metric_data).execute()

    filename = f"{BASE_OUTPUT_DIR}/sample.tsv"

    assert os.path.exists(filename)
    assert read_file(filename) == read_file(expected_result)
