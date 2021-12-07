# Think about feed back
# Testing
# Add the ability to


from questions import aston_questions
import random
import os
from os import system, name
import time
# # import gspread
# from google.oauth.service_account import Credentials

# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# # Accesses the excel sheet itself
# CREDS = Credentials.from_service_account_file('creds.json')
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# SHEET = GSPREAD_CLIENT.open('aston_quiz_score')

# # Identifies the actual sheet in the excel
# score_sheet = SHEET.worksheet('scoreboard')

def add_to_leaderboard():
    """
    This will add all users scores to excel sheet
    """
    # NEEDS TO GET THE USERS NAME FROM GETS_USERNAME
    # NEEDS TO GET USERS SCORE AT END OF LOOP AND ADD IT INTO THE SPREADSHEET



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
    users_name = str(input(""))
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


def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


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
    point = 0
    while i < question_selection:
        print(game_questions[i]["question"])
        print(f"1 - {game_questions[i]['answers'][0]} 2 - {game_questions[i]['answers'][1]} 3- {game_questions[i]['answers'][2]}")
        print()
        correct_answer = generate_correct_answer(game_questions[i])
        users_choice = user_gameplay_input()
        if users_choice == correct_answer:
            point += 1
            print(f"Thats correct well done you now have {point} point!")
        else:
            print("Thats incorrect im afraid oh well onto the next question")
        i = i + 1
    add_to_leaderboard()


def generate_correct_answer(game_questions):
    """
    generates the correct answer
    """
    if game_questions['correct'] == game_questions['answers'][0]:
        return 1
    elif game_questions['correct'] == game_questions['answers'][1]:
        return 2
    elif game_questions['correct'] == game_questions['answers'][2]:
        return 3


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
                return users_choice
        except Exception:
            print("You didnt obviously read any of my hard work its 1 2 or 3 !!!!!")


startup()
