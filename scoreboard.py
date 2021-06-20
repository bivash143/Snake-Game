from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Your Score: {self.score}", align=ALIGN, font=FONT)


    def increaseScore(self):
        self.score += 1
        self.clear()
        self.write(f"Your Score: {self.score}", align=ALIGN, font=FONT)


    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

