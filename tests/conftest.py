import pytest
import shutil
from models import settings


settings.load_config("config/test.yaml")


@pytest.fixture(scope="function")
def delete_dir() -> None:
    yield

    shutil.rmtree("tmp/tests")
