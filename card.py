import random

# Card class representing a single card
class Card:
    def __init__(self, name, cost, attack, defense):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.defense = defense
        self.has_attacked = False

    def __str__(self):
        return f"{self.name}: cost={self.cost}, attack={self.attack}, defense={self.defense}"
