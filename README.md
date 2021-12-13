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
 
