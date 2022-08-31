import os


class GitHubConfig:
    base_url_api = os.environ.get("BASER_URL_API", "https://api.github.com")
    base_url_ui = os.environ.get("BASER_URL_UI", "https://github.com")


class FinalSpaceConfig:
    BASE_URL = "https://finalspaceapi.com/api/v0"

    CHARACTERS_ENDPOINT = "/character"
    LOCATIONS_ENDPOINT = "/location"
