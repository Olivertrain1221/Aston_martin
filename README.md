# Aston Martin Quiz
## Introduction
The Aston Martin quiz is a browser built quiz with Python. It is a simple multiple choice based on the prestigious vehicle brand Aston Martin, highlighting the vehicles specs, comforts and interesting facts.
As the game was developed in Python for use in the terminal, it utilises the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

View the live website on [Heroku](https://aston-martin-quiz.herokuapp.com) Please note: To open any links in this document in a new browser tab, please press cntrl + Click.


## UX
### The Strategy Plane
* Aston Martin is intended to be a fun knowledge based quiz that people can take and will be ranked in a spreadsheet with other players, suitable for individual users looking to play a game for short or medium periods of time. Given the limitations of the terminal-based interface, care will need to be taken to incorporate some form of a visual stimulus.

#### Site Goals
* To provide users with a fun and simple to play quiz.
* To provide users with alternative options to choose a different amount of questions.
* To provide users with the ability to open a spreadsheet and see there ranking in comparison of other players

#### User Stories
* As a user I want an online quiz about a luxury car brandw
* As a user I want to be able to control the amount of questions that will be asked.
As a user I want to be able to compare my results with other players of the games.
#### The Scope Plane
**Features planned:**
* As there are certain restrictions in the scope of the development of the application, such as the terminal confines and methods of deployment. It will be important to ensure all functionality is contained within the game terminal screen.
* Despite the confines of the terminal window, the site should be visually stimulating with a graphic/image behind it and clear to the user that it is a quiz.
* Three question amount options should be available to the user	5 – 10 - 15.

### The Structure Plane
User Story:
> As a user, I want a fun and simple quiz to test my knowledge

Acceptance Criteria:
* It should be clear to the user that this is a quiz, what the quiz is about and how to play it with a option to read rules.
Implementation:
* The layout, use of askiart helps in order to create a fun user themed quiz. I also have used a background image to enable to user to feel in a luxurey quiz like the brand itself i have also added along the project validation for each user input.

User Story:
 > As a user, I want to be able to check my points and how many I have got in comparison to other players.
Acceptance Criteria:
* The user should have the option to check back on previous records and see there ranking
Implementation:
* The user will have the ability to read through in a seperate excel sheet all of the players along with there points achieved

### The Skeleton Plane
#### Wireframe mock-ups
Given that the application will be run within a terminal emulator which was provided within the CI template, there are limited options available in regards to how the program is displayed. Early on within the development of the theme of the quiz it made sense to have a luxury feel photo to to the luxury brand this then fitted in with the project and contents in the quiz to further the UI more pleasing to the user, I located a suitable background image on iStock. To position the terminal appropriately for the background graphic, and keeping user experience in mind, I decided to centre the terminal horizontally on the screen.  

### Logic Flow
To develop the logical steps required within the quiz, along with understanding how the different functions within the quiz logic elements would interact, I created a flow chart detailing the individual steps for the game. The full image can be viewed here Logic Flow Diagram
The game logic can be broken down into main sections. The initial startup runs and produces the askii art it then runs a game loop which calls functions to loop generate and validate different information, from username, points, creating question selection for the user.

### Game Loop
 
The player will input what they would like to play a 5,10,15 quiz this will then establish the amount of questions produced from Aston martin
I will utilise a variety of return methods into a game loop in order to be able to pull and pass specific user data into other functions, therefore I will not have to pass information from loop to loop to loop.

### The Surface Plane
#### Design
Once I had decided on the theme of the quiz itself ie Aston Martin due to my mechanical background, I therefore knew the colour scheme and silhouette image I wanted as my background.

### Features
#### Welcome Screen
At the start of game the user is greeted with a menu which consists of a Quit option, Leaderboard option, Rules and Play option users are told what they are required to input for them to access a menu.

---------------------

#### Instructions Screen
If users select the instructions option from the main menu the screen will display an overview of te game and how to play. Aswell as the option to return to the main menu.

-----------------------

#### Leaderboard Screen
If the user selects the leaderboard option it prints a leaderboard to the screen and shows 1,2,3 for the 5, 10 and 15 game option and it gets the highest users points along with the key to that value to ensure its a live leaderboard

------------------------

#### Play option
When selecting the play option the game then starts the game loop which then does the below.

---------------------------

#### Question amount selection
When the user confirms that they would like to play the game, they are greeted by a message asking them  hjow many questions in the game would they like to play.

-----------------

#### Name Option
The option is then given to the user to put in two alphabetic characters there intitials this is so it can show there name in the leaderboard with there point achieved in the excel sheet.

--------------------------

Once the name has been inputted the game loop comences and start to generate the questions from a seperate file. The questions are then displayed along witht the potential answers and the option to input a 1,2,3 this is then up to the user to input there choice.

------------------------- 

This then calls for the function to pass in the actual correct answer in comparison to the users guess. Depending on if it is correct depends on what the code odes next. 

--------------

If the answer inputted by the user is the correct answer it adds a point to the users score and gives a well done message witht the current users point value.

-------------------------

If the answer inputted by the user is wrong it gives the user a message of that incorrect onto the next question.

----------------------

After the game is finished it adds the users initials and there score to the excelsheet. Thi is how the leaderboard gets all of the players initials and there points and works out accordingly a 1st, 2nd, 3rd


### Future Enhancements
In the future I would add more questions to the questions file as although it generates the questions randomly there are only 30 questions currently.

### Testing
### Testing Strategy
I took a two-stage approach to testing the application. The first stage was continuous testing as the application was being developed. With the application being based within the terminal, it was straight forward to test functions and print statements as they were being developed using the terminal within the IDE I was also able to check validation easily for any user inputs to ensure only text could be put in nothing else when required and only the correct input could be inputted when asked 5, 10, 15

#### December 4th, 2021.
I started an issue on Github that I wasn’t able to sort on the spot on my main menus validation. Which I update when I was able to assess the issue and identify the code required fixing this. The update in the issue shows also my correction and what I did to resolve the issue.

----------------

#### December 7th, 2021.
I discovered a new bug that was a hidden issue that I hadn’t thought about correctly. This was for the main game loop. Randomly it would not generate a question.... this therefore was an issue. Due to the game generating questions randomly anyway it was hard to find out at what question in the questions file was throwing it off. Upon reflect it should have been a simple spot. The reasoning behind this was because the code was getting 3 answers as well on the next line. Then printed the question and the 3 possible answers. It was unable to get 3 possible answers for any of the random questions that were only holding 2 possible answers (“true/false”).

----------------------

#### December 13th, 2021.
I recieved an email during my final stages of code testing saying my API had been suspended. i believed this to be due to a over use of refreshes and updates to the
file in a short space of time when under testing. This therefore stopped my code running at all.

--------------



