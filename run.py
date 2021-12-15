# DO TESTING FORM EXCEL MATT SENT
# pep 8 validation pep8online.com.
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
    end_of_game_message(users_name, point)
    add_to_leaderboard(question_selection, users_name, point)
    startup()


def end_of_game_message(users_name, point):
    clear()
    print("Thankyou ever so much for playing my the Aston Martin Quiz")
    print("")
    print(f'Well {users_name} you achieved {point} points')
    time.sleep(8.0)


def add_to_leaderboard(question_selection, users_name, point):
    """
    This will add all users scores to excel sheet
    """
    if question_selection == 5:
        score_sheet_five = SHEET.worksheet('scoreboard-5')
        score_sheet_five.append_row([users_name, point])
    elif question_selection == 10:
        score_sheet_ten = SHEET.worksheet('scoreboard-10')
        score_sheet_ten.append_row([users_name, point])
    elif question_selection == 15:
        score_sheet_fifteen = SHEET.worksheet('scoreboard-15')
        score_sheet_fifteen.append_row([users_name, point])


def get_scoresheet_list(rounds, position):
    # worksheet
    if rounds == 5:
        worksheet = SHEET.worksheet('scoreboard-5')
    elif rounds == 10:
        worksheet = SHEET.worksheet('scoreboard-10')
    elif rounds == 15:
        worksheet = SHEET.worksheet('scoreboard-15')
    # print(worksheet)
    worksheet_values = worksheet.get_all_values()
    score = worksheet_values
    length_score = len(score)
    for i in range(0, length_score):
        for j in range(0, length_score-i-1):
            if (score[j][1] > score[j + 1][1]):
                tempo = score[j]
                score[j] = score[j + 1]
                score[j + 1] = tempo
    # print("running end of scoresheet new")
    return score[length_score - (position + 1)]


def leaderboard():
    """
    Gets the leaderboard on screen and prints top players from excel
    """
    print("got to leaderboard")
    first_place_five = get_scoresheet_list(5, 1)
    first_place_ten = get_scoresheet_list(10, 1)
    first_place_fifteen = get_scoresheet_list(15, 1)
    second_place_five = get_scoresheet_list(5, 2)
    second_place_ten = get_scoresheet_list(10, 2)
    second_place_fifteen = get_scoresheet_list(15, 2)
    third_place_five = get_scoresheet_list(5, 3)
    third_place_ten = get_scoresheet_list(10, 3)
    third_place_fifteen = get_scoresheet_list(15, 3)
    print(" " * 24 + "########  LEADERBOARD  ########" + " " * 25)
    print()
    print(" " * 33 + first_place_five[0] + " " + first_place_five[1])
    print(" " * 32 + "_" * 9 + " " * 34)
    print(" " * 31 + "|" + " " * 3 + "1ST" + " " * 3 + "|" + " " * 34)
    print(" " * 25 + second_place_five[0] + " " + second_place_five[1] + " " * 2 + "|" + " " * 9 + "|" + " " * 2 + third_place_five[0] + " " + third_place_five[1])
    print(" " * 25 + "_" * 6 + "/" + " " * 9 + "\\" + "_" * 7)
    print(" " * 24 + "|" + " " + "2ND" + " " * 17 + "3RD" + "|")
    print(" " * 24 + "|" + " " * 9 + "5 quiz" + " " * 9 + "|")
    print(" " * 24 + "|" + "_" * 24 + "|")
    print()
    print()
    print(" " * 11 + first_place_ten[0] + " " + first_place_ten[1] + " " * 41 + first_place_fifteen[0] + " " + first_place_fifteen[1])
    print(" " * 9 + "_" * 9 + " " * 38 + "_" * 9 + " " * 8)
    print(" " * 8 + "|" + " " * 3 + "1ST" + " " * 3 + "|" + " " * 36 + "|" + " " * 3 + "1ST" + " " * 3 + "|" + " " * 8)
    print(" " * 2 + second_place_ten[0] + " " + second_place_ten[1] + "|" + " " * 9 + "|" + " " * 2 + third_place_ten[0] + " " + third_place_ten[1] + " " * 22 + second_place_fifteen[0] + " " + second_place_fifteen[1] +" " * 2 + "|" + " " * 9 + "|" + " " * 2 + third_place_fifteen[0] + " " + third_place_fifteen[1])
    print(" " * 2 + "_" * 6 + "/" + " " * 9 + "\\" + "_" * 6 + " " * 23 + "_" * 7 + "/" + " " * 10 + "\\" + "_" * 7)
    print(" " * 1 + "|" + " " + "2ND" + " " * 16 + "3RD" + "|" + " " * 21 + "|" + " " + "2ND" + " " * 19 + "3RD" + "|")
    print(" " * 1 + "|" + " " * 23 + "|" + " " * 21 + "|" + " " * 26 + "|")
    print(" " * 1 + "|" + " " * 8 + "10 Quiz" + " " * 8 + "|" + " " * 21 + "|" + " " * 10 + "15 quiz" + " " * 9 + "|")
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
        print("Nice try")
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
