# TicTacToe_PVP.py
import tkinter as tk
from tkinter import messagebox

class TicTacToePvP(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe - PvP")
        self.turn = "X"
        self.board = [""] * 9
        self.buttons = []
        self.player_x_score = 0
        self.player_o_score = 0
        self.create_widgets()

    def create_widgets(self):
        self.score_label = tk.Label(self, text=f"Player X: {self.player_x_score} | Player O: {self.player_o_score}", font=("Arial", 16))
        self.score_label.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(9):
            button = tk.Button(self, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.click(i))
            button.grid(row=(i//3)+1, column=i%3)
            self.buttons.append(button)
        
        exit_button = tk.Button(self, text="Exit", command=self.destroy, font=("Arial", 14))
        exit_button.grid(row=4, column=0, columnspan=3, pady=10)

    def click(self, index):
        if self.board[index] == "":
            self.board[index] = self.turn
            self.buttons[index].config(text=self.turn)
            if self.check_winner():
                if self.turn == "X":
                    self.player_x_score += 1
                else:
                    self.player_o_score += 1
                messagebox.showinfo("Game Over", f"Player {self.turn} wins!")
                self.update_score()
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def reset_game(self):
        self.board = [""] * 9
        self.turn = "X"
        for button in self.buttons:
            button.config(text="")

    def update_score(self):
        self.score_label.config(text=f"Player X: {self.player_x_score} | Player O: {self.player_o_score}")