# ping-pong-xiiProj
PingPong - A project made by Dev Radadia and Dheer Banker
The aim of the project is to create a ping-pong game with basic 1v1 options and a smooth, intuitive gameplay.

Salient Features:

	1) The project is divided into 5 packages:
		i) image - Contains the images used in the project
		ii) r - Contains the screen-wise strings, resources and font styles used in the project
		iii) screens - Contains the logic for every screen in the project, with a module for every screen
		iv) sound - Contains the sounds used in the project
		v) sprites - Contains the different pygame drawables that have been used frequently in the project, like ball, paddle, button, etc.


	2) All the GUI Elements in the project are developed solely using pygame, from scratch, in order to keep a consistent GUI

	3) The project also includes various sounds in it, which are played, for example, when a button is clicked, or when the ball bounces.


	4) There are a total of 6 screens in the project
		i) About - Tells the user about the developers and the basic controls of the game
		ii) Main Menu - The main screen that has options to go to the other screens.
		iii) Player Names - Where players can enter their names and choose their colours
		iv) Game - The game screen, where the players play.
		v) Pause - The screen which comes up when players choose to pause the game
		vi) EndGame - The screen which declares the winner of the game just played


	5) All the screens are then bound and controlled using "The Game.py", the main controller code of this project.