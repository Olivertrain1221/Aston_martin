# DO TESTING FORM EXCEL MATT SENT
# ASK TIM ABOUT GETTING FROM EXCEL SHEET and how to add the names and the user points
# pep 8 validation pep8online.com.

# READ ME
# WHERE AM I GOING TO USE THE CLEAR FUNCTION
# COLOR OF BACK GROUND
# Need to add validation to stop inputing a empty string...
# Need to also ensure it only takes in letters
# need it to get all info in the file in for five 10 15 and then work out heighest and


from questions import aston_questions
import random
import os
# from os import system, name
import time
import gspread
from google.oauth2.service_account import Credentials
import operator

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Accesses the excel sheet itself
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('aston_quiz_score')


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
    -       LeaderBoard       -
    -          Quit           -
    Type 'P' for play, 'R' for rules, 'L' for Leaderboard or 'Q' for quit.""")
    main_menu_selection()


def main_game_loop():
    users_name = gets_username()
    question_selection = question_amount_selection()
    game_questions = generate_random_question(question_selection)
    point = display_questions(game_questions, question_selection)
    add_to_leaderboard(users_name, point, question_selection)
    # startup()


def add_to_leaderboard(users_name, point, question_selection):
    """
    This will add all users scores to excel sheet
    """
    # NEEDS TO GET THE USERS NAME FROM GETS_USERNAME
    # NEEDS TO GET USERS SCORE AT END OF LOOP AND ADD IT INTO THE SPREADSHEET
    print("got to start of add leaderboard func")
    if question_selection == 5:
        score_sheet_five = SHEET.worksheet('scoreboard-5')
        score_sheet_five.append_row([users_name, point])
    elif question_selection == 10:
        score_sheet_ten = SHEET.worksheet('scoreboard-10')
        score_sheet_ten.append_row([users_name, point])
    elif question_selection == 15:
        score_sheet_fifteen = SHEET.worksheet('scoreboard-15')
        score_sheet_fifteen.append_row([users_name, point])
    print("got to end of add to leader board func, should of added")


def get_scoresheet_five():
    """
    Gets the values in scoresheet 5
    """
    worksheet_list_five = SHEET.get_worksheet(0)
    worksheet_values = worksheet_list_five.get_all_values()
    print(worksheet_values)
    score_five = worksheet_values
    l = len(score_five)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (score_five[j][1] > score_five[j + 1][1]):
                tempo = score_five[j]
                score_five[j] = score_five[j + 1]
                score_five[j + 1] = tempo
    print(score_five)
    # # sorted_score_five = dict( sorted(score_five.items(), key = operator.itemgetter(1), reverse = True))
    # print(sorted_score_five)
    return sorted_score_five


def get_scoresheet_ten():
    """
    Gets the values in scoresheet 5
    """
    worksheet_list_five = SHEET.get_worksheet(1)
    worksheet_values = worksheet_list_five.get_all_values()
    print(worksheet_values)
    score_five = worksheet_values
    l = len(score_five)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (score_five[j][1] > score_five[j + 1][1]):
                tempo = score_five[j]
                score_five[j] = score_five[j + 1]
                score_five[j + 1] = tempo
    print(score_five)
    return score_five


def get_scoresheet_fifteen():
    """
    Gets the values in scoresheet 5
    """
    worksheet_list_five = SHEET.get_worksheet(2)
    worksheet_values = worksheet_list_five.get_all_values()
    print(worksheet_values)
    score_five = worksheet_values
    l = len(score_five)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (score_five[j][1] > score_five[j + 1][1]):
                tempo = score_five[j]
                score_five[j] = score_five[j + 1]
                score_five[j + 1] = tempo
    print(sorted_score_five)
    return sorted_score_five


def leaderboard():
    """
    Gets the leaderboard on screen and prints top players from excel
    """
    # first_best_of_five = SHEET.worksheet('scoreboard-5')
    # retrieve all data from score  5, and put them all into a list/dict
    # sort the list/dict via point column values (highest to lowest), MAYBE SORT -1 if ypu get stuck (-1 usualy reverse)
    # grab 0 -1 2 index and display where i want.
    # # worksheet_five = sh.
    get_scoresheet_five()
    # best_of_five = worksheet.row_values(1)
    # thrid_best_of_five = 
    # first_best_of_ten = 
    # second_best_of_ten = 
    # thrid_best_of_ten = 
    # first_best_of_fifteen = 
    # second_best_of_fifteen = 
    # thrid_best_of_fifteen = 
    print(" " * 24 + "########  LEADERBOARD  ########" + " " * 25)
    print()
    print()
    print(" " * 32 + "_" * 9 + " " * 34)
    # print(" " * 32 + "|" + " " * 5 + "|" + " " * 34)
    # print(" " * 32 + "|" + " " * 5 + "|" + " " * 34) TEMP SEE TOP IN RUNNING
    print(" " * 31 + "|" + " " * 3 + "1ST" + " " * 3 + "|" + " " * 34)
    print(" " * 31 + "|" + " " * 9 + "|" + " " * 34)
    print(" " * 25 + "_" * 6 + "/" + " " * 9 + "\\" + "_" * 7)
    print(" " * 24 + "|" + " " + "2ND" + " " * 17 + "3RD" + "|")
    print(" " * 24 + "|" + " " * 24 + "|")
    print(" " * 24 + "|" + "_" * 24 + "|")
    # print(" " * 25 + "|" + " " * 20 + "|" + " " * 34) # EDITING
    print()
    print()  # Users name
    print()  # Users point
    print(" " * 9 + "_" * 9 + " " * 38 + "_" * 9 + " " * 8)
    print(" " * 8 + "|" + " " * 3 + "1ST" + " " * 3 + "|" + " " * 36 + "|" + " " * 3 + "1ST" + " " * 3 + "|" + " " * 8)
    print(" " * 8 + "|" + " " * 9 + "|" + " " * 36 + "|" + " " * 9 + "|" + " " * 8)
    print(" " * 2 + "_" * 6 + "/" + " " * 9 + "\\" + "_" * 6 + " " * 23 + "_" * 7 + "/" + " " * 10 + "\\" + "_" * 7)
    print(" " * 1 + "|" + " " + "2ND" + " " * 16 + "3RD" + "|" + " " * 21 + "|" + " " + "2ND" + " " * 19 + "3RD" + "|")
    print(" " * 1 + "|" + " " * 23 + "|" + " " * 21 + "|" + " " * 26 + "|")
    print(" " * 1 + "|" + " " * 23 + "|" + " " * 21 + "|" + " " * 26 + "|")
    print('''Press M for menu to return''')
    try:
        while True:
            return_to_menu = input("")
            return_to_menu = return_to_menu.upper()
            if return_to_menu not in ["M"]:
                raise Exception
            else:
                startup()
    except Exception:
        clear()
        print(" DERRRRR try inputing 'M'")
        leaderboard()


def main_menu_selection():
    """
    Checking what the user inputs and validates,
    """
    try:
        while True:
            option = input("")
            option = option.upper()
            if option not in ["P", "R", "L", "Q"]:
                raise Exception
            else:
                if option == 'P':
                    main_game_loop()
                    break
                elif option == 'R':
                    rule_options()
                    break
                elif option == 'Q':
                    startup()
                    break
                elif option == 'L':
                    leaderboard()
                    break
    except Exception:
        clear()
        print('''Hmmm you didnt follow the rules!!! You entered please try
again with valid input.So once again Please type "P" to play,
"R" to remind the rules or "Q" to quit.''')
        user_main_menu()


def gets_username():
    """
    Gets the users name
    """
    clear()
    print("Good choice on playing, but first lets get the intials to your name!")
    try:
        while True:
            users_name = str(input("Enter 1 to 3 letters:\n"))
            if len(users_name) <= 3 and users_name.isalpha():
                clear()
                time.sleep(1.5)
                print(f"Excellent thankyou for entering your name: {users_name}")
                time.sleep(1)
                return users_name
            else:
                print("Just your initials Wakey wakey")
    except Exception:
        clear()
        gets_username()


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
                startup()
    except Exception:
        print(" DERRRRR try 'M'")
        rule_options()


def question_amount_selection():
    """
    Allows the user to select amount of questions
    """
    print("Please enter the amount of questions you would like")
    while True:
        try:
            question_selection = int(input("5, 10, 15:\n"))
            if question_selection not in [5, 10, 15]:
                raise Exception
            else:
                clear()
                return question_selection
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
    return game_questions


def display_questions(game_questions, question_selection):
    """
    Gets the random questions generated and then displays
    """
    i = 0
    point = 0
    while i < question_selection:
        print(game_questions[i]["question"])
        print(f"1 - {game_questions[i]['answers'][0]}")
        print(f"2 - {game_questions[i]['answers'][1]}")
        print(f"3 - {game_questions[i]['answers'][2]}")
        print()
        correct_answer = generate_correct_answer(game_questions[i])
        users_choice = user_gameplay_input()
        if users_choice == correct_answer:
            point += 1
            print(f"Thats correct well done you now have {point} point!")
        else:
            print("Thats incorrect im afraid oh well onto the next question")
        time.sleep(3)
        clear()
        i = i + 1

    return point


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
    print("Please select your selection (1, 2, 3):\n")
    while True:
        try:
            users_choice = input("1, 2 or 3:\n")
            users_choice = int(users_choice)
            clear()
            print(f"You selected {str(users_choice)}!")
            if users_choice not in [1, 2, 3]:
                raise Exception
            else:
                return users_choice
        except Exception:
            print("You didnt obviously read any of my hard work. its 1 2 or 3!")


startup()