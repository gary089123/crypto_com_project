import pytest
import yaml
import logging
from utils.webdriverManager import WebDriverManager

def pytest_addoption(parser):

    parser.addoption(
        '--env',
        action="store"
    )


def read_yaml(path):

    data = None

    with open(path, "r") as f:
        try:
            data = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            logging.error(exc)
    return data


@pytest.fixture(scope="class")
def set_env(request):

    config_file = request.config.getoption("--env")
    request.cls.env = read_yaml(config_file)


@pytest.fixture(scope="class")
def set_selenium_driver(request):

    driver = WebDriverManager().get_driver()
    request.cls.driver = driver
    yield
    driver.close()






    
