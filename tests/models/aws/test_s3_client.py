import pytest
from typing import List
from models.aws import S3Client


def test_init() -> None:
    instance = S3Client()

    assert type(instance.client) is not None


@pytest.mark.parametrize(
    [
        "prefix",
        "max_per_page",
        "expected_results",
    ],
    [
        pytest.param(
            "sample/",
            1,
            [
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2145Z_1.2.3.4_KddaYsf3.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2200Z_1.2.3.4_DFXV1dHFH.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2200Z_1.2.3.5_lofR4gdsgfs.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/29/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231229T2340Z_1.2.3.4_ddGdfda12.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/29/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231229T2345Z_1.2.3.4_hfg343GVBS.log.gz",
            ],
        ),
        pytest.param(
            "sample/",
            3,
            [
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2145Z_1.2.3.4_KddaYsf3.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2200Z_1.2.3.4_DFXV1dHFH.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2200Z_1.2.3.5_lofR4gdsgfs.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/29/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231229T2340Z_1.2.3.4_ddGdfda12.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/29/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231229T2345Z_1.2.3.4_hfg343GVBS.log.gz",
            ],
        ),
        pytest.param(
            "sample/",
            1000,
            [
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2145Z_1.2.3.4_KddaYsf3.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2200Z_1.2.3.4_DFXV1dHFH.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2200Z_1.2.3.5_lofR4gdsgfs.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/29/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231229T2340Z_1.2.3.4_ddGdfda12.log.gz",
                "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/29/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231229T2345Z_1.2.3.4_hfg343GVBS.log.gz",
            ],
        ),
        pytest.param(
            "example/",
            1,
            [],
        ),
    ],
)
def test_list_object_v2(
    prefix: str, max_per_page: int, expected_results: List[str]
) -> None:
    instance = S3Client()
    results = instance.list_object_v2("log-parser-test", prefix, max_per_page)

    assert results == expected_results


def test_download() -> None:
    instance = S3Client()
    result = instance.download(
        "log-parser-test",
        "sample/AWSLogs/123456789012/elasticloadbalancing/ap-northeast-1/2023/12/28/123456789012_elasticloadbalancing_ap-northeast-1_app.sample_20231228T2200Z_1.2.3.4_DFXV1dHFH.log.gz",
    )

    assert result is not None


def test_download_without_existing_object() -> None:
    instance = S3Client()
    result = instance.download("log-parser-test", "without_existing_object.py")

    assert result is None


def test_get_bucket_location(mocker) -> None:  # type: ignore
    instance = S3Client()
    instance.client = mocker.Mock()
    instance.client.get_bucket_location.return_value = {
        "LocationConstraint": "ap-northeast-1"
    }

    result = instance.get_bucket_location("log-parser-test")

    assert result == "ap-northeast-1"
