import random


class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.desc = description
        self.prop = prop

    def generate_damage(self):
        low = self.prop - 20
        high = self.prop + 20
        return random.randrange(low, high)