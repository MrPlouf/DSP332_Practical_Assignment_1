import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import math
from functions import generate_valid_numbers 
from gametree import generate_complete_tree

class Main:
    """ Initializes UI, game state, and game flow. """

    #Initialisation of the different variables and functions used throughout the code
    def __init__(self, landing):

        #Frame config
        self.landing = landing
        self.landing.title("Practical Assignment 1 - Groupe 33") 
        self.landing.geometry("600x450")

        #Different windows base design (lightblue cause why not)
        self.Menu = tk.Frame(landing, bg="lightblue")
        self.Rules = tk.Frame(landing, bg="lightblue")
        self.Settings = tk.Frame(landing, bg="lightblue")
        self.About = tk.Frame(landing, bg="lightblue")
        self.NumberGeneration = tk.Frame(landing, bg="lightblue")
        self.Game = tk.Frame(landing, bg="lightblue")
        self.Results = tk.Frame(landing, bg="lightblue")

        #Variables used during the game
        #Default settings are: User start first and Minmax algorithm
        self.AlphaBetaAlgorithm = tk.IntVar()
        self.MinMaxAlgorithm = tk.IntVar(value=1) 
        self.UserStart = tk.IntVar(value=1)

        #Number for start number      
        self.chosenNumber = tk.IntVar(value=0)   
        self.algorithm_used = "Minimax" 

        #Score and Max Depth used in Algs         
        self.max_depth = 6                      
        self.human_score = 0
        self.computer_score = 0
        self.current_number = 0
        self.current_player = None

        #Tracks if the player WHOSE TURN IT IS at the current node is the maximizer
        self.is_maximizing_player = None

        #Game Tree Data: All tree and then current node
        self.game_tree = {}
        self.current_node_key = None

        #Creation of the different windows used thoughout the game (ini with buttons and text and all)
        self.Create_Menu()
        self.Create_Rules()
        self.Create_Settings()
        self.Create_About()
        self.Create_NumberGeneration()
        self.Create_Game()
        self.Create_Results()

        #Initial landing on page
        self.show_frame(self.Menu)



    #base game functions
    def _is_terminal_state(self, number):
        if number <= 10:
            return True
        if number > 10 and number % 2 != 0 and number % 3 != 0:
            return True
        return False

    def _get_valid_moves(self, number):
        moves = []
        if number <= 10:
            return []
        if number % 2 == 0:
            moves.append(2)
        if number % 3 == 0:
            moves.append(3)
        return moves

    def evaluate_heuristic(self, number, human_score, computer_score):

        if self._is_terminal_state(number):
             pass 
        score_diff = computer_score - human_score

        return score_diff

    def show_frame(self, frame):
        for f in [self.Menu, self.Rules, self.Settings, self.About, self.NumberGeneration, self.Game, self.Results]:
            f.grid_forget()
        frame.grid(row=0, column=0, sticky="nsew")
        self.landing.rowconfigure(0, weight=1)
        self.landing.columnconfigure(0, weight=1)

    def set_chosen_number(self, num):
        self.chosenNumber.set(num)
        
        if hasattr(self, 'start_game_button'): 
             if num > 0:
                  self.start_game_button.config(state=tk.NORMAL)
                  if hasattr(self, 'status_label_numgen'):
                    self.status_label_numgen.config(text=f"Selected: {num}. Ready to Start.")
             else:
                  #shount happen
                  self.start_game_button.config(state=tk.DISABLED)
                  if hasattr(self, 'status_label_numgen'):
                    self.status_label_numgen.config(text="Select a number")

    def Create_Menu(self):
        self.Menu.columnconfigure((0, 1, 2), weight=1)
        self.Menu.rowconfigure((0, 1, 2, 3), weight=1)
        tk.Label(self.Menu, text="Welcome to our assignment :D", bg="lightblue", font=("Arial", 16)).grid(row=0, columnspan=3, padx=10, pady=10, sticky="w")
        tk.Button(self.Menu, text="See Rules", command=lambda: self.show_frame(self.Rules), font=("Arial", 12)).grid(row=1, columnspan=2, column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Menu, text="About", command=lambda: self.show_frame(self.About), font=("Arial", 12)).grid(row=2, columnspan=2, column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Menu, text="Start Game Setup",
                  command=lambda: [self.reset_game_settings(), self.Create_NumberGeneration(), self.show_frame(self.NumberGeneration)],
                  font=("Arial", 12)).grid(row=3, columnspan=2, column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Menu, text="Settings", command=lambda: self.show_frame(self.Settings), font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=10, sticky="ne")

    def Create_Rules(self):
        self.Rules.columnconfigure((0, 1), weight=1)
        self.Rules.rowconfigure((0, 1, 2), weight=1)
        tk.Label(self.Rules, text="Rules given to us", bg="lightblue", font=("Arial", 14)).grid(row=0, padx=10, pady=10, sticky="w")
        rule_text = ("At the beginning of the game, the game software randomly generates 5 numbers between 10000 and 20000,"
                     "but initially divisible by both 3 and 2. The human player chooses which of the generated numbers "
                     "he wants to start the game with. \n \n"
                     "At the beginning of the game, the number chosen by the human player "
                     "is given. Both players have 0 points. The players take turns, each turn dividing the current number "
                     "by 2 or 3. If division by 2 is made, then 2 points are added to the opponent's score. If division by 3 "
                     "is made, 3 points are added to the player's score. The game ends as soon as a number less than or equal "
                     "to 10 has been acquired. The player whose turn it is when the number is <= 10 might not be able to move. "
                     "If no moves are possible (either <=10 or >10 and not divisible by 2 or 3), the game ends. "
                     "The player with the highest number of points wins.")
        tk.Label(self.Rules, text=rule_text, bg="lightblue", wraplength=500, font=("Arial", 12), justify="left").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Rules, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=2, column=1, padx=10, pady=10, sticky="se")

    def Create_About(self):
        self.About.columnconfigure((0, 1), weight=1)
        self.About.rowconfigure(tuple(range(7)), weight=1)
        tk.Label(self.About, text="Team Members", bg="lightblue", font=("Arial", 12)).grid(row=0, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Enzo Höhenberger", bg="lightblue", font=("Arial", 12)).grid(row=1, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Ahmed Dabbagh", bg="lightblue", font=("Arial", 12)).grid(row=2, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Andrii Nazarkevych", bg="lightblue", font=("Arial", 12)).grid(row=3, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Ijin Kunnel Thankachan", bg="lightblue", font=("Arial", 12)).grid(row=4, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Welathantrige Dawini Hasulu Boteju", bg="lightblue", font=("Arial", 12)).grid(row=5, padx=10, pady=10, sticky="w")
        tk.Button(self.About, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=6, column=1, padx=10, pady=10, sticky="se")

    def Change_Check_Value(self):
        
        #if not hasattr(self, 'warning_label'): return # Should not happen if called from Create_Settings

        if self.AlphaBetaAlgorithm.get() == 1 and self.MinMaxAlgorithm.get() == 1:
            self.warning_label.config(text="Select only one algorithm", fg="red")
            self.MinMaxAlgorithm.set(0)
            self.algorithm_used = "Alpha-Beta"
        elif self.AlphaBetaAlgorithm.get() == 1:
            self.algorithm_used = "Alpha-Beta"
            self.MinMaxAlgorithm.set(0)
        elif self.MinMaxAlgorithm.get() == 1:
            self.algorithm_used = "Minimax"
            self.AlphaBetaAlgorithm.set(0)
        else:
            self.warning_label.config(text="No algorithm selected, defaulting to Minimax", fg="orange")
            self.MinMaxAlgorithm.set(1) 
            self.algorithm_used = "Minimax"

        # Update combined warning label text
        algo_text = f"{self.algorithm_used} selected"
        start_text = "User starts first" if self.UserStart.get() == 1 else "Computer starts first"
        final_text = f"{algo_text}. {start_text}."

        # Determine color based on algo status
        #current_warning = self.warning_label.cget("text")
        #final_color = "green" # Default success color
        #if "Select only one" in current_warning: final_color = "red"
        #elif "defaulting" in current_warning: final_color = "orange"

        self.warning_label.config(text=final_text, fg="green")


    def Create_Settings(self):
        
        self.Settings.columnconfigure((0,1,2), weight=1)
        self.Settings.rowconfigure(tuple(range(7)), weight=1)

        tk.Label(self.Settings, text="Settings", bg="lightblue", font=("Arial", 14)).grid(row=0, padx=10, pady=10, sticky="w")
        tk.Label(self.Settings, text="Choose Algorithm:", fg="black", bg="lightblue", font=("Arial", 12)).grid(row=1, padx=10, pady=10, sticky="w")
        tk.Checkbutton(self.Settings, text="Minimax", variable=self.MinMaxAlgorithm, onvalue=1, offvalue=0, font=("Arial", 12), command=self.Change_Check_Value, bg="lightblue").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        tk.Checkbutton(self.Settings, text="Alpha Beta", variable=self.AlphaBetaAlgorithm, onvalue=1, offvalue=0, font=("Arial", 12), command=self.Change_Check_Value, bg="lightblue").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        tk.Checkbutton(self.Settings, text="User Starts first", variable=self.UserStart, onvalue=1, offvalue=0, font=("Arial", 12), command=self.Change_Check_Value, bg="lightblue").grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.warning_label = tk.Label(self.Settings, text="", fg="red", bg="lightblue", font=("Arial", 12), wraplength=350, justify="left")
        self.warning_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.Change_Check_Value()

        tk.Button(self.Settings, text="Go Back", command=lambda: [self.Change_Check_Value(), self.show_frame(self.Menu)]).grid(row=6, column=2, padx=10, pady=10, sticky="se")


    def Create_NumberGeneration(self):
        #using number generation function in function.py
        for widget in self.NumberGeneration.winfo_children(): widget.destroy()

        self.NumberGeneration.columnconfigure(tuple(range(7)), weight=1)
        self.NumberGeneration.rowconfigure(tuple(range(5)), weight=1)

        tk.Label(self.NumberGeneration, text="Choose a starting number:", bg="lightblue", font=("Arial", 14)).grid(row=0, columnspan=7, padx=10, pady=10)

        self.number_buttons = []
        self.generated_numbers = generate_valid_numbers(count=5) #generate the numbers

        positions = [(1,1),(1,3),(1,5),(2,2),(2,4)]
        #default_selected = False
        if not self.generated_numbers: #Should not happen 
             tk.Label(self.NumberGeneration, text="Error generating numbers!", fg="red").grid(row=1, column=1)
             return

        for i, num in enumerate(self.generated_numbers):
            btn = tk.Radiobutton(self.NumberGeneration, text=str(num), variable=self.chosenNumber, value=num,
                                 indicatoron=0, font=("Arial", 12), width=10, bg="white", selectcolor="lightgreen",
                                 command=lambda n=num: self.set_chosen_number(n))

            row, col = positions[i]
            btn.grid(row=row, column=col, padx=5, pady=10, sticky="ew")
            self.number_buttons.append(btn)
            #if not default_selected:
            #   btn.select()
            #  default_selected = True

        self.status_label_numgen = tk.Label(self.NumberGeneration, text="", bg="lightblue", font=("Arial", 10))
        self.status_label_numgen.grid(row=3, column=0, columnspan=5, padx=10, pady=5, sticky="sw")

        self.start_game_button = tk.Button(self.NumberGeneration, text="Start Game", state=tk.DISABLED,
                                           command=self.start_game, font=("Arial", 12))
        self.start_game_button.grid(row=3, column=5, columnspan=2, padx=10, pady=20, sticky="sew")

        tk.Button(self.NumberGeneration, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=4, column=5, columnspan=2, padx=10, pady=10, sticky="sew")

        #if default_selected:
        #    self.set_chosen_number(self.generated_numbers[0])
        #else: 
        #    self.set_chosen_number(0)


    #main game window
    def Create_Game(self):

        for widget in self.Game.winfo_children(): widget.destroy()
        self.Game.columnconfigure(0, weight=1)
        self.Game.rowconfigure(0, weight=1) 
        self.Game.rowconfigure(1, weight=1) 
        self.Game.rowconfigure(2, weight=2) 
        self.Game.rowconfigure(3, weight=1) 

        self.game_info_label = tk.Label(self.Game, text="", bg="lightblue", font=("Arial", 14), justify="left")
        self.game_info_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.turn_label = tk.Label(self.Game, text="", bg="lightblue", font=("Arial", 12, "bold"))
        self.turn_label.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.button_frame = tk.Frame(self.Game, bg="lightblue")
        self.button_frame.grid(row=2, column=0, pady=10)

        self.divide_by_2_button = tk.Button(self.button_frame, text="Divide by 2", font=("Arial", 12), width=12, command=lambda: self.make_move(2), state=tk.DISABLED)
        self.divide_by_3_button = tk.Button(self.button_frame, text="Divide by 3", font=("Arial", 12), width=12, command=lambda: self.make_move(3), state=tk.DISABLED)
        self.divide_by_2_button.pack(side=tk.LEFT, padx=10)
        self.divide_by_3_button.pack(side=tk.LEFT, padx=10)

        tk.Button(self.Game, text="Quit Game", command=lambda: self.show_frame(self.Menu)).grid(row=3, column=0, pady=20, sticky="s")


    def Create_Results(self, winner="Game Over", details=""):

        for widget in self.Results.winfo_children(): widget.destroy()
        self.Results.columnconfigure(0, weight=1)
        self.Results.rowconfigure((0,1,2), weight=1)

        tk.Label(self.Results, text=winner, bg="lightblue", font=("Arial", 20, "bold")).grid(row=0, column=0, padx=10, pady=20)
        tk.Label(self.Results, text=details, bg="lightblue", font=("Arial", 14), justify="center").grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.Results, text="Back to Menu", command=lambda: self.show_frame(self.Menu), font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=30)


    def start_game(self):
        
        #last check to start with smth available and possible
        if self.chosenNumber.get() <= 0:
             messagebox.showerror("Error", "Please select a starting number.")
             return
        if not self.algorithm_used:
            messagebox.showerror("Error", "Algorithm not set. Check settings.")
            return

        self.current_number = self.chosenNumber.get()
        self.human_score = 0
        self.computer_score = 0
        self.game_tree = {} #start with empty tree

        #Determine starting player and maximizing status for the root
        if self.UserStart.get() == 1:
            self.current_player = 'human'
            self.is_maximizing_player = False 
        else:
            self.current_player = 'computer'
            self.is_maximizing_player = True

        #preparation for function for dictionnary
        game_logic_funcs = {
            'is_terminal': self._is_terminal_state,
            'get_moves': self._get_valid_moves,
            'evaluate': self.evaluate_heuristic
        }

        print(f"Starting tree generation for {self.current_number} using {self.algorithm_used} (max depth: {self.max_depth})...")
        #Update label
        if hasattr(self, 'status_label_numgen') and self.status_label_numgen.winfo_exists():
             self.status_label_numgen.config(text=f"Generating tree ({self.algorithm_used})... Please wait.")
        self.landing.update_idletasks() #Force  to show message

        start_time = time.time()
        try:
            #game tree creation
            self.game_tree = generate_complete_tree(start_number=self.current_number, start_is_maximizing=self.is_maximizing_player, max_depth=self.max_depth, algorithm_choice=self.algorithm_used, game_logic_funcs=game_logic_funcs)

            end_time = time.time()
            generation_time = end_time - start_time

            #check if errors
            if self.game_tree is None: 
                 messagebox.showerror("Tree Error", f"Tree generation failed")
                 self.show_frame(self.Menu)
                 return

            print(f"Tree generation complete in {generation_time:.2f} seconds. Nodes: {len(self.game_tree)}")

            #starting node
            self.current_node_key = (self.current_number, self.is_maximizing_player)

            #verify root node exists
            if self.current_node_key not in self.game_tree:
                 messagebox.showerror("Tree Error", f"Root node {self.current_node_key} missing after generation!")
                 print("Tree keys sample:", list(self.game_tree.keys())[:10]) # Debug
                 self.show_frame(self.Menu)
                 return

            self.Create_Game() 
            self.show_frame(self.Game)
            self.update_game_state()

        except Exception as e:
            messagebox.showerror("Tree Generation Error", f"An error occurred: {e}")
            print(f"Error during tree generation call or setup: {e}")
            import traceback
            traceback.print_exc()
            self.show_frame(self.Menu) #cc menu


    def update_game_state(self):
        #funciton to update state
        if self._is_terminal_state(self.current_number):
            self.end_game()
            return

        # Check node key validity before proceeding
        if self.current_node_key is None:
             print("Error: Current node key is None in update_game_state")
             self.end_game("Error - Node Key Lost")
             return

        current_node_data = self.game_tree.get(self.current_node_key)
        if not current_node_data:
            print(f"FATAL ERROR: Node {self.current_node_key} not found in tree during gameplay!")
            self.end_game("Error - Tree Desync")
            return

        #update score
        self.game_info_label.config(text=f"Current Number: {self.current_number}\nYour Score: {self.human_score}\nComputer Score: {self.computer_score}")

        #gives available moves
        available_moves = current_node_data.get('children', {}).keys()

        if self.current_player == 'human':
            self.turn_label.config(text="Your Turn", fg="blue")
            self.divide_by_2_button.config(state=tk.NORMAL if 2 in available_moves else tk.DISABLED)
            self.divide_by_3_button.config(state=tk.NORMAL if 3 in available_moves else tk.DISABLED)

            if not available_moves: #no user moves
                 print(f"Info: Human has no moves from node {self.current_node_key} (tree). Ending.")
                 self.end_game()

        elif self.current_player == 'computer':
            self.turn_label.config(text="Computer's Turn...", fg="red")
            self.divide_by_2_button.config(state=tk.DISABLED)
            self.divide_by_3_button.config(state=tk.DISABLED)

            if not available_moves: #no computer moves
                 print(f"Info: Computer has no moves from node {self.current_node_key} (tree). Ending.")
                 self.end_game()
            else:
                 self.landing.after(100, self.computer_turn) 

        else:
             self.turn_label.config(text="Game Over", fg="grey")
             self.divide_by_2_button.config(state=tk.DISABLED)
             self.divide_by_3_button.config(state=tk.DISABLED)


    def make_move(self, divisor):

        #make move for game and update ui
        if self._is_terminal_state(self.current_number):
            print("Warning: make_move called on a terminal state.")
            return
        if self.current_node_key is None:
             print("Error: make_move called with None node key.")
             self.end_game("Error - Node Key Lost")
             return

        current_node_data = self.game_tree.get(self.current_node_key)
        if not current_node_data:
             print(f"Error: Node {self.current_node_key} missing during make_move!")
             self.end_game("Error - Tree Desync")
             return

        possible_children = current_node_data.get('children', {})
        if divisor not in possible_children:
             print(f"Error: Invalid move {divisor} attempted from node {self.current_node_key}. Allowed: {list(possible_children.keys())}")
             return

        #Score change
        if self.current_player == 'human':
            if divisor == 2: self.computer_score += 2
            elif divisor == 3: self.human_score += 3
        else: 
            if divisor == 2: self.human_score += 2
            elif divisor == 3: self.computer_score += 3

        self.current_number //= divisor
        if self.current_player == 'human':
            next_player= 'computer' 
        else:
            next_player= 'human'
        next_is_maximizing = not self.is_maximizing_player 

        #update current node
        self.current_node_key = possible_children[divisor]

        #Update state for current player
        self.current_player = next_player
        self.is_maximizing_player = next_is_maximizing

        self.update_game_state()


    #Chooses best move for computer (AI) and closes the game if necessary
    def computer_turn(self):
        if self.current_player != 'computer': return
        if self.current_node_key is None:
             print("Error: computer_turn called with None node key.")
             self.end_game("Error - Node Key Lost")
             return

        current_node_data = self.game_tree.get(self.current_node_key)
        if not current_node_data:
            print(f"Error: Node {self.current_node_key} missing during computer turn!")
            self.end_game("Error")
            return

        best_move = current_node_data.get('best_move')
        available_moves = list(current_node_data.get('children', {}).keys())

        #choose best moves
        if best_move is None or best_move not in available_moves:
            if available_moves:
                if best_move is not None:
                     print(f"Error: Stored best_move {best_move} invalid for node {self.current_node_key}. Children: {available_moves}. Falling back.")
                else: 
                     print(f"Warning: No 'best_move' for node {self.current_node_key}, choosing first: {available_moves[0]}")
                best_move = available_moves[0] # Fallback
            else:
                #No more possibiliteies: game must end
                print(f"Info: Computer has no moves from node {self.current_node_key} (no children). Should be terminal.")

                if not self._is_terminal_state(self.current_number):
                     print(f"Warning: Node {self.current_node_key} has no moves but isn't terminal by number ({self.current_number})!")
                self.end_game()
                return

        print(f"Computer using move from tree: {best_move}")
        self.make_move(best_move)


    #handling end game
    def end_game(self, status="Normal"):
        
        print(f"Game Over! Status: {status}")
        self.current_player = None #stop main loop
        self.is_maximizing_player = None

        #disalbel buttons
        try: 
            if hasattr(self, 'divide_by_2_button') and self.divide_by_2_button.winfo_exists():
                self.divide_by_2_button.config(state=tk.DISABLED)
            if hasattr(self, 'divide_by_3_button') and self.divide_by_3_button.winfo_exists():
                self.divide_by_3_button.config(state=tk.DISABLED)
        except tk.TclError: pass

        # Determine Winner
        if "Error" in status:
            winner = "Game ended due to error"
            details = f"Status: {status}\nFinal Number: {self.current_number}"
        else: 
            if self.human_score > self.computer_score: winner = "User Win!"
            elif self.computer_score > self.human_score: winner = "Computer Wins!"
            else: winner = "It's a Tie!"
            details = f"Final Number: {self.current_number}\nYour Score: {self.human_score}\nComputer Score: {self.computer_score}"

        self.Create_Results(winner, details)
        self.show_frame(self.Results)


    def reset_game_settings(self):

        #reset settings
        self.chosenNumber.set(0)
        self.current_number = 0
        self.human_score = 0
        self.computer_score = 0
        self.current_player = None
        self.is_maximizing_player = None
        self.game_tree = {}
        self.current_node_key = None
        #clear the NumberGeneration frame's widgets before recreating
        for widget in self.NumberGeneration.winfo_children():
            widget.destroy()

#launch game
if __name__ == "__main__":
    landing_window = tk.Tk()
    app = Main(landing_window)
    landing_window.mainloop()