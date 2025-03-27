import tkinter as tk

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
        self.NumberGeneration = tk.Frame(landing)
        self.Game = tk.Frame(landing)

        self.check1 = tk.IntVar()
        self.check2 = tk.IntVar()

        self.Create_Menu()
        self.Create_Rules()
        self.Create_Settings()
        self.Create_About()
        #self.Create_NumberGeneration()
        #self.Create_Game()

        self.show_frame(self.Menu)

    def Create_Menu(self):

        self.Menu.columnconfigure((0,1,2), weight=1)
        self.Menu.rowconfigure((0,1,2,3), weight=1)

        tk.Label(self.Menu, text="Welcome to our Assignment", bg="lightblue", font=("Arial", 12)).grid(row=0,columnspan=3, padx=10, pady=10, sticky="w")

        tk.Button(self.Menu, text="See Rules", command=lambda: self.show_frame(self.Rules), font=("Arial", 12)).grid(row=1, columnspan=2,column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Menu, text="About", command=lambda: self.show_frame(self.About), font=("Arial", 12)).grid(row=2, columnspan=2,column=0, padx=10, pady=10, sticky="nsew")
        tk.Button(self.Menu, text="Start Game", command=lambda: self.show_frame(self.Game), font=("Arial", 12)).grid(row=3, columnspan=2,column=0, padx=10, pady=10, sticky="nsew")

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
        self.About.rowconfigure((0,1,2,3,4,5), weight=1)

        tk.Label(self.About, text="Team Members", bg="lightblue", font=("Arial", 12)).grid(row=0, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Enzo Höhenberger", bg="lightblue", font=("Arial", 12)).grid(row=1, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Ahmed Dabbagh", bg="lightblue", font=("Arial", 12)).grid(row=2, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Andrii Nazarkevych", bg="lightblue", font=("Arial", 12)).grid(row=3, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Ijin Kunnel Thankachan", bg="lightblue", font=("Arial", 12)).grid(row=4, padx=10, pady=10, sticky="w")
        tk.Label(self.About, text="Welathantrige Dawini Hasulu Boteju", bg="lightblue", font=("Arial", 12)).grid(row=5, padx=10, pady=10, sticky="w")

        tk.Button(self.About, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=5, column=1, padx=10, pady=10, sticky="se")

    def Change_Check_Value(self):
        if self.check1.get() == 1 and self.check2.get() == 1:
            self.warning_label.config(text="Only one can be chosen", fg="red")
        elif self.check1.get() == 0 and self.check2.get() == 0:
            self.warning_label.config(text="Select AT LEAST one", fg="red")
        else:
            self.warning_label.config(text="")

    def Create_Settings(self):

        self.Settings.columnconfigure((0,1,2), weight=1)
        self.Settings.rowconfigure((0,1,2,3,4,5), weight=1)

        tk.Label(self.Settings, text="Settings", bg="lightblue", font=("Arial", 14)).grid(row=0, padx=10, pady=10, sticky="w")
        tk.Label(self.Settings, text="Choose which Algorithm is used", fg="green", bg="lightblue", font=("Arial", 14)).grid(row=1, padx=10, pady=10, sticky="w")

        tk.Checkbutton(self.Settings, text="Algorithm 1", variable=self.check1, onvalue=1, offvalue=0, font=("Arial", 12), command=self.Change_Check_Value).grid(row=2, padx=10, pady=10, sticky="news")
        tk.Checkbutton(self.Settings, text="Algorithm 2", variable=self.check2, onvalue=1, offvalue=0, font=("Arial", 12), command=self.Change_Check_Value).grid(row=3, padx=10, pady=10, sticky="news")

        self.warning_label = tk.Label(self.Settings, text="", fg="red", bg="lightblue", font=("Arial", 14))
        self.warning_label.grid(row=4, padx=10, pady=10, sticky="w")

        tk.Button(self.Settings, text="Go Back", command=lambda: self.show_frame(self.Menu)).grid(row=5, column=2, padx=10, pady=10, sticky="se")



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