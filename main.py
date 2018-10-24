from classes import setup
from classes.visual import Colors, draw_titlescreen, title_choice, draw_gameover, go_choice, draw_win
from classes.battle import battle_loop
from classes.setup import setup_game

# TODO Add AI to NPCs
# TODO Add Shop where you can buy/sell items. Shop has it's own inventory that gets expanded with stuff you sell
# TODO Move spells into own file
# TODO Add character classes with different attributes
# TODO Add Spellbook (own file)
# TODO Add class trainers where you can learn new spells depending on your class
# TODO Rework Winning screen

draw_titlescreen()
running = title_choice()

while running:
    setup_game()

    print(Colors.FAIL + Colors.BOLD + " " * 20 + "AN ENEMY ATTACKS!" + Colors.ENDC)

    battle_result = battle_loop(setup.players, setup.enemies, setup.player_items, running)

    if battle_result == 1:
        draw_win()
        choice = title_choice()
        if choice:
            continue
    elif battle_result == 0:
        draw_gameover()
        choice = go_choice()
        if choice:
            continue
