def startup():
    """
    Game starts with message and options
    """
    print("Welcome to the Aston Martin Quiz\n")
    print("""
                                 _..-------++._
                             _.-'/ |      _||  \"--._
                       __.--'`._/_\j_____/_||___\    `----.
                  _.--'_____    |          \     _____    /
                _j    /,---.\   |        =o |   /,---.\   |_
               [__]==// .-. \\==`===========/==// .-. \\=[__]
                 `-._|\ `-' /|___\_________/___|\ `-' /|_.'
                       `---'                     `---'""")

def user_main_menu():
    print("Are you ready to play?")
    print("""
    -          Play           -
    -          Rules          -
    -          Quit           -
    Type 'P' for play, 'R' for rules or 'Q' for quit.""")
    # main_menu_selection()



def main_menu_selection():
    """
    Checking what the user inputs
    """
    option = ''
    while option not in ['P', 'R', 'Q']:
        
        if option == 'P':
            game_play()
            break
        elif option == 'R':
            rule_options()
            break
        elif option == 'Q':
            startup()
        else:
            print('\nHmmm you didnt follow the rules!!! please try again with valid input. So once again Please type "P" to play, "R" to remind the rules or "Q" to quit.')
            continue


def game_play():
    """
    Game startup of quiz
    """


def rule_options():
    """
    when selected will display rules
    """
    print("Welcome to the Aston Martin quiz, a quiz for all you buzzing petrol heads!\n")
    print("In this game you will be asked a range of questions and the answers will need to be\n inputted but using the numbers on your keyboard '1, 2, 3'")


def main():
    startup()
    user_main_menu()


main()