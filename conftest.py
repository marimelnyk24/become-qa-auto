import pytest

from applications.api.github_api import GitHubAPI
from applications.api.final_space_api import FinalSpaceApi
from applications.ui.github_ui import GitHubUI
from config.config import FinalSpaceConfig, GitHubConfig
from config.config import FinalSpaceConfig
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


@pytest.fixture(scope="session")
def final_space_api_client():
    final_space_api_client = FinalSpaceApi(FinalSpaceConfig.BASE_URL)

    yield final_space_api_client

    print("END-UP TEST")
