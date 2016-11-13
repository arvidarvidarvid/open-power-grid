from player import Player
from plant import PlantSet


class Game(object):

    def __init__(self, name, number_of_players):
        self.name = name
        self.players = []
        self.init_players(number_of_players)
        self.plants = PlantSet()

    def __str__(self):
        return 'Game: %s' % self.name

    def init_players(self, number_of_players):
        for i in range(number_of_players):
            player_name = input('What is the name of player %s? ' % i)
            self.players.append(Player(player_name))
