import requests


class FinalSpaceApi():

    def __init__(self, base_url):
        self.base_url = base_url

    def get_by_id(self, endpoint, id):
        r = requests.get(f"{self.base_url}{endpoint}/{id}")
        r.raise_for_status()

        return r.json()
