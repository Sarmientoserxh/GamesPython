import turtle
import time
from tkinter import messagebox
import random

class PingPong:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("PingPong")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        # Jugador 1
        self.playerA = turtle.Turtle()
        self.playerA.speed(0)
        self.playerA.shape("square")
        self.playerA.color("white")
        self.playerA.penup()
        self.playerA.goto(-350, 0)
        self.playerA.shapesize(stretch_wid=5, stretch_len=1)

        # Jugador 2 (Máquina)
        self.playerB = turtle.Turtle()
        self.playerB.speed(0)
        self.playerB.shape("square")
        self.playerB.color("white")
        self.playerB.penup()
        self.playerB.goto(350, 0)
        self.playerB.shapesize(stretch_wid=5, stretch_len=1)

        # Pelota
        self.ballGame = turtle.Turtle()
        self.ballGame.speed(1)
        self.ballGame.shape("square")
        self.ballGame.color("white")
        self.ballGame.penup()
        self.ballGame.goto(0, 0)
        self.ballGame.dx = 2  # Ajusta la velocidad de la pelota
        self.ballGame.dy = 2  # Ajusta la velocidad de la pelota

        # Línea de división
        self.lineDivision = turtle.Turtle()
        self.lineDivision.color("white")
        self.lineDivision.penup()
        self.lineDivision.goto(0, 300)
        self.lineDivision.pendown()
        self.lineDivision.goto(0, -300)

        # Marcador
        self.puntoA = 0
        self.puntoB = 0

        self.marker = turtle.Turtle()
        self.marker.speed(0)
        self.marker.color("white")
        self.marker.penup()
        self.marker.hideturtle()
        self.marker.goto(0, 260)
        self.marker.write("PlayerA: 0         PlayerB: 0", align="center", font=("Courier", 24, "normal"))

        # Controles
        self.window.listen()
        self.window.onkeypress(self.playerA_up, "Up")
        self.window.onkeypress(self.playerA_down, "Down")

    def playerA_up(self):
        y = self.playerA.ycor()
        if y < 250:  # Limita el movimiento hacia arriba
            y += 20
        self.playerA.sety(y)

    def playerA_down(self):
        y = self.playerA.ycor()
        if y > -240:  # Limita el movimiento hacia abajo
            y -= 20
        self.playerA.sety(y)

    def mainLoop(self):
        while True:
            self.window.update()
            time.sleep(0.01)  # Ajusta el valor para cambiar la velocidad del juego
            
            # Movimiento de la pelota
            self.ballGame.setx(self.ballGame.xcor() + self.ballGame.dx)
            self.ballGame.sety(self.ballGame.ycor() + self.ballGame.dy)

            # Rebotar en las paredes
            if self.ballGame.ycor() > 290 or self.ballGame.ycor() < -290:
                self.ballGame.dy *= -1

            # Rebotar en las paletas
            if self.ballGame.xcor() > 340 and self.ballGame.xcor() < 350 and self.playerB.ycor() - 50 < self.ballGame.ycor() < self.playerB.ycor() + 50:
                self.ballGame.dx *= -1
            if self.ballGame.xcor() < -340 and self.ballGame.xcor() > -350 and self.playerA.ycor() - 50 < self.ballGame.ycor() < self.playerA.ycor() + 50:
                self.ballGame.dx *= -1

            # Movimiento de la máquina
            if self.ballGame.dx > 0:
                if self.ballGame.ycor() > self.playerB.ycor() and self.playerB.ycor() < 250:
                    self.playerB.sety(self.playerB.ycor() + 2)
                elif self.ballGame.ycor() < self.playerB.ycor() and self.playerB.ycor() > -240:
                    self.playerB.sety(self.playerB.ycor() - 2)

            # Puntos y reiniciar pelota
            if self.ballGame.xcor() < -390:
                self.ballGame.goto(0, 0)
                self.ballGame.dx *= -1
                self.puntoB += 1
                self.marker.clear()
                self.marker.write(f"PlayerA: {self.puntoA}         PlayerB: {self.puntoB}", align="center", font=("Courier", 24, "normal"))
                if self.puntoB == 10:
                    messagebox.showinfo("Juego Terminado", "Perdiste :(")
                    break

            if self.ballGame.xcor() > 390:
                self.ballGame.goto(0, 0)
                self.ballGame.dx *= -1
                self.puntoA += 1
                self.marker.clear()
                self.marker.write(f"PlayerA: {self.puntoA}         PlayerB: {self.puntoB}", align="center", font=("Courier", 24, "normal"))
                if self.puntoA == 10:
                    messagebox.showinfo("Juego Terminado", "¡Ganaste!")
                    break

if __name__ == "__main__":
    ping = PingPong()
    ping.mainLoop()
