import pytest
import requests
from config.config import FinalSpaceConfig
from providers.data.characters_provider import CharactersProvider


def test_character_exists(final_space_api_client):
    character = CharactersProvider.existing_character()
    api_character = final_space_api_client.get_by_id(
        FinalSpaceConfig.CHARACTERS_ENDPOINT, character["id"])

    assert api_character["id"] == character["id"]
    assert api_character["name"] == character["name"]
    assert api_character["status"] == character["status"]
    assert api_character["species"] == character["species"]
    assert api_character["gender"] == character["gender"]
    assert api_character["hair"] == character["hair"]
    assert api_character["origin"] == character["origin"]


def test_character_not_exists(final_space_api_client):
    character = CharactersProvider.fake_character()

    with pytest.raises(requests.exceptions.HTTPError):
        final_space_api_client.get_by_id(
            FinalSpaceConfig.CHARACTERS_ENDPOINT, character["id"])
