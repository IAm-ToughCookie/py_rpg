from classes.characters import Person
from classes.game import bcolors, gui
from classes.magic import Spell
from classes.inventory import Item
import random

# TODO Add AI to NPCs
# TODO Add Shop where you can buy/sell items. Shop has it's own inventory that gets expanded with stuff you sell
# TODO Move spells into own file
# TODO Add character classes with different attributes
# TODO Add Spellbook (own file)
# TODO Add class trainers where you can learn new spells depending on your class
# TODO Refactor main.py so it's just runs the game
# TODO Add title screen with "Play", "Help" and "Quit" options
# TODO import sys and os for clearing screen

# Spell library
# Damage
fire = Spell("Fire", 10, 100, "Fire", "black")
thunder = Spell("Thunder", 12, 124, "Lightning", "black")
blizzard = Spell("Blizzard", 10, 100, "Frost", "black")
meteor = Spell("Meteor", 10, 100, "Fire", "black")
quake = Spell("Quake", 14, 140, "Earth", "black")

# Heal
cure = Spell("Cure", 12, 120, "Light", "white")
cura = Spell("Cura", 18, 200, "Light", "white")

# Item Stock
# Healing-Items
potion = Item("Potion", "potion", "Heals 50HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 999)
megaelixir = Item("Mega Elixir", "elixir", "Fully restores HP/MP of all party members", 999)

# Attack-Items
bomb = Item("Bomb", "attack", "A throwable bomb. BIG BOOM", 500)
knife = Item("Throwing Knife", "attack", "A small throwing knife.", 50)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "qty": 15}, {"item": hipotion, "qty": 5},
                {"item": superpotion, "qty": 5}, {"item": elixir, "qty": 5},
                {"item": megaelixir, "qty": 2}, {"item": bomb, "qty": 2},
                {"item": knife, "qty": 20}]

# Player & Enemies
player1 = Person("Dan", 1460, 150, 60, 34, player_spells, player_items)
player2 = Person("Priest", 900, 399, 15, 34, player_spells, player_items)
player3 = Person("Druid", 1600, 250, 60, 85, player_spells, player_items)

enemy1 = Person("Imp", 150, 10, 20, 5, [], [])
enemy2 = Person("Goblin", 3000, 20, 200, 25, [], [])
enemy3 = Person("Imp", 150, 10, 20, 5, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + " " * 20 + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("\033[H\033[J")
    print(gui.separatorA + "========")
    print(bcolors.BOLD + "NAME     HP                                        MP")
    for player in players:
        player.get_stats()
    print("ENEMIES:", gui.separatorA)
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input(bcolors.BOLD + "\nChoose action:    " + bcolors.ENDC)
        index = int(choice) - 1

        print("You chose", choice + "\n")

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)

            if enemies[enemy].hp is 0:
                print("\nYou have attacked for", dmg, "and killed", enemies[enemy].name, "!")
                del enemies[enemy]
            else:
                print("\nYou attacked", enemies[enemy].name, "for", dmg, "damage!")
                enemies[enemy].get_enemy_stats()

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic:    ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nYou don't have enough MP!" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals " + player.name + " for", magic_dmg, "HP."
                      + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                if enemies[enemy].hp is 0:
                    print(bcolors.OKBLUE + "Your", str.lower(spell.name), "deals", magic_dmg, "damage and killed",
                          enemies[enemy].name,
                          "!" + bcolors.ENDC)
                    del enemies[enemy]
                else:
                    print(bcolors.OKBLUE + "Your", str.lower(spell.name), "deals", magic_dmg, "damage to",
                          enemies[enemy].name + bcolors.ENDC)
                    enemies[enemy].get_enemy_stats()

        elif index == 2:
            player.choose_items()
            item_choice = int(input("Choose item:    ")) - 1

            if item_choice == -1:
                continue

            item = player_items[item_choice]["item"]
            player.items[item_choice]["qty"] -= 1
            if player.items[item_choice]["qty"] == 0:
                del player.items[item_choice]

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals" + player.name + " for", str(item.prop) + "HP!"
                      + bcolors.ENDC)

            elif item.type == "elixir":
                if item.name == "Mega Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " fully restored HP and MP of your party!"
                          + bcolors.ENDC)
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " fully restored" + "HP and MP" + " to" + player.name
                          + bcolors.ENDC)

            elif item.type == "attack":
                item_dmg = item.generate_damage()
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item_dmg)
                if enemies[enemy].hp is 0:
                    print(bcolors.OKGREEN + "\n" + item.name + " deals", item_dmg, "damage and kills",
                          enemies[enemy].name + "!" + bcolors.ENDC)
                    del enemies[enemy]
                else:
                    print(bcolors.OKGREEN + "\n" + item.name + " deals", item_dmg, "damage" + " to",
                          enemies[enemy].name + "!" + bcolors.ENDC)
                    enemies[enemy].get_enemy_stats()

    if not enemies:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif not players:
        print(bcolors.FAIL + "You died!" + bcolors.ENDC)
        running = False
    else:
        i = 0
        for enemy in enemies:
            enemy_choice = 1
            target = random.randrange(0, len(players))
            enemy_dmg = enemies[i].generate_damage()
            players[target].take_damage(enemy_dmg)
            if players[target].get_hp() == 0:
                print(enemies[i].name, "attacks", players[target].name, "for", enemy_dmg, "damage.",
                      players[target].name, "has died!")
                del players[target]
            else:
                print(enemies[i].name,  "attacks", players[target].name, "for", enemy_dmg, "damage.")
            i += 1
