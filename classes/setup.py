from classes.characters import Person
from classes.magic import Spell
from classes.inventory import Item


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

# Player & Enemies 1460,900,1600
player1 = Person("Dan", 1460, 150, 60, 34, player_spells, player_items)
player2 = Person("Priest", 900, 399, 15, 34, player_spells, player_items)
player3 = Person("Druid", 1600, 250, 60, 85, player_spells, player_items)

# 150, 2000, 150
enemy1 = Person("Imp", 150, 10, 20, 5, [], [])
enemy2 = Person("Goblin", 2000, 20, 200, 25, [], [])
enemy3 = Person("Imp", 150, 10, 20, 5, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]


def setup_game():
    # Spell library
    # Damage
    global fire, thunder, blizzard, meteor, quake, cure, cura
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
    global potion, hipotion, superpotion, elixir, megaelixir, bomb, knife
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

    global player1, player2, player3, enemy1, enemy2, enemy3
    # Player & Enemies 1460,900,1600
    player1 = Person("Dan", 1460, 150, 60, 34, player_spells, player_items)
    player2 = Person("Priest", 900, 399, 15, 34, player_spells, player_items)
    player3 = Person("Druid", 1600, 250, 60, 85, player_spells, player_items)

    # 150, 2000, 150
    enemy1 = Person("Imp", 150, 10, 20, 5, [], [])
    enemy2 = Person("Goblin", 2000, 20, 200, 25, [], [])
    enemy3 = Person("Imp", 150, 10, 20, 5, [], [])

    global players, enemies
    players = [player1, player2, player3]
    enemies = [enemy1, enemy2, enemy3]