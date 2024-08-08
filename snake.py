import turtle
import time
import random

class SnakeGame:
    def __init__(self):
        self.posTime = 0.1  # milisegundos
        self.score = 0
        self.high_score = 0

        self.window = turtle.Screen()
        self.window.title("SnakeGame")
        self.window.bgcolor("black")
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

        self.texto = turtle.Turtle()
        self.texto.speed(0)
        self.texto.color("white")
        self.texto.penup()
        self.texto.hideturtle()
        self.texto.goto(0, 260)
        self.texto.write("Score: 0      High Score: 0", align="center", font=("Courier", 23, "normal"))

        self.head_snake = turtle.Turtle()
        self.head_snake.speed(0)
        self.head_snake.shape("square")
        self.head_snake.color("green")
        self.head_snake.penup()
        self.head_snake.goto(0, 0)
        self.head_snake.direction = "stop"

        self.food_snake = turtle.Turtle()
        self.food_snake.speed(0)
        self.food_snake.shape("circle")
        self.food_snake.color("red")
        self.food_snake.penup()
        self.food_snake.goto(0, 100)

        self.body_snake = []

        self.window.listen()
        self.window.onkeypress(self.up_snake, "Up")
        self.window.onkeypress(self.down_snake, "Down")
        self.window.onkeypress(self.left_snake, "Left")
        self.window.onkeypress(self.right_snake, "Right")

    def up_snake(self):
        if self.head_snake.direction != "down":
            self.head_snake.direction = "up"

    def down_snake(self):
        if self.head_snake.direction != "up":
            self.head_snake.direction = "down"

    def left_snake(self):
        if self.head_snake.direction != "right":
            self.head_snake.direction = "left"

    def right_snake(self):
        if self.head_snake.direction != "left":
            self.head_snake.direction = "right"

    def move(self):
        if self.head_snake.direction == "up":
            y = self.head_snake.ycor()
            self.head_snake.sety(y + 20)
        elif self.head_snake.direction == "down":
            y = self.head_snake.ycor()
            self.head_snake.sety(y - 20)
        elif self.head_snake.direction == "left":
            x = self.head_snake.xcor()
            self.head_snake.setx(x - 20)
        elif self.head_snake.direction == "right":
            x = self.head_snake.xcor()
            self.head_snake.setx(x + 20)

    def reset_game(self):
        self.score = 0
        self.head_snake.goto(0, 0)
        self.head_snake.direction = "stop"

        for segment in self.body_snake:
            segment.goto(3000, 3000)
        self.body_snake.clear()
        self.update_score()

    def update_score(self):
        self.texto.clear()
        self.texto.write("Score: {}     High Score: {}".format(self.score, self.high_score), align="center", font=("Courier", 23, "normal"))

    def main_loop(self):
        while True:
            self.window.update()

            if (self.head_snake.xcor() > 290 or self.head_snake.xcor() < -290 or 
                self.head_snake.ycor() > 290 or self.head_snake.ycor() < -290):
                self.reset_game()

            if self.head_snake.distance(self.food_snake) < 20:
                x = random.randint(-280, 280)
                y = random.randint(-280, 280)
                self.food_snake.goto(x, y)

                new_body_snake = turtle.Turtle()
                new_body_snake.speed(0)
                new_body_snake.shape("square")
                new_body_snake.color("#008F39")
                new_body_snake.penup()
                self.body_snake.append(new_body_snake)

                self.score += 10

                if self.score > self.high_score:
                    self.high_score = self.score

                self.update_score()

            total_body_snake = len(self.body_snake)
            for index in range(total_body_snake - 1, 0, -1):
                x = self.body_snake[index - 1].xcor()
                y = self.body_snake[index - 1].ycor()
                self.body_snake[index].goto(x, y)

            if total_body_snake > 0:
                x = self.head_snake.xcor()
                y = self.head_snake.ycor()
                self.body_snake[0].goto(x, y)

            self.move()

            for segmento in self.body_snake:
                if segmento.distance(self.head_snake) < 20:
                    self.reset_game()

            time.sleep(self.posTime)

if __name__ == "__main__":
    game = SnakeGame()
    game.main_loop()
