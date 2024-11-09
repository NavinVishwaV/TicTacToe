# TicTacToe
Tic Tac Toe game created in Python with a graphical user interface using Tkinter

Tic Tac Toe Game - README

Overview

This Tic Tac Toe game project provides a graphical user interface (GUI) using Python’s Tkinter library and includes two game modes:
	1.	Player vs Player (PvP): Two players play against each other.
	2.	Player vs Computer (PvC): The player competes against a computer opponent with simple AI.

Project Structure

The project is divided into three main Python files, each serving a specific role:
	1.	TicTacToe_main.py - Main entry point where the player selects the game mode.
	•	Displays options to start either PvP or PvC mode.
	•	Each mode loads a separate game window, which is closed and returned to the main menu on exit.
	2.	TicTacToe_PVP.py - Implements the Player vs Player (PvP) game mode.
	•	Handles game logic for alternating turns, win conditions, and score tracking between two players.
	3.	TicTacToe_PVC.py - Implements the Player vs Computer (PvC) mode.
	•	Contains game logic for player and computer turns, with the computer’s AI making random moves.
	•	Tracks scores for both player and computer.

Game Features

1. Main Menu (in TicTacToe_main.py)

	•	Interface: This main menu window provides game mode options:
	•	Player vs Player: Opens the Tic Tac Toe game in a two-player (PvP) format.
	•	Player vs Computer: Opens the Tic Tac Toe game in a single-player format against a computer (PvC).
	•	Exit: Closes the application.
	•	Functionality:
	•	Each button initializes the selected game mode, opening a new game window, or exits the program.
	•	Both game modes return to this main menu when closed.

2. Player vs Player Mode (PvP) - TicTacToe_PVP.py

	•	Gameplay:
	•	Turn-Based: Alternates turns between Player X and Player O.
	•	Move Validation: Prevents moves on occupied cells.
	•	Win Detection:
	•	Checks for winning combinations after each move (rows, columns, and diagonals).
	•	Displays a message if a player wins or if the game ends in a draw.
	•	Score Tracking:
	•	Tracks and displays each player’s score.
	•	Increments the winning player’s score after each round.
	•	Restart Option:
	•	After each game (win or draw), the game board resets automatically.

3. Player vs Computer Mode (PvC) - TicTacToe_PVC.py

	•	Gameplay:
	•	Player as X: The player always plays as X.
	•	Computer as O: The computer takes random available moves on its turn.
	•	Move Validation: Prevents moves on already occupied cells.
	•	Win Detection:
	•	Detects winning combinations and announces a win or draw.
	•	Resets the board after each game round.
	•	Score Tracking:
	•	Maintains separate scores for the player and computer.
	•	Updates the displayed scores after each round.

Running the Game

To play the game, you will need Python installed on your computer along with the Tkinter library for the GUI.
	1.	Check that Python is installed:
	•	Open a terminal and type:

python --version


	•	If Python is not installed, download and install it from Python’s website.

	2.	Install Tkinter (if not already installed):
	•	Windows/Mac: Tkinter usually comes pre-installed.
	•	Linux: Install Tkinter using:

sudo apt-get install python3-tk


	3.	Run the Game:
	•	Open a terminal and navigate to the project folder.
	•	Run the following command to start the game:

python TicTacToe_main.py



How to Play

	1.	Starting the Game:
	•	Run TicTacToe_main.py to open the main menu, where you can choose either:
	•	Player vs Player mode to play with another person.
	•	Player vs Computer mode to play against the computer.
	•	Select your preferred mode to start a new game.
	2.	Making Moves:
	•	Click on any empty cell to place your marker.
	•	The game alternates between players (PvP) or between the player and computer (PvC) after each move.
	3.	Game Outcomes:
	•	Win: The game will display a message indicating which player won.
	•	Draw: If all cells are filled without a winner, it announces a draw.
	•	Restart: The game board automatically resets for a new round after a win or draw.
	4.	Scorekeeping:
	•	Each win is recorded, with scores displayed at the top of the window.
	•	Scores reset only when the application is closed and reopened.

Requirements

	•	Python 3.x: Necessary to run the code.
	•	Tkinter Library: Required for the GUI.

Example Usage

	1.	Running the Game:

python TicTacToe_main.py


	2.	Navigating the Interface:
	•	Select Player vs Player for a two-player experience.
	•	Select Player vs Computer to play against the AI.
	•	Click Exit to close the application.

Credits

This Tic Tac Toe project demonstrates the use of Tkinter for GUI creation and Python for implementing game logic, offering a beginner-friendly game experience in both Player vs Player and Player vs Computer formats.
