import os

PREFIX = 'SOURCE'

class Source():
    @staticmethod
    def loadFromEnv():
        name = os.environ[f'{PREFIX}_NAME']
        identifier = os.environ[f'{PREFIX}_IDENTIFIER']

        return Source({
            'name': name,
            'identifier': identifier
        })

    def __init__(self, config):
        self.name = config['name']
        self.identifier = config['identifier']

    def serialize(self):
        return {
            'name': self.name,
            'identifier': self.identifier
        }
