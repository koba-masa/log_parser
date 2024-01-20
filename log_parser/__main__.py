import datetime
import sys
from models import settings
from services.aws import ApplicationLoadBalancer as ALB
from services.aws import CloudWatchMetric as CWM


class LogParser:
    TARGET_KEYS = {
        "aws_alb": "aws_application_load_balancer",
        "aws_metric": "aws_cloudwatch_metric",
    }

    def __init__(self, config_path: str) -> None:
        settings.load_config(config_path)
        self.base_output_dir = self.output_dir()

    def execute(self) -> None:
        if self.TARGET_KEYS["aws_alb"] in settings.SETTINGS:
            for config in settings.SETTINGS.get(self.TARGET_KEYS["aws_alb"], []):
                ALB(self.base_output_dir, config).execute()

        if self.TARGET_KEYS["aws_metric"] in settings.SETTINGS:
            for config in settings.SETTINGS.get(self.TARGET_KEYS["aws_metric"], []):
                CWM(self.base_output_dir, config).execute()

    def output_dir(self) -> str:
        return f"tmp/results/{datetime.datetime.now().strftime('%Y%m%d_%H%M_%S')}"


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python -m log_parser <config_path>")
        sys.exit(1)

    config_path = sys.argv[1]
    parser = LogParser(config_path)
    parser.execute()
