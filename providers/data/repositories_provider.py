from os import stat


class RepositoriesProvider:

    @staticmethod
    def existing_reporitory():
        return {
            'name': 'become_qa_auto',
            'total_count': 1,
            'items_count': 1
        }

    @staticmethod
    def non_existing_reporitory():
        return {
            'name': 'kdjjfhfjdsskjfhfeldsalsd',
            'total_count': 0,
            'items_count': 0
        }
