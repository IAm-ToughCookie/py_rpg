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

    def choose_target(self, enemies):
        i = 1
        print(bcolors.FAIL + bcolors.BOLD + "TARGET" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(str(i) + ".", enemy.name)
                i += 1
        choice = int(input(bcolors.BOLD + "Choose target:    " + bcolors.ENDC)) -1
        return choice

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "▋"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "▋"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)

            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string
        else:
            current_mp = mp_string

        n_string = str(self.name) + ":"
        current_n = ""

        if len(n_string) < 9:
            n_decreased = 9 - len(n_string)

            while n_decreased > 0:
                current_n += " "
                n_decreased -= 1

            current_n = n_string + current_n
        else:
            current_n = n_string
        print(bcolors.BOLD + " " * 20 + "_" * len(hp_bar) + " " * 15 + "_" * len(mp_bar))
        print(bcolors.BOLD + current_n + current_hp + " |" + bcolors.OKGREEN + hp_bar +
              bcolors.ENDC + bcolors.BOLD + "|     " + current_mp + " |" + bcolors.OKBLUE + mp_bar +
              bcolors.ENDC + bcolors.BOLD + "|")
        print(bcolors.BOLD + " " * 20 + "¯" * len(hp_bar) + " " * 15 + "¯" * len(mp_bar))

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "▋"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        n_string = str(self.name) + ":"
        current_n = ""

        if len(n_string) < 9:
            n_decreased = 9 - len(n_string)

            while n_decreased > 0:
                current_n += " "
                n_decreased -= 1

            current_n = n_string + current_n
        else:
            current_n = n_string

        print(bcolors.BOLD + " " * 20 + "_" * len(hp_bar))
        print(bcolors.BOLD + current_n + current_hp + " |" + bcolors.FAIL + hp_bar +
              bcolors.ENDC + bcolors.BOLD + "|")
        print(bcolors.BOLD + " " * 20 + "¯" * len(hp_bar))