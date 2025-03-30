#Use this file as main work of the game (including UI)
import tkinter as tk
from functions import *


class Main:
    def __init__(self, landing):
        self.landing = landing
        self.landing.title("Practical Assignment 1 - ENG_33_O365G")
        self.landing.geometry("600x400")

        # Create the frames
        self.Menu = tk.Frame(landing, bg="lightblue")
        self.Rules = tk.Frame(landing, bg="lightblue")
        self.Settings = tk.Frame(landing, bg="lightblue")
        self.About = tk.Frame(landing, bg="lightblue")
        self.NumberGeneration = tk.Frame(landing, bg="lightblue")
        self.Game = tk.Frame(landing)

        self.AlphaBetaAlgorithm = tk.IntVar()
        self.MinMaxAlgorithm = tk.IntVar()

        self.chosenNumber = tk.IntVar()

        self.Create_Menu()
        self.Create_Rules()
        self.Create_Settings()
        self.Create_About()
        self.Create_NumberGeneration()
        self.Create_Game()

        self.show_frame(self.Menu)

    def Create_Menu(self):

        self.Menu.columnconfigure((0,1,2), weight=1)
        self.Menu.rowconfigure((0,1,2,3), weight=1)

        tk.Label(self.Menu, text="Welcome to our Assignment", bg="lightblue", font=("Arial", 16)).grid(row=0,columnspan=3, padx=10, pady=10, sticky="w")

        tk.Button(self.Menu, text="See Rules", command=lambda: self.show_frame(self.Rules), font=("Arial", 12)).grid(row=1, columnspan=2,column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Menu, text="About", command=lambda: self.show_frame(self.About), font=("Arial", 12)).grid(row=2, columnspan=2,column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Menu, text="Start Game", command=lambda: [self.NumberGeneration.grid_forget(), self.Create_NumberGeneration(), self.show_frame(self.NumberGeneration)], font=("Arial", 12)).grid(row=3, columnspan=2,column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Menu, text="Settings", command=lambda: self.show_frame(self.Settings), font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=10, sticky="ne")

        #print(self.landing.grid_size())

    def Create_Rules(self):

        self.Rules.columnconfigure((0,1), weight=1)
        self.Rules.rowconfigure((0,1,2), weight=1)

        tk.Label(self.Rules, text="Rules given to us", bg="lightblue", font=("Arial", 14)).grid(row=0, padx=10, pady=10, sticky="w")

        tk.Label(self.Rules, text="At the beginning of the game, the game software randomly generates 5 numbers between 10000 and 20000, "
                                          "but initially divisible by both 3 and 2. The human player chooses which of the generated numbers "
                                          "he wants to start the game with. \n \n"
                                          "At the beginning of the game, the number chosen by the human player"
                                          "is given. Both players have 0 points. The players take turns, each turn dividing the current number "
                                          "by 2 or 3. If division by 2 is made, then 2 points are added to the opponent's score. If division by 3 "
                                          "is made, 3 points are added to the player's score. The game ends as soon as a number less than or equal "
                                          "to 10 has been acquired. Otherwise, the player with the highest number of points wins.",bg="lightblue",
                           wraplength=500,font=("Arial", 12), justify="left").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        #print(self.landing.grid_size())

        tk.Button(self.Rules, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=2, column=1, padx=10, pady=10, sticky="se")

    def Create_About(self):

        self.About.columnconfigure((0,1), weight=1)
        self.About.rowconfigure((0,1,2,3,4,5,6), weight=1)

        tk.Label(self.About, text="Team Members", bg="lightblue", font=("Arial", 12)).grid(row=0, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Enzo Höhenberger", bg="lightblue", font=("Arial", 12)).grid(row=1, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Ahmed Dabbagh", bg="lightblue", font=("Arial", 12)).grid(row=2, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Andrii Nazarkevych", bg="lightblue", font=("Arial", 12)).grid(row=3, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Ijin Kunnel Thankachan", bg="lightblue", font=("Arial", 12)).grid(row=4, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Welathantrige Dawini Hasulu Boteju", bg="lightblue", font=("Arial", 12)).grid(row=5, padx=10, pady=10, sticky="w")

        tk.Button(self.About, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=6, column=1, padx=10, pady=10, sticky="se")

    def Change_Check_Value(self):
        if self.AlphaBetaAlgorithm.get() == 1 and self.MinMaxAlgorithm.get() == 1:
            self.warning_label.config(text="Only one can be chosen", fg="red")
        elif self.AlphaBetaAlgorithm.get() == 0 and self.MinMaxAlgorithm.get() == 0:
            self.warning_label.config(text="Select AT LEAST one", fg="red")
        else:
            self.warning_label.config(text="")

    def Create_Settings(self):

        self.Settings.columnconfigure((0,1,2), weight=1)
        self.Settings.rowconfigure((0,1,2,3,4,5), weight=1)

        tk.Label(self.Settings, text="Settings", bg="lightblue", font=("Arial", 14)).grid(row=0, padx=10, pady=10, sticky="w")
        tk.Label(self.Settings, text="Choose which Algorithm is used", fg="green", bg="lightblue", font=("Arial", 14)).grid(row=1, padx=10, pady=10, sticky="w")

        tk.Checkbutton(self.Settings, text="Manimax Algorithm", variable=self.AlphaBetaAlgorithm, onvalue=1, offvalue=0, font=("Arial", 12), command=self.Change_Check_Value).grid(row=2, padx=10, pady=10, sticky="news")
        tk.Checkbutton(self.Settings, text="Alpha Beta Algorithm", variable=self.MinMaxAlgorithm, onvalue=1, offvalue=0, font=("Arial", 12), command=self.Change_Check_Value).grid(row=3, padx=10, pady=10, sticky="news")

        self.warning_label = tk.Label(self.Settings, text="", fg="red", bg="lightblue", font=("Arial", 14))
        self.warning_label.grid(row=4, padx=10, pady=10, sticky="w")

        tk.Button(self.Settings, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=5, column=2, padx=10, pady=10, sticky="se")

    def set_chosen_number(self,num):
        self.chosenNumber.set(num)

    def Create_NumberGeneration(self):
        self.NumberGeneration.columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.NumberGeneration.rowconfigure((0,1,2,3,4), weight=3)
        self.NumberGeneration.rowconfigure((6,7), weight=1)
        tk.Label(self.NumberGeneration, text="Choose a starting number between the following:", bg="lightblue", font=("Arial", 12)).grid(row=0, columnspan=6, column=0, padx=10, pady=10)
        self.number_buttons = []
        self.generated_numbers = generation_numbers()

        for i, num in enumerate(self.generated_numbers):
            btn = tk.Button(self.NumberGeneration, text=str(num), font=("Arial", 12), command=lambda num=num: self.set_chosen_number(num))
            self.rowsettings = [1,1,1,3,3]
            self.columnsettings = [1,3,5,2,4]
            btn.grid(row=self.rowsettings[i] + 1, column=self.columnsettings[i] + 1, padx=5, pady=5, sticky="news")
            self.number_buttons.append(btn)

        tk.Button(self.NumberGeneration, text="Start Game", command=lambda: [self.Game.grid_forget(), self.Create_Game(), self.show_frame(self.Game)]).grid(row=6, column=7, padx=10, pady=10, sticky="sew")
        tk.Button(self.NumberGeneration, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=7, column=7, padx=10, pady=10, sticky="sew")
        print(self.chosenNumber)


    def Create_Game(self):

        tk.Label(self.Game, text=f"Chosen Number is: {self.chosenNumber.get()}", bg="lightblue", font=("Arial", 12)).grid(row=0, columnspan=6, column=2, padx=10, pady=10)
        
        self.number_buttons = []


    def show_frame(self, frame):
        for f in [self.Menu, self.Rules, self.Settings, self.About, self.NumberGeneration, self.Game]:
            f.grid_forget()
        frame.grid(row=0, column=0, sticky="nsew")
        self.landing.rowconfigure(0, weight=1)
        self.landing.columnconfigure(0, weight=1)
        #print(self.landing.grid_size())  # Shows (columns, rows) count


landing = tk.Tk()
app = Main(landing)
landing.mainloop()