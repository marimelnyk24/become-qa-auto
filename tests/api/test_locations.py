import pytest
import requests
from config.config import FinalSpaceConfig
from providers.data.locations_provider import LocationsProvider


def test_location_exists(final_space_api_client):
    location = LocationsProvider.existing_location()
    api_location = final_space_api_client.get_by_id(
        FinalSpaceConfig.LOCATIONS_ENDPOINT, location["id"])

    assert api_location["id"] == location["id"]
    assert api_location["name"] == location["name"]
    assert api_location["type"] == location["type"]
    assert sorted(api_location["inhabitants"]) == sorted(
        location["inhabitants"])
    assert api_location["img_url"] == location["img_url"]


def test_location_not_exists(final_space_api_client):
    location = LocationsProvider.fake_location()

    with pytest.raises(requests.exceptions.HTTPError):
        final_space_api_client.get_by_id(
            FinalSpaceConfig.LOCATIONS_ENDPOINT, location["id"])
