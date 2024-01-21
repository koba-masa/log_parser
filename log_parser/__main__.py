import datetime
import sys
from models import settings
from services.aws import ApplicationLoadBalancer
from services.aws import CloudWatchMetric


class LogParser:
    SERVICES = {
        "aws_application_load_balancer": ApplicationLoadBalancer,
        "aws_cloudwatch_metric": CloudWatchMetric,
    }

    def __init__(self, config_path: str) -> None:
        settings.load_config(config_path)
        self.base_output_dir = self.output_dir()

    def execute(self) -> None:
        for key, klass in self.SERVICES.items():
            if key not in settings.SETTINGS:
                continue

            for config in settings.SETTINGS[key]:
                klass(f"{self.base_output_dir}/{key}", config).execute()

    def output_dir(self) -> str:
        return f"tmp/results/{datetime.datetime.now().strftime('%Y%m%d_%H%M_%S')}"


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python -m log_parser <config_path>")
        sys.exit(1)

    config_path = sys.argv[1]
    parser = LogParser(config_path)
    parser.execute()
