import json
import os
import pytest

from log_parser.tools.metrics_dict_creation import MetricsDictCreation


def read_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


@pytest.fixture(scope="function")
def described_instance(mocker):
    def _described_instance(output_dir):
        metric_data = (
            "tests/files/services/aws/cloudwatch/metrics/list_metrics_response.json"
        )
        loaded_metric_data = None
        with open(metric_data) as f:
            loaded_metric_data = json.load(f)

        instance = MetricsDictCreation("config/test.yaml", output_dir)
        instance.cloudwatch_client = mocker.Mock()
        instance.cloudwatch_client.list_metrics.return_value = loaded_metric_data

        return instance

    return _described_instance


def test_execute(delete_dir, described_instance):
    expected_result = (
        "tests/files/services/aws/cloudwatch/metrics/list_metrics_response.txt"
    )
    output_dir = "tmp/tests/results"

    described_instance(output_dir).execute()
    filename = f"{output_dir}/{MetricsDictCreation.OUTPUT_FILENAME}"

    assert os.path.exists(filename)
    assert read_file(filename) == read_file(expected_result)
