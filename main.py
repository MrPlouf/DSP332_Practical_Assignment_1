# import tkinter as tk
# from GameConstants import *
# from graph import *
#
# import random
# class NumberDivisionGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Number Division Game")
#         self.root.configure(bg='#2E3B55')
#
#         self.generated_numbers = [num for num in random.sample(range(GameConstants.MIN_VALUE, GameConstants.MAX_VALUE + 1), GameConstants.SAMPLE_SIZE) if num % GameConstants.DIVISIBLE_BY == 0][:GameConstants.CHOICES]
#         self.human_score = 0
#         self.computer_score = 0
#         self.current_number = 0
#         self.current_player = 'human'
#
#         self.setup_gui()
#
#     def setup_gui(self):
#         title_label = tk.Label(self.root, text="Number Division Game", font=("Helvetica", 24, "bold"), bg='#2E3B55', fg='white')
#         title_label.pack(pady=20)
#
#         self.label = tk.Label(self.root, text="Choose a number to start:", font=("Helvetica", 14), bg='#2E3B55', fg='white')
#         self.label.pack(pady=5)
#
#         self.number_var = tk.StringVar(self.root)
#         self.number_var.set(self.generated_numbers[0])
#
#         self.number_menu = tk.OptionMenu(self.root, self.number_var, *self.generated_numbers)
#         self.number_menu.config(font=("Helvetica", 12), bg='#4A6274', fg='white')
#         self.number_menu.pack(pady=5)
#
#         self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, font=("Helvetica", 14), bg='#4CAF50', fg='white')
#         self.start_button.pack(pady=10)
#
#         self.info_frame = tk.Frame(self.root, bg='#2E3B55')
#         self.info_frame.pack(pady=10)
#
#         self.info_label = tk.Label(self.info_frame, text="", font=("Helvetica", 14), bg='#4A6274', fg='white', width=40, height=4)
#         self.info_label.pack(pady=5)
#
#         self.move_label = tk.Label(self.root, text="Choose division (2 or 3):", font=("Helvetica", 14), bg='#2E3B55', fg='white')
#         self.move_label.pack(pady=5)
#
#         self.move_entry = tk.Entry(self.root, font=("Helvetica", 14), width=5)
#         self.move_entry.pack(pady=5)
#
#         self.move_button = tk.Button(self.root, text="Make Move", command=self.make_move, font=("Helvetica", 14), bg='#2196F3', fg='white')
#         self.move_button.pack(pady=10)
#
#         self.reset_button = tk.Button(self.root, text="New Game", command=self.reset_game, font=("Helvetica", 14), bg='#F44336', fg='white')
#         self.reset_button.pack(pady=10)
#
#         self.algorithm_label = tk.Label(self.root, text="Choose algorithm for computer:", font=("Helvetica", 14), bg='#2E3B55', fg='white')
#         self.algorithm_label.pack(pady=5)
#
#         self.algorithm_var = tk.StringVar(self.root)
#         self.algorithm_var.set("Minimax")
#
#         self.algorithm_menu = tk.OptionMenu(self.root, self.algorithm_var, "Minimax", "Alpha-Beta")
#         self.algorithm_menu.config(font=("Helvetica", 12), bg='#4A6274', fg='white')
#         self.algorithm_menu.pack(pady=5)
#
#     def make_move(self, number, depth, is_maximizing):
#         if number <= 10:
#             return (self.human_score - self.computer_score) if is_maximizing else (self.computer_score - self.human_score)
#
#         best_score = float('-inf') if is_maximizing else float('inf')
#         best_move = None
#
#         for move in [2, 3]:
#             if number % move == 0:
#                 next_number = number // move
#                 if is_maximizing:
#                     score = self.minimax_move(next_number, depth + 1, False)
#                     if score > best_score:
#                         best_score = score
#                         best_move = move
#                 else:
#                     score = self.make_move(next_number, depth + 1, True)
#                     if score < best_score:
#                         best_score = score
#                         best_move = move
#
#         return best_move if depth == 0 else best_score
#
#     def computer_move(self):
#         algorithm = self.algorithm_var.get()
#         if algorithm == "Minimax":
#             move = self.make_move(self.current_number, 0, True)
#         else:
#             move = 2 if self.current_number % 2 == 0 else 3
#
#         self.move_entry.delete(0, tk.END)
#         self.move_entry.insert(0, str(move))
#         self.make_move()
#
#     def start_game(self):
#         self.current_number = int(self.number_var.get())
#         self.update_info()
#
#     def update_info(self):
#         self.info_label.config(text=f"Current Number: {self.current_number}\nHuman Score: {self.human_score}\nComputer Score: {self.computer_score}\nCurrent Player: {self.current_player}")
from tkinter import *

from NumberDivisionGame import NumberDivisionGame

if __name__ == '__main__':
    root = Tk()
    game = NumberDivisionGame(root)
    root.mainloop()
