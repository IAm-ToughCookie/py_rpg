from classes.game import bcolors

def draw_titlescreen():
    print(bcolors.BOLD + "┌" + 70 * "─" + "┐" + bcolors.ENDC)
    print(bcolors.BOLD + "|" + 70 * " " + "|" + bcolors.ENDC)
    print(bcolors.BOLD + "|" + 70 * " " + "|" + bcolors.ENDC)
    print(bcolors.BOLD + "|" + 28 * " " + "THIS IS AN RPG" + 28 * " " + "|" + bcolors.ENDC)
    print(bcolors.BOLD + "|" + 25 * " " + "Choose:" + "   1. Play" + 28 * " " + "|" + bcolors.ENDC)
    print(bcolors.BOLD + "|" + 32 * " " + "   2. Help" + 28 * " " + "|" + bcolors.ENDC)
    print(bcolors.BOLD + "|" + 32 * " " + "   3. Quit" + 28 * " " + "|" + bcolors.ENDC)
    print(bcolors.BOLD + "|" + 70 * " " + "|" + bcolors.ENDC)
    print(bcolors.BOLD + "|" + 70 * " " + "|" + bcolors.ENDC)
    print(bcolors.BOLD + "└" + 70 * "─" + "┘" + bcolors.ENDC)


def title_choice():
    running = False
    while not running:
        title_input = input(">_   ")
        if title_input is "1":
            return True
        elif title_input is "2":
            print("Showing help")
            input("Press Enter to continue...")
            return True
        elif title_input is "3":
            raise SystemExit
        else:
            print("No valid input! Please use either 1, 2 or 3.")


def draw_gameover():
    print(bcolors.BOLD + "			        __" + bcolors.ENDC)
    print(bcolors.BOLD + "			    ___|  |___" + bcolors.ENDC)
    print(bcolors.BOLD + "			   |___    ___|" + bcolors.ENDC)
    print(bcolors.BOLD + "			       |  |" + bcolors.ENDC)
    print(bcolors.BOLD + "			    ___|  |___" + bcolors.ENDC)
    print(bcolors.BOLD + "		 ______/          \______" + bcolors.ENDC)
    print(bcolors.BOLD + "		|                        ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|       " + bcolors.FAIL +"+ R.I.P. +" + bcolors.ENDC, bcolors.BOLD + "      ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|    " + bcolors.FAIL + "Game       Over" + bcolors.ENDC, bcolors.BOLD + "    ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|                        ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|  Choose: 1. Play again ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|          2. Show Help  ||" + bcolors.ENDC)
    print(bcolors.BOLD + "	    |          3. Quit       ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|                        ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|                        ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|                        ||" + bcolors.ENDC)
    print(bcolors.BOLD + "		|                        ||" + bcolors.ENDC)
    print(bcolors.BOLD + "	//||/\,,./,||\,,....//||||..,,\|||" +bcolors.ENDC)