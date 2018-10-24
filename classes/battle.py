from classes.visual import Colors, Gui
import random


def battle_loop(players, enemies, player_items, running):
    battle = running
    while battle:
        print("\033[H\033[J")
        print(Gui.separatorA + "========")
        print(Colors.BOLD + "NAME     HP                                        MP")
        for player in players:
            player.get_stats()
        print("ENEMIES:", Gui.separatorA)
        for enemy in enemies:
            enemy.get_enemy_stats()

        for player in players:
            player.choose_action()
            choice = input(Colors.BOLD + "\nChoose action:    " + Colors.ENDC)
            index = int(choice) - 1

            print("You chose", choice + "\n")

            if index == 0:
                dmg = player.generate_damage()
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(dmg)

                if enemies[enemy].hp is 0:
                    print("\nYou have attacked for", dmg, "and killed", enemies[enemy].name, "!")
                    del enemies[enemy]
                    if not enemies:
                        return 1
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
                    print(Colors.FAIL + "\nYou don't have enough MP!" + Colors.ENDC)
                    continue

                player.reduce_mp(spell.cost)

                if spell.type == "white":
                    player.heal(magic_dmg)
                    print(Colors.OKBLUE + "\n" + spell.name + " heals " + player.name + " for", magic_dmg, "HP."
                          + Colors.ENDC)
                elif spell.type == "black":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(magic_dmg)
                    if enemies[enemy].hp is 0:
                        print(Colors.OKBLUE + "Your", str.lower(spell.name), "deals", magic_dmg, "damage and killed",
                              enemies[enemy].name,
                              "!" + Colors.ENDC)
                        del enemies[enemy]
                        if not enemies:
                            return 1
                    else:
                        print(Colors.OKBLUE + "Your", str.lower(spell.name), "deals", magic_dmg, "damage to",
                              enemies[enemy].name + Colors.ENDC)
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
                    print(Colors.OKGREEN + "\n" + item.name + " heals" + player.name + " for", str(item.prop) + "HP!"
                          + Colors.ENDC)

                elif item.type == "elixir":
                    if item.name == "Mega Elixir":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                        print(Colors.OKGREEN + "\n" + item.name + " fully restored HP and MP of your party!"
                              + Colors.ENDC)
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                        print(Colors.OKGREEN + "\n" + item.name + " fully restored" + "HP and MP" + " to" + player.name
                              + Colors.ENDC)

                elif item.type == "attack":
                    item_dmg = item.generate_damage()
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(item_dmg)
                    if enemies[enemy].hp is 0:
                        print(Colors.OKGREEN + "\n" + item.name + " deals", item_dmg, "damage and kills",
                              enemies[enemy].name + "!" + Colors.ENDC)
                        del enemies[enemy]
                        if not enemies:
                            return 1
                    else:
                        print(Colors.OKGREEN + "\n" + item.name + " deals", item_dmg, "damage" + " to",
                              enemies[enemy].name + "!" + Colors.ENDC)
                        enemies[enemy].get_enemy_stats()

        if not enemies:
            return 1
        elif not players:
            return 0
        else:
            i = 0
            for enemy in enemies:
                # enemy_choice = 1
                target = random.randrange(0, len(players))
                enemy_dmg = enemies[i].generate_damage()
                players[target].take_damage(enemy_dmg)
                if players[target].get_hp() == 0:
                    print(enemies[i].name, "attacks", players[target].name, "for", enemy_dmg, "damage.",
                          players[target].name, "has died!")
                    del players[target]
                    if not players:
                        return 0
                else:
                    print(enemies[i].name,  "attacks", players[target].name, "for", enemy_dmg, "damage.")
                i += 1
