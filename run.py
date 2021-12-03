# Add user input into it next and to display
# validate the users input as to what the correct answeris
# then call a win/ lose func dependant on result (if)
# add counter into the game lives
#


from questions import aston_questions
import random
import os
from os import system, name
import time


def clear():
    """
    Adds the clear terminal function
    """
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
                    generate_random_question(question_selection)
                    break
                elif question_selection == 10:
                    # function for 10 q
                    generate_random_question(question_selection)
                    break
                elif question_selection == 15:
                    # function for 15 q
                    generate_random_question(question_selection)
                    break
        except Exception:
            print('''Hmmm you didnt follow the rules AGAIN!!! Please enter 5, 10, 
15 ''')
            question_amount_selection_loop()



def generate_random_question(question_selection):
    """
    Generates a random question by getting it from question_selections
    also uses user input to loop through depending on user input
    """
    previous_number = []
    game_questions = []
    while len(game_questions) < question_selection:
        x = random.randint(0, (len(aston_questions) - 1))
        if x not in previous_number:
            previous_number.append(x)
            game_questions.append(aston_questions[x])

    display_questions(game_questions, question_selection)


def display_questions(game_questions, question_selection):
    """
    Gets the random questions generated and then displays
    """
    i = 0
    while i < question_selection:
        print(game_questions[i]["question"])
        print(f"1 - {game_questions[i]['answers'][0]} 2 - {game_questions[i]['answers'][1]} 3- {game_questions[i]['answers'][2]}")
        print()
        i = i + 1
        user_gameplay_input()


def user_gameplay_input():
    """
    Users game play input
    """
    print("Please select either a 1, 2 or 3 for your answer")
    while True:
        try:
            users_choice = input("")
            users_choice = int(users_choice)
            print(f"You selected {str(users_choice)}!")
            if users_choice not in [1, 2, 3]:
                raise Exception
            else:
                #run the compare module#
                print("Got to users choice Else end")
        except Exception:
            print("You didnt obviously read any of my hard work its 1 2 or 3 !!!!!")

# def checks_user_to_correct(game_questions, users_choice):  # unsure on what variables required to pass through
#     """
#     Will compare users input to correct answer to verify
#     """
#     correct_answer = game_questions[0]]("correct")
#     if users_choice  #value as a str == correct_answer:
#         print("THATS CORRECT!!!")
#     else:
#         print("your wrong...... unlucky")


startup()
