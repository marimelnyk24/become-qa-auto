import pytest

from applications.api.github_api import GitHubAPI
from applications.api.wizzard_world_api import WizzardWorldApi
from applications.ui.github_ui import GitHubUI
from config.config import GitHubConfig
from config.config import WizzardWorldConfig
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def github_api_client():
    github_api_client = GitHubAPI(GitHubConfig.base_url_api)

    yield github_api_client

    print("END-UP TEST")


@pytest.fixture()
def github_ui_client():
    driver = webdriver.Chrome(
        service=Service(
            r"/home/maryna/become-qa-auto/chromedriver")
    )

    github_ui_client = GitHubUI(GitHubConfig.base_url_ui, driver)

    yield github_ui_client

    github_ui_client.close_browser()
