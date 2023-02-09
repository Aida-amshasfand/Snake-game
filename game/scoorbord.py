from turtle import Turtle


class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        with open("scores.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scores.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()
