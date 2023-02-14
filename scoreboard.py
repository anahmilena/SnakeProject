from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(-40, 275)
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.get_score()
        self.hideturtle()
        self.update_scoreboard()

    def get_score(self):
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

    def store_score(self):
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def refresh(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_score()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",
                   font=("Courier", 15, "normal"), align="center")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", font=("Courier", 15, "normal"), align="center")
