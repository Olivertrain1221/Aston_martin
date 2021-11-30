from questions import aston_questions
import random
import os
from os import system, name
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def startup():
    """
    Game starts with message and options
    """
    clear()
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
    user_main_menu()


def user_main_menu():
    """
    Displays the main menu and gives the user the option to
    read rules, playu or quit
    """
    print("Are you ready to play?")
    print("""
    -          Play           -
    -          Rules          -
    -          Quit           -
    Type 'P' for play, 'R' for rules or 'Q' for quit.""")
    main_menu_selection()


def main_menu_selection():
    """
    Checking what the user inputs and validates,
    """
    try:
        while True:
            option = input("")
            option = option.upper()
            if option not in ["P", "R", "Q"]:
                raise Exception
            else:
                if option == 'P':
                    gets_username()
                    break
                elif option == 'R':
                    rule_options()
                    break
                elif option == 'Q':
                    startup()
                    break
    except Exception:
        print('''Hmmm you didnt follow the rules!!! You entered please try
again with valid input.So once again Please type "P" to play,
"R" to remind the rules or "Q" to quit.''')
        user_main_menu()


def gets_username():
    """
    Gets the users name
    """
    clear()
    print("Good choice on playing, but first lets get your name!")
    users_name = input("")
    clear()
    time.sleep(1.5)
    print(f"Excellent thankyou for entering your name: {users_name}")
    time.sleep(1)
    question_amount_selection()


def rule_options():
    """
    when selected will display rules a
    """
    clear()
    print('''Welcome to the Aston Martin quiz, a quiz for all you buzzing petrol
heads!''')
    print('''In this game you will be asked a range of questions and the 
answers will need to be inputted but using the numbers on your keyboard
"1, 2, 3".''')
    print('''Press M for menu to return''')
    try:
        while True:
            return_to_menu = input("")
            return_to_menu = return_to_menu.upper()
            if return_to_menu not in ["M"]:
                raise Exception
            else:
                main()
    except Exception:
        print(" DERRRRR try 'M'")
        rule_options()


def question_amount_selection():
    """
    Allows the user to select amount of questions
    """
    print('''Please enter either a 5, 10, 15 to select the amount of questions
''')
    while True:
        try:
            question_selection = int(input(""))
            if question_selection not in [5, 10, 15]:
                raise Exception
            else:
                if question_selection == 5:
                    print("working on 5")
                    display_five_questions()
                    break
                elif question_selection == 10:
                    # function for 10 q
                    print("working on 10")
                    display_ten_questions()
                    break
                elif question_selection == 15:
                    # function for 15 q
                    print("working on 15")
                    display_fifteen_questions()
                    break
        except Exception:
            print('''Hmmm you didnt follow the rules AGAIN!!! Please enter 5, 10, 
15 ''')
            question_amount_selection()


def generate_random_question(question_selection):
    previous_number = []
    game_questions = []

    while len(game_questions) < user_choice:
        x = rand.int(0, len(question_selection)) """between 0 and 29 to do"""
        if x not in previous_number:
            previous_number.append(x)
            game_questions.append(array_of_questions[x])
        # return to game loop now

def display_questions(game_questions):
    while i < user_wants:
        print(game_questions[0]("question"))
        print(game_questions[0, 1, 2]("answers"))
        user_gamechoice_input()


def array_of_questions():
    """
    Gets the questions in a form of an array
    """
    question = questions_dict["question"]
    answers = questions_dict["answers"]
    correct = questions_dict["correct"]


def user_gameplay_input():
    users_choice = input("")

    
startup()