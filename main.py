# Import necessary libraries
import random
import tkinter as tk
from tkinter import messagebox

class NumberDivisionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Division Game")
        self.root.configure(bg='#2E3B55')

        self.generated_numbers = [num for num in random.sample(range(10000, 20001), 100) if num % 6 == 0][:5]
        self.human_score = 0
        self.computer_score = 0
        self.current_number = 0
        self.current_player = 'human'

        self.setup_gui()

    def setup_gui(self):
        title_label = tk.Label(self.root, text="Number Division Game", font=("Helvetica", 24, "bold"), bg='#2E3B55', fg='white')
        title_label.pack(pady=20)

        self.label = tk.Label(self.root, text="Choose a number to start:", font=("Helvetica", 14), bg='#2E3B55', fg='white')
        self.label.pack(pady=5)

        self.number_var = tk.StringVar(self.root)
        self.number_var.set(self.generated_numbers[0])

        self.number_menu = tk.OptionMenu(self.root, self.number_var, *self.generated_numbers)
        self.number_menu.config(font=("Helvetica", 12), bg='#4A6274', fg='white')
        self.number_menu.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, font=("Helvetica", 14), bg='#4CAF50', fg='white')
        self.start_button.pack(pady=10)

        self.info_frame = tk.Frame(self.root, bg='#2E3B55')
        self.info_frame.pack(pady=10)

        self.info_label = tk.Label(self.info_frame, text="", font=("Helvetica", 14), bg='#4A6274', fg='white', width=40, height=4)
        self.info_label.pack(pady=5)

        self.move_label = tk.Label(self.root, text="Choose division (2 or 3):", font=("Helvetica", 14), bg='#2E3B55', fg='white')
        self.move_label.pack(pady=5)

        self.move_entry = tk.Entry(self.root, font=("Helvetica", 14), width=5)
        self.move_entry.pack(pady=5)

        self.move_button = tk.Button(self.root, text="Make Move", command=self.make_move, font=("Helvetica", 14), bg='#2196F3', fg='white')
        self.move_button.pack(pady=10)

        self.reset_button = tk.Button(self.root, text="New Game", command=self.reset_game, font=("Helvetica", 14), bg='#F44336', fg='white')
        self.reset_button.pack(pady=10)

        self.algorithm_label = tk.Label(self.root, text="Choose algorithm for computer:", font=("Helvetica", 14), bg='#2E3B55', fg='white')
        self.algorithm_label.pack(pady=5)

        self.algorithm_var = tk.StringVar(self.root)
        self.algorithm_var.set("Minimax")

        self.algorithm_menu = tk.OptionMenu(self.root, self.algorithm_var, "Minimax", "Alpha-Beta")
        self.algorithm_menu.config(font=("Helvetica", 12), bg='#4A6274', fg='white')
        self.algorithm_menu.pack(pady=5)

    def start_game(self):
        self.current_number = int(self.number_var.get())
        self.update_info()

    def make_move(self):
        try:
            move = int(self.move_entry.get())
            if move not in [2, 3] or self.current_number % move != 0:
                raise ValueError("Invalid move")

            if move == 2:
                self.current_number //= 2
                if self.current_player == 'human':
                    self.computer_score += 2
                else:
                    self.human_score += 2

            elif move == 3:
                self.current_number //= 3
                if self.current_player == 'human':
                    self.human_score += 3
                else:
                    self.computer_score += 3

            if self.is_game_over() or not self.valid_moves_remaining():
                self.end_game()
                return

            self.switch_player()
            self.update_info()

            if self.current_player == 'computer':
                self.computer_move()

        except ValueError:
            messagebox.showerror("Error", "Invalid move. Choose 2 or 3 and ensure it's a valid division.")

    def computer_move(self):
        algorithm = self.algorithm_var.get()
        move = self.minimax_move() if algorithm == "Minimax" else self.alpha_beta_move()
        self.move_entry.delete(0, tk.END)
        self.move_entry.insert(0, str(move))
        self.make_move()

    def minimax_move(self):
        return 2 if self.current_number % 2 == 0 else 3

    def alpha_beta_move(self):
        return 2 if self.current_number % 2 == 0 else 3

    def switch_player(self):
        self.current_player = 'computer' if self.current_player == 'human' else 'human'

    def is_game_over(self):
        return self.current_number <= 10

    def valid_moves_remaining(self):
        return self.current_number % 2 == 0 or self.current_number % 3 == 0

    def get_winner(self):
        if self.human_score > self.computer_score:
            return 'Human wins'
        elif self.computer_score > self.human_score:
            return 'Computer wins'
        else:
            return 'Draw'

    def update_info(self):
        self.info_label.config(text=f"Current Number: {self.current_number}\nHuman Score: {self.human_score}\nComputer Score: {self.computer_score}\nCurrent Player: {self.current_player}")

    def end_game(self):
        winner = self.get_winner()
        messagebox.showinfo("Game Over", winner)

    def reset_game(self):
        self.generated_numbers = [num for num in random.sample(range(10000, 20001), 100) if num % 6 == 0][:5]
        self.human_score = 0
        self.computer_score = 0
        self.current_number = 0
        self.current_player = 'human'

        menu = self.number_menu['menu']
        menu.delete(0, 'end')
        for number in self.generated_numbers:
            menu.add_command(label=number, command=tk._setit(self.number_var, number))
        self.number_var.set(self.generated_numbers[0])

        self.update_info()

if __name__ == '__main__':
    root = tk.Tk()
    game = NumberDivisionGame(root)
    root.mainloop()
