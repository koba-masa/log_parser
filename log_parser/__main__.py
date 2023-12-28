import sys
from models import settings


class LogParser:
    def __init__(self, config_path: str) -> None:
        settings.load_config(config_path)

    def parse(self) -> None:
        print(settings.SETTINGS)


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: python -m log_parser <config_path>")
        sys.exit(1)

    config_path = sys.argv[1]
    parser = LogParser(config_path)
    parser.parse()
