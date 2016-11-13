class Player(object):

    def __init__(self, name):
        self.name = name
        self.balance = 50
        self.plants = []

    def __str__(self):
        return 'Player: {name}'.format(name=self.name)

    def grant_resources(self, resource_type, count):
        raise Exception('Not implemented')
