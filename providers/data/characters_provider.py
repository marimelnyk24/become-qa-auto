class CharactersProvider:

    @staticmethod
    def existing_character():
        return {
            'id': 1,
            'name': 'Gary Goodspeed',
            'status': 'Alive',
            'species': 'Human',
            'gender': 'Male',
            'hair': 'Blonde',
            'origin': 'Earth'
        }

    @staticmethod
    def fake_character():
        return{
            'id': 300084755,
            'name': 'name',
            'status': 'status',
            'species': 'species',
            'gender': 'gender',
            'hair': 'hair',
            'origin': 'moon'
        }
