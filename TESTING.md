 # Test Cases and Execution Report
To navigate back to the main README click [here](README.md)

### Testing
### Testing Strategy
I took a two-stage approach to test the application. The first stage was continuous testing as the application was being developed. With the application being based within the terminal, it was straightforward to test functions and print statements as they were being developed using the terminal within the IDE I was also able to check validation easily for any user inputs to ensure only text could be put in nothing else when required and only the correct input could be inputted when asked 5, 10, 15



### Second stage testing
For the second stage of testing my project, I utilized a more formal structured approach and created a test schedule for the application which covered each logical cycle. I then proceeded to run through the manual tests that I had made and made sure to note any errors that I found. Where the code didn't do as expected, the code was altered to correct the behavior almost straight away unless it was a major issue which I documented via the Github issues section. After extensive testing the only issues. I found was the odd validation error that the user could input a symbol instead of their initials. Once the code was adjusted accordingly the code passed the validation.

The individual python files were also validated using pep8online.com further details are below.

### Testing Overview
Testing was divided into different sections to ensure everything was tested individually with test cases developed for each area.
 
### Validator Testing
pep8online.com - I utilized pep8online.com to validate my python code. All python files were checked with only lines being too long as an error and a whitespace issue.
I sorted these accordingly which are noted further down the file with valid pep8 validation

#### Screenshots of the validator reports are here:
![run.py](images/pep8_fail.PNG)
![questions.py](images/pep8_questions_fail.PNG)

### Notable Bugs

#### December 4th, 2021
I started an issue on Github that I wasn’t able to sort on the spot on my main menus validation. Which I update when I was able to assess the issue and identify the code required to fix this. The update in the issue shows also my correction and what I did to resolve the issue.

![Main menu validation bug](images/github_issues_main_menu_validation.PNG)

#### December 7th, 2021.
I discovered a new bug that was a hidden issue that I hadn’t thought about correctly. This was for the main game loop. Randomly it would not generate a question.... this, therefore, was an issue. Due to the game generating questions randomly anyway it was hard to find out at what question in the questions file was throwing it off. Upon reflecting it should have been a simple spot. The reasoning behind this was because the code was getting 3 answers as well on the next line. Then printed the question and the 3 possible answers. It was unable to get 3 possible answers for any of the random questions that were only held 2 possible answers (“true/false”).

![Main game loop bug](images/github_issues_random_question.PNG)

#### December 13th, 2021.
I received an email during my final stages of code testing saying my API had been suspended. I believed this to be due to the overuse of refreshes and updates to the
file in a short space of time when under testing. This, therefore, stopped my code from running at all.

![API Bug error isses](images/github_api_crash.PNG)


Below is a detailed excel sheet of all the testing carrid out with the supporting screenshots from the spreadsheet. You can view the spreadsheet [here.](documentation/testing-schedule-complete.pdf)


Test 1
![Test1](images/test_1.PNG)
![Test2](images/test_1a.PNG)
### Python Validation
The Python code was checked using the pep8 validator available at pep8online.com. Errors were reported for longer lines I edited my code accordingly until there were no reported errors by the validator. The following file however did include warnings regarding a line break before binary operator this is acceptable due to some code needing to be on more than one line.

list of files with warnings
run.py - 4 warnings

The point in the PEP8 guidelines can be found [here](https://www.python.org/dev/peps/pep-0008/) 

Screenshots of the validator reports are here

![run.py Pass](images/pep8_runpy_pass.PNG)

![questions.py Pass](images/questions_pep8_pass.PNG)


Test 2

Start Menu Functionality

The start menu input was tested for the correct validation of the user input. On correct input, the screen will redirect to the correct screen. On incorrect input, the input validation correctly displays an error message to the user to guide how to move on.

![Test2](images/test_2.PNG)

Instruction Screen Functionality

Input validation was also tested on the instructions screen along with testing that the user could launch the game from the screen. On incorrect input, the screen displays the correct error message with guidance on how to correctly input the required values. On correct input, the desired functionality proceeded as designed.

Leaderboard Screen Functionality

Input validation was also tested on the leaderboard screen along with testing that the user could launch the game from the screen. On incorrect input, the screen displays the correct error message with guidance on how to correctly input the required values. On correct input, the desired functionality proceeded as designed.

![Test3](images/test_2.PNG)

User initials input functionality

Input validation was also tested on the user initials screen along with testing that the user could launch the game from the screen. On incorrect input, the screen displays the correct error message with guidance on how to correctly input the required values. On correct input, the desired functionality proceeded as designed.

![Test4](images/test_3.PNG)

User question amount input functionality

Input validation was also tested on the number of questions to play the screen along with testing that the user could launch the game from the screen. On incorrect input, the screen displays the correct error message with guidance on how to correctly input the required values. On correct input, the desired functionality proceeded as designed.

![Test5](images/test_4.PNG)

User input to the game questions

Input validation was also tested on the game with actual input as an answer along with testing that the user could launch the game from the screen. On incorrect input, the screen displays the correct error message with guidance on how to correctly input the required values. On correct input, the desired functionality proceeded as designed.

![Test6](images/test_5.PNG)

User correct input to the game questions

Input validation was also tested on the user guessing the correct answer screen along with testing that the user could launch the game from the screen. On incorrect input, the screen displays the correct error message with guidance on how to correctly input the required values. On correct input, the desired functionality proceeded as designed.

![Test7](images/test_6.PNG)

At end of the game, it added to the sheets file

Checked that the code ran in the background to log the live leaderboard.

![Test8](images/test_7.PNG)

To return to my README.md click [here.](README.md)