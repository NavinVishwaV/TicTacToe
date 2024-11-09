# TicTacToe_PVC.py
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToePvC(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe - PvC")
        self.turn = "X"  # Player is X, Computer is O
        self.board = [""] * 9
        self.buttons = []
        self.player_score = 0
        self.computer_score = 0
        self.create_widgets()

    def create_widgets(self):
        self.score_label = tk.Label(self, text=f"Player: {self.player_score} | Computer: {self.computer_score}", font=("Arial", 16))
        self.score_label.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(9):
            button = tk.Button(self, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=(i//3)+1, column=i%3)
            self.buttons.append(button)
        
        exit_button = tk.Button(self, text="Exit", command=self.destroy, font=("Arial", 14))
        exit_button.grid(row=4, column=0, columnspan=3, pady=10)

    def player_move(self, index):
        if self.board[index] == "" and self.turn == "X":
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_winner("X"):
                self.player_score += 1
                messagebox.showinfo("Game Over", "Player wins!")
                self.update_score()
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.turn = "O"
                self.computer_move()

    def computer_move(self):
        available_moves = [i for i, val in enumerate(self.board) if val == ""]
        if available_moves:
            move = random.choice(available_moves)
            self.board[move] = "O"
            self.buttons[move].config(text="O")
            if self.check_winner("O"):
                self.computer_score += 1
                messagebox.showinfo("Game Over", "Computer wins!")
                self.update_score()
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.turn = "X"

    def check_winner(self, player):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.turn = "X"
        for button in self.buttons:
            button.config(text="")

    def update_score(self):
        self.score_label.config(text=f"Player: {self.player_score} | Computer: {self.computer_score}")