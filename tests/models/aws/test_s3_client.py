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
