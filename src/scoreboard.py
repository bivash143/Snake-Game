from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./src/data.txt") as ft:
            self.highScore = int(ft.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score: {self.score} High Score: {self.highScore}", align=ALIGN, font=FONT)


    def increaseScore(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("src/data.txt","w")as ft:
                ft.write(str(self.highScore))
        self.score = 0
        self.update_scoreboard()
