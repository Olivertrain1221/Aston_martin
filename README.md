# Aston Martin Quiz
## Introduction
The Aston Martin quiz is a browser built quiz with Python. It is a simple multiple-choice based on the prestigious vehicle brand Aston Martin, highlighting the vehicle's specs, comforts, and interesting facts.

As the game was developed in Python for use in the terminal, it utilizes the Code Institute Python Template to generate a "terminal" onto the page, making it available within a web browser.

![Aston Martin Quiz](documentation/images/startup_screen.png)

View the live website on [Heroku](https://aston-martin-quiz.herokuapp.com) Please note: To open any links in this document in a new browser tab, please press Ctrl + Click.


## UX
### The Strategy Plane
* Aston Martin is intended to be a fun knowledge-based quiz that people can take and will be ranked in a spreadsheet with other players, suitable for individual users looking to play a game for short or medium periods of time. Given the limitations of the terminal-based interface, care will need to be taken to incorporate some form of a visual stimulus.

#### Site Goals
* To provide users with a fun and simple-to-play quiz.
* To provide users with alternative options to choose a different amount of questions.
* To provide users with the ability to open the leaderboard option and see their ranking in comparison to other players.

#### User Stories
* As a user I want an online quiz about a luxury car brand
* As a user I want to be able to control the number of questions that will be asked.
As a user, I want to be able to compare my results with other players of the games.

#### The Scope Plane

**Features planned:**
* As there are certain restrictions in the scope of the development of the application, such as the terminal confines and methods of deployment. It will be important to ensure all functionality is contained within the game terminal screen.
* Despite the confines of the terminal window, the site should be visually stimulating with a graphic/image behind it and clear to the user that it is a quiz.
* Three question amount options should be available to the user 5 ??? 10 - 15.

### The Structure Plane
User Story:
As a user, I want a fun and simple quiz to test my knowledge.

Acceptance Criteria:
* It should be clear to the user that this is a quiz, what the quiz is about, and how to play it with an option to read rules.
Implementation:
* The layout, use of askiart helps to create a fun user-themed quiz. I also have used a background image to enable to user to feel in a luxury quiz like the brand itself I have also added along with the project validation for each user input.

User Story:
  As a user, I want to be able to check my points and how many I have got in comparison to other players.
Acceptance Criteria:
* The user should have the option to check back on previous records and see their ranking
Implementation:
* The user will have the ability to read through in a separate excel sheet all of the players along with their points achieved

I used lucid chart to help my understanding and to support this project's development. This allowed me as the developer to plan the logic and also how each input a user puts in will be checked.

![Game_flow](documentation/images/basic_game_running.png)
![Inputted_data](documentation/images/validating_user_data.png)

### The Skeleton Plane
#### Wireframe mock-ups
Given that the application will be run within a terminal emulator which was provided within the CI template, there are limited options available in regards to how the program is displayed. Early on within the development of the theme of the quiz, it made sense to have a luxury feel photo to the luxury brand this then fitted in with the project and contents in the quiz to further the UI more pleasing to the user, I located a suitable background image on iStock. To position the terminal appropriately for the background graphic, and keep user experience in mind, I decided to centre the terminal horizontally on the screen.  

### Logic Flow
To develop the logical steps required within the quiz, along with understanding how the different functions within the quiz logic elements would interact, I created a flow chart detailing the individual steps for the game. The full image can be viewed here Logic Flow Diagram
The game logic can be broken down into main sections. The initial startup runs and produces the askii art it then runs a game loop which calls functions to loop generate and validate different information, from username, points, creating question selection for the user.

### Game Loop
 
The player will input what they would like to play a 5,10,15 quiz this will then establish the number of questions produced from Aston martin
I will utilize a variety of return methods into a game loop to be able to pull and pass specific user data into other functions, therefore I will not have to pass information from loop to loop to loop.

### The Surface Plane
#### Design
Once I had decided on the theme of the quiz itself ie Aston Martin due to my mechanical background, I, therefore, knew the colour scheme and silhouette image I wanted as my background.

### Features
#### Welcome Screen
At the start of the game the user is greeted with a menu which consists of a Quit option, Leaderboard option, Rules and Play option users are told what they are required to input for them to access a menu.

![Startup screen](documentation/images/startup_screen.png)


#### Instructions Screen
If users select the instructions option from the main menu the screen will display an overview of the game and how to play. As well as the option to return to the main menu.

![Instructions screen](documentation/images/instructions.png)

#### Leaderboard Screen
If the user selects the leaderboard option it prints a leaderboard to the screen and shows 1,2,3 for the 5, 10, and 15 game option and it gets the highest users points along with the key to that value to ensure its a live leaderboard

![Leaderboard screen](documentation/images/leaderboard.png)

#### Play option
When selecting the play option the game then starts the game loop which then does the below.

#### Name Option
The option is then given to the user to put in two alphabetic characters their initials this is so it can show their name in the leaderboard with their point achieved in the excel sheet.

![Name Selection](documentation/images/name.png)

#### Question amount selection
When the user confirms that they would like to play the game, they are greeted by a message asking them how many questions in the game would they like to play.

![Amount of questions](documentation/images/amount_of_games.png)

Once the name has been inputted the game loop commences and starts to generate the questions from a separate file. The questions are then displayed along with the potential answers and the option to input a 1,2,3 this is then up to the user to input their choice.

![Game question layout](documentation/images/game_running.png) 

This then calls for the function to pass in the actual correct answer in comparison to the user's guess. Depending on if it is correct depends on what the code does next. 
If the answer inputted by the user is the correct answer it adds a point to the user's score and gives a well-done message with the current user's point value.

![Correct answer ](documentation/images/amount_of_games.png)

If the answer inputted by the user is wrong it gives the user a message of that incorrect onto the next question.

![Wrong answer](documentation/images/wrong_answer.png)

After the game is finished it adds the user's initials and their score to the excel sheet. This is how the leaderboard gets all of the players' initials and their points and works out accordingly a 1st, 2nd, 3rd



## Future Enhancements
In the future, I would add more questions to the questions file as although it generates the questions randomly there are only 30 questions currently.



## Testing
For all testing please click here to go to the [TESTING.md](TESTING.md)



## Libraries Utilised

#### Built-in Python Libraries
Several of the built-in python libraries were utilized to enable additional functionality within the application math.
The math library was imported to utilize the math.floor functionality. This was used during the calculation of the correct number of questions along with math.random to generate the random number to make sure that users didn't get the exact same questions. 

#### Time
The time library was also imported to utilize the time.sleep functionality. This enabled me to incorporate specific time delays within the program which adds to the player experience by simulating the time between the player answering their points going up or their correct/wrong message before the next question is displayed.

#### os
The os library was imported to utilize the os.system and os.name functionality. This enabled me to add functionality to the terminal emulator which allowed me to clear the previous print statements. This provides a clearer and more structured experience for the user.

#### GSpread
I also added in the GSpread function which allowed me to link the API for google sheets into the file so I could successfully create a live leaderboard that would change on every player's input.


## Deployment
The site was deployed via Heroku, and the live link can be found here - [Aston Martin Quiz Heroku](https://aston-martin-quiz.herokuapp.com)
The project was developed utilizing a Code Institute provided template. During the development of the project, the template was updated to increase functionality. I switched over to the new template mid-project which you can see within the commit history. Some of the deployment steps below are specifically required for the new CI template and may not apply to older versions, or different projects.
Project Deployment
To deploy the project through Heroku I followed these steps:
* Sign up / Log in to Heroku
* From the main Heroku Dashboard page select 'New' and then 'Create New App'
* Give the project a name - I entered Aston_Martin_Quiz and select a suitable region, then selected create app. The name of the app must be unique.
* This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the settings tab.
* This next step is required for creating the app when using the CI Python Deployment Template. If you created your own program without using the CI Template, you might not need to add a config var.
* In the config vars section selects the reveal config vars button. This will display the current config vars for the app, there should be nothing already there.
* In the KEY input field input PORT all in capitals, then in the VALUE field input 8000 and select the Add button to the right.
* Next select the add buildpack button below the config vars section.
* In the pop-up window select Python as your first build pack and select save changes.
* Then repeat the steps to add a node.js buildpack.
* The order of the buildpacks is important, in the list Python should be first with Node.js second. If they are not in this order, you can click and drag them to rearrange.
* Next navigate back to the deploy tab using the submenu at the top of the page.
* In the deployment method section select the GitHub - Connect to GitHub button and follow the steps prompted if any to connect your GitHub account
* In the Connect to GitHub section that appears, select the correct account, and enter the name of the repository, and select search.
* Once Heroku has located the repo select connect.
* This will connect the repo to the app within Heroku. Below the Apps Connected to Heroku section will be the Automatic Deploys section.
* In this section, confirm the correct branch of the repo is selected in the drop-down box, and then click the Enable Automatic Deploys button
* This will ensure whenever you change something in the repo and push the changes to GitHub, Heroku will rebuild the app. If you prefer to do this manually you can utilize the manual deployment options further down. For this project, I utilized the Automatic Deployment to enable me to check changes I made to the app as I developed it.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.
* There is then a link to run it in the heroku site which opens the game into a new separate tab.

Once in the file, Because I am including packages in the requirements.txt file. you must also do the following:

1: how to download just the packages required for this project (pip3 install -r requirements.txt)
and
2: how to freeze the commands for a local copy of this project on their own account (pip3 freeze --local > requirements.txt)

## Credits
#### Code
I was informed of a method to clear the terminal by mentor Tim Nelson who had found the method in [slack overview](https://stackoverflow.com/questions/2084508/clear-terminal-in-python) provided by. Tim had suggested that I used the method successfully within my project to keep the window clearer to improve UX.
![ClearTerminal](documentation/images/clear_term.png)

### Content

#### Background Image
I as stated above already had an idea of how I was going to link the image behind the terminal along with what style of photo I wanted.

#### Stack Overflow
Stack overflow was useful a few times whilst I developed my understanding of filtering and sorting through data from an excel sheet that was appended into a dict.

### Acknowledgements
I'd like to thank the following:
* My mentor Tim Nelson for encouraging me throughout the project and providing me with supporting and useful coding skills and knowledge.
* Matt Bodden for helping with the planning of the logic in regards to how it will run (game loop), general coding queries, Aswell as supplying me with a mockup for how he carried out his testing to encourage me to show further advancement in the way I am testing the code that I am building.
* CI Tutor support for helping in regards to sorting through the list of my excel sheet.
