from turtle import Turtle
import pandas


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        """ Keeps track of score, topscore and lives left. """
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 5
        self.top_score = 0
        self.data = None
        self.fetch_topscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        """ Scoreboard updates with score, lives left and the topscore. """
        self.clear()
        self.goto(0, 255)
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 35, "normal"))
        self.goto(-380, 255)
        lives_left = self.lives * "🫀 "
        self.write(f"{lives_left}", align="left", font=("Courier", 25, "normal"))
        self.goto(380, 255)
        self.write(f"Topscore: {self.top_score}", align="right", font=("Courier", 15, "normal"))

    def point(self, p):
        """ Points are added to the score, according to the input. Scoreboard is updated. """
        self.score += p
        self.update_scoreboard()

    def lost_live(self):
        """ Players total lives are decreased by one. Scoreboard is updated. """
        self.lives -= 1
        self.update_scoreboard()

    def fetch_topscore(self):
        """ Gets the topscore from the .csv file.
        If there is no .csv file available, a .csv file is created with a topscore value 0.
         Scoreboard is updated with the topscore value. """
        try:
            self.data = pandas.read_csv("topscore.csv")
        except FileNotFoundError:
            self.data = pandas.DataFrame({"Topscore": [0]})
            self.data.to_csv("topscore.csv", index=False)
        self.top_score = self.data["Topscore"][0]
        # Update the topscore in GUI
        self.update_scoreboard()

    def save_new_topscore(self, top):
        """ Updates the topscore in the .csv file and in the game (scoreboard) with the given input. """
        self.top_score = top
        self.data["Topscore"] = top
        self.data.to_csv("topscore.csv", index=False)
        self.update_scoreboard()

    def game_over(self):
        """ Write game over. """
        self.goto(0, 180)
        self.write(f"GAME OVER", move=False, align="center", font=("Courier", 70, "normal"))

    def winner(self):
        """ Writes Winner and the score. """
        self.goto(0, 0)
        self.write(f"Winner!\nScore: {self.score}", move=False, align="center", font=("Courier", 70, "normal"))

    def clear_score(self):
        """ Clears the score and updates scoreboard. """
        self.score = 0
        self.update_scoreboard()
