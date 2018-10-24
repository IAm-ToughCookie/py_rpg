class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Gui:
    separatorA = "============================================================="
    separatorB = "-------------------------------------------------------------"


def draw_titlescreen():
    print(Colors.BOLD + "┌" + 70 * "─" + "┐" + Colors.ENDC)
    print(Colors.BOLD + "|" + 70 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 70 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 28 * " " + "THIS IS AN RPG" + 28 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 25 * " " + "Choose:" + "   1. Play" + 28 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 32 * " " + "   2. Help" + 28 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 32 * " " + "   3. Quit" + 28 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 70 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 70 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "└" + 70 * "─" + "┘" + Colors.ENDC)


def draw_gameover():
    print(Colors.BOLD + "			        __" + Colors.ENDC)
    print(Colors.BOLD + "			    ___|  |___" + Colors.ENDC)
    print(Colors.BOLD + "			   |___    ___|" + Colors.ENDC)
    print(Colors.BOLD + "			       |  |" + Colors.ENDC)
    print(Colors.BOLD + "			    ___|  |___" + Colors.ENDC)
    print(Colors.BOLD + "		 ______/          \______" + Colors.ENDC)
    print(Colors.BOLD + "		|                        ||" + Colors.ENDC)
    print(Colors.BOLD + "		|       " + Colors.FAIL + "+ R.I.P. +" + Colors.ENDC, Colors.BOLD + "      ||" + Colors.ENDC)
    print(Colors.BOLD + "		|    " + Colors.FAIL + "Game       Over" + Colors.ENDC, Colors.BOLD + "    ||" + Colors.ENDC)
    print(Colors.BOLD + "		|                        ||" + Colors.ENDC)
    print(Colors.BOLD + "		|  Choose: 1. Play again ||" + Colors.ENDC)
    print(Colors.BOLD + "		|          2. Show Help  ||" + Colors.ENDC)
    print(Colors.BOLD + "	    |          3. Quit       ||" + Colors.ENDC)
    print(Colors.BOLD + "		|                        ||" + Colors.ENDC)
    print(Colors.BOLD + "		|                        ||" + Colors.ENDC)
    print(Colors.BOLD + "		|                        ||" + Colors.ENDC)
    print(Colors.BOLD + "		|                        ||" + Colors.ENDC)
    print(Colors.BOLD + "	//||/\,,./,||\,,....//||||..,,\|||" + Colors.ENDC)


def draw_win():
    print(Colors.BOLD + "┌" + 70 * "─" + "┐" + Colors.ENDC)
    print(Colors.BOLD + "|" + 70 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 70 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 28 * " " + "YOU WON" + 35 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 25 * " " + "Choose:" + "   1. Play" + 28 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 32 * " " + "   2. Help" + 28 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 32 * " " + "   3. Quit" + 28 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 70 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "|" + 70 * " " + "|" + Colors.ENDC)
    print(Colors.BOLD + "└" + 70 * "─" + "┘" + Colors.ENDC)


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


def go_choice():
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