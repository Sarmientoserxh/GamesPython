import turtle
import time
import random

posTime = 0.1  # milesima de segundo; para que no se ejecute tan rapido;

# marcador
score = 0
high_Score = 0

window = turtle.Screen()
window.title("SnakeGame")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)

# Textos del marcador;
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0      High Score: 0", align="center", font=("Courier", 23, "normal"))

# head of snake;
headSnake = turtle.Turtle()
headSnake.speed(0)
headSnake.shape("square")
headSnake.color("green")
headSnake.penup()  # comando para que quitemos el rastro;
headSnake.goto(0, 0)

# food of the snake
foodSnake = turtle.Turtle()
foodSnake.speed(0)
foodSnake.shape("circle")
foodSnake.color("red")
foodSnake.penup()  # comando para que quitemos el rastro;
foodSnake.goto(0, 100)

# cuerpo de la serpiente;
bodySnake = []

# dirección inicial de la serpiente;
headSnake.direction = "stop"

# funciones de los movimientos;
def upSnake():
    if headSnake.direction != "down":  # Evitar moverse en la dirección opuesta
        headSnake.direction = "up"

def downSnake():
    if headSnake.direction != "up":
        headSnake.direction = "down"

def leftSnake():
    if headSnake.direction != "right":
        headSnake.direction = "left"

def rightSnake():
    if headSnake.direction != "left":
        headSnake.direction = "right"

def mov():
    if headSnake.direction == "up":
        y = headSnake.ycor()
        headSnake.sety(y + 20)
    elif headSnake.direction == "down":
        y = headSnake.ycor()
        headSnake.sety(y - 20)
    elif headSnake.direction == "left":
        x = headSnake.xcor()
        headSnake.setx(x - 20)
    elif headSnake.direction == "right":
        x = headSnake.xcor()
        headSnake.setx(x + 20)

def reset_game():
    global score
    time.sleep(1)
    headSnake.goto(0, 0)
    headSnake.direction = "stop"
    
    for segment in bodySnake:
        segment.goto(3000, 3000)
    bodySnake.clear()
    
    score = 0
    update_score()

def update_score():
    texto.clear()
    texto.write("Score: {}     High Score: {}".format(score, high_Score), align="center", font=("Courier", 23, "normal"))

# conectar con el teclado.
window.listen()
window.onkeypress(upSnake, "Up")
window.onkeypress(downSnake, "Down")
window.onkeypress(leftSnake, "Left")
window.onkeypress(rightSnake, "Right")

while True:
    window.update()

    if (headSnake.xcor() > 290 or headSnake.xcor() < -290 or headSnake.ycor() > 290 or headSnake.ycor() < -290):
        reset_game()

    if headSnake.distance(foodSnake) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        foodSnake.goto(x, y)

        newBodySnake = turtle.Turtle()
        newBodySnake.speed(0)
        newBodySnake.shape("square")
        newBodySnake.color("#008F39")
        newBodySnake.penup()  # comando para que quitemos el rastro;
        bodySnake.append(newBodySnake)

        # Aumentar el marcador;
        score += 10

        if score > high_Score:
            high_Score = score

        update_score()

    # mover el cuerpo de la serpiente animaciones;
    totalBodySnake = len(bodySnake)
    for index in range(totalBodySnake - 1, 0, -1):
        x = bodySnake[index - 1].xcor()
        y = bodySnake[index - 1].ycor()
        bodySnake[index].goto(x, y)

    if totalBodySnake > 0:
        x = headSnake.xcor()
        y = headSnake.ycor()
        bodySnake[0].goto(x, y)

    mov()
    
    for segmento in bodySnake:
        if segmento.distance(headSnake) < 20:
            reset_game()
    
    time.sleep(posTime)
