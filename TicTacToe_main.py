import tkinter as tk
from TicTacToe_PVP import TicTacToePvP
from TicTacToe_PVC import TicTacToePvC

def start_pvp():
    game_window = TicTacToePvP()
    game_window.mainloop()

def start_pvc():
    game_window = TicTacToePvC()
    game_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")

    tk.Label(root, text="Choose Game Mode", font=("Arial", 18)).pack(pady=10)

    pvp_button = tk.Button(root, text="Player vs Player", command=start_pvp, font=("Arial", 14))
    pvc_button = tk.Button(root, text="Player vs Computer", command=start_pvc, font=("Arial", 14))
    exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 14))

    pvp_button.pack(pady=5)
    pvc_button.pack(pady=5)
    exit_button.pack(pady=5)

    root.mainloop()