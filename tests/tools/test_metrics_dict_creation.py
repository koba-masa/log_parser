import json
import os
import pytest

from log_parser.tools.metrics_dict_creation import MetricsDictCreation


DUMMY_METRIC_DICT = {
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


def read_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


@pytest.fixture(scope="function")
def described_instance(mocker):
    def _described_instance(output_dir, mock_metric_data):
        loaded_metric_data = None
        with open(mock_metric_data) as f:
            loaded_metric_data = json.load(f)

        instance = MetricsDictCreation("config/test.yaml", output_dir)

        instance.metrics = DUMMY_METRIC_DICT

        instance.cloudwatch_client = mocker.Mock()
        instance.cloudwatch_client.list_metrics.return_value = loaded_metric_data

        return instance

    return _described_instance


@pytest.mark.parametrize(
    ["mock_metric_data", "expected_result"],
    [
        pytest.param(
            "tests/files/services/aws/cloudwatch/metrics/list_metrics_response.json",
            "tests/files/services/aws/cloudwatch/metrics/list_metrics_response.txt",
        ),
        pytest.param(
            "tests/files/services/aws/cloudwatch/metrics/list_metrics_response_override.json",
            "tests/files/services/aws/cloudwatch/metrics/list_metrics_response_override.txt",
        ),
    ],
)
def test_execute(delete_dir, described_instance, mock_metric_data, expected_result):
    output_dir = "tmp/tests/results"

    described_instance(output_dir, mock_metric_data).execute()
    filename = f"{output_dir}/{MetricsDictCreation.OUTPUT_FILENAME}"

    assert os.path.exists(filename)
    assert read_file(filename) == read_file(expected_result)
