from models import settings
from services.aws import ApplicationLoadBalancer

import os
import pytest
import datetime


def read_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def test_init() -> None:
    base_output_dir = "tmp/tests/results/202312300121"
    config = settings.SETTINGS["aws_application_load_balancer"][0]
    instance = ApplicationLoadBalancer(base_output_dir, config)

    assert instance.base_output_dir == base_output_dir
    assert instance.config["name"] == "sample"


def test_execute(delete_dir) -> None:
    base_output_dir = "tmp/tests/202312300121"
    config = settings.SETTINGS["aws_application_load_balancer"][0]

    filename = f"{base_output_dir}/{config['name']}.tsv"

    ApplicationLoadBalancer(base_output_dir, config).execute()

    assert os.path.exists(filename)
    assert read_file(filename) == read_file(
        "tests/files/services/aws/application_load_blancer/normal.tsv"
    )


@pytest.mark.parametrize(
    [
        "target_datetime",
        "expected_start_datetime",
        "expected_end_datetime",
    ],
    [
        pytest.param(
            "2023/12/28 21:58",
            datetime.datetime(2023, 12, 28, 21, 53, 0),
            datetime.datetime(2023, 12, 28, 22, 3, 0),
        ),
        pytest.param(
            "2023/12/31 23:58",
            datetime.datetime(2023, 12, 31, 23, 53, 0),
            datetime.datetime(2024, 1, 1, 0, 3, 0),
        ),
    ],
)
def test_create_range(
    target_datetime: str,
    expected_start_datetime: datetime.datetime,
    expected_end_datetime: datetime.datetime,
) -> None:
    base_output_dir = "tmp/tests/202312300121"
    config = settings.SETTINGS["aws_application_load_balancer"][0]

    instance = ApplicationLoadBalancer(base_output_dir, config)

    actual_start_datetime, actual_end_datetime = instance.create_range(target_datetime)

    assert actual_start_datetime == expected_start_datetime
    assert actual_end_datetime == expected_end_datetime
