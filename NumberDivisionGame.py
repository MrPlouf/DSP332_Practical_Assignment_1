import tkinter as tk
import random
from tkinter import messagebox


import GameLogic as gl
from graph import GameGraph

class NumberDivisionGame:
    def __init__(self, root):
        self.root = root
        self.game_tree = None
        self.root.title("Number Division Game")
        self.root.configure(bg='#2E3B55')
        self.reset_game()

    def setup_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Number Division Game", font=("Helvetica", 24, "bold"), bg='#2E3B55', fg='white').pack(
            pady=20)
        tk.Label(self.root, text="Choose a number to start:", font=("Helvetica", 14), bg='#2E3B55', fg='white').pack(
            pady=5)

        self.number_var = tk.StringVar(self.root)
        self.number_var.set(self.generated_numbers[0])
        tk.OptionMenu(self.root, self.number_var, *self.generated_numbers).pack(pady=5)

        tk.Button(self.root, text="Start Game", command=self.start_game, font=("Helvetica", 14), bg='#4CAF50',
                  fg='white').pack(pady=10)

        self.info_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg='#4A6274', fg='white', width=40,
                                   height=4)
        self.info_label.pack(pady=10)

        self.move_entry = tk.Entry(self.root, font=("Helvetica", 14), width=5)
        self.move_entry.pack(pady=5)
        tk.Button(self.root, text="Make Move", command=self.make_move, font=("Helvetica", 14), bg='#2196F3',
                  fg='white').pack(pady=10)

        tk.Button(self.root, text="New Game", command=self.reset_game, font=("Helvetica", 14), bg='#F44336',
                  fg='white').pack(pady=10)

    def start_game(self):
        self.current_number = int(self.number_var.get())
        self.human_score = 0
        self.computer_score = 0
        self.current_player = 'human'
        self.game_tree = GameGraph.build_game_tree(self.current_number, self.human_score, self.computer_score)
        self.update_info()

    def make_move(self):
        try:
            move = int(self.move_entry.get())
            if move not in gl.GameLogic.valid_moves(self.current_number):
                raise ValueError("Invalid move")

            self.current_number, score = gl.GameLogic.apply_move(self.current_number, move, self.current_player)
            if self.current_player == 'human':
                self.human_score += score
            else:
                self.computer_score += score

            self.move_entry.delete(0, tk.END)
            if gl.GameLogic.is_game_over(self.current_number):
                self.update_info()
                self.end_game()
                return

            self.switch_player()
            self.update_info()

            if self.current_player == 'computer':
                self.computer_move()
        except ValueError:
            messagebox.showerror("Error", "Invalid move. Choose 2 or 3 and ensure it's a valid division.")

    def computer_move(self):
        valid_moves = gl.GameLogic.valid_moves(self.current_number)
        if valid_moves:
            move = random.choice(valid_moves)
            self.current_number, score = gl.GameLogic.apply_move(self.current_number, move, 'computer')
            self.computer_score += score
            if gl.GameLogic.is_game_over(self.current_number):
                self.end_game()
                return
            self.switch_player()
            self.update_info()

    def switch_player(self):
        self.current_player = 'computer' if self.current_player == 'human' else 'human'

    def update_info(self):
        self.info_label.config(
            text=f"Current Number: {self.current_number}\nHuman Score: {self.human_score}\nComputer Score: {self.computer_score}\nCurrent Player: {self.current_player}")

    def end_game(self):
        winner = 'Human wins' if self.human_score > self.computer_score else 'Computer wins' if self.computer_score > self.human_score else 'Draw'
        messagebox.showinfo("Game Over", winner)
        if self.game_tree:
            self.game_tree.render('game_tree', format='png', view=True)
    def reset_game(self):
        self.generated_numbers = [num for num in random.sample(range(10000, 20001), 100) if num % 6 == 0][:5]
        self.human_score = 0
        self.computer_score = 0
        self.current_number = 0
        self.current_player = 'human'
        self.setup_gui()


if __name__ == '__main__':
    root = tk.Tk()
    game = NumberDivisionGame(root)
    root.mainloop()
