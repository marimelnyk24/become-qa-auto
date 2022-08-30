import os


class GitHubConfig:
    base_url_api = os.environ.get("BASER_URL_API", "https://api.github.com")
    base_url_ui = os.environ.get("BASER_URL_UI", "https://github.com")


class WizzardWorldConfig:
    base_url_api = "https://wizard-world-api.herokuapp.com"
