import random
from classes.game import bcolors


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def choose_action(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("     " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("     " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_items(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD  + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("     " + str(i) + ".", item["item"].name + ":", item["item"].desc, "(x" + str(item["qty"]) + ")")
            i += 1

    def get_stats(self):
        print("                  ________________________           _____________")
        print(bcolors.BOLD + str(self.name) +
              str(self.hp) + "/" + str(
            self.maxhp) + " |" + bcolors.OKGREEN + "████                " + bcolors.ENDC, bcolors.BOLD +
              " |   " + str(self.mp) + "/" + str(
            self.maxmp) + " |" + bcolors.OKBLUE + "███       " + bcolors.ENDC, bcolors.BOLD + "|")