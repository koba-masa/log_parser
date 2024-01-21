import pytest
from models.aws.cloudwatch import Metric


@pytest.mark.parametrize(
    ["namespace", "expected_result"],
    [
        pytest.param("AWS/Lambda", True),
        pytest.param("AWS/NotExisting", False),
    ],
)
def test_check_namespace(namespace, expected_result):
    assert Metric.check_namespace(namespace) is expected_result


@pytest.mark.parametrize(
    ["metric_name", "expected_result"],
    [
        pytest.param("Errors", True),
        pytest.param("NotExisting", False),
    ],
)
def test_check_metric_name(metric_name, expected_result):
    assert Metric.check_metric_name("AWS/Lambda", metric_name) is expected_result


@pytest.mark.parametrize(
    ["dimensions", "expected_result"],
    [
        pytest.param(["FunctionName", "Resource"], True),
        pytest.param(["TooTiny"], False),
        pytest.param(["FunctionName", "Resource", "TooMany"], False),
        pytest.param(["FunctionName", "Resource", "Resource"], False),
    ],
)
def test_check_dimensions(dimensions, expected_result):
    assert (
        Metric.check_dimensions("AWS/Lambda", "Errors", dimensions) is expected_result
    )
