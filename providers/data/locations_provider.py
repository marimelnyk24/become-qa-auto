class LocationsProvider:

    @staticmethod
    def existing_location():
        return {
            'id': 1,
            'name': 'Earth',
            'type': 'Planet',
            'inhabitants': ["Humans", "Animals", "Robots", "Aliens"],
            'img_url': 'https://finalspaceapi.com/api/location/image/earth.jpg',
        }

    @staticmethod
    def fake_location():
        return{
            'id': 59404769605,
            'name': 'name',
            'type': 'type',
            'inhabitants': ["noone"],
            'img_url': 'https://some.website.com',
        }
