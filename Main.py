import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ProyectGame AlgebraLineal")
        self.geometry("600x400")

        # Cargar la imagen de fondo
        self.bg_image = tk.PhotoImage(file="C:/Users/Serxch/OneDrive/Documentos/calculoMath/Juegos/Juego_Snake/GamesPython/images/fondo2.png")

        # Crear un Canvas y colocar la imagen de fondo
        self.canvas = tk.Canvas(self, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.create_widgets()

    def create_widgets(self):
        # Colocar los widgets en el Canvas
        self.canvas.create_text(300, 50, text="GameProyect", font=("Helvetica", 32), fill="#FFD23F")
        self.canvas.create_text(300, 100, text="por: Samantha Bello, Sergio Sarmiento", font=("Helvetica", 18), fill="#FFD23F")
        self.canvas.create_text(300, 150, text="Versión 1.0", font=("Helvetica", 18), fill="#FFD23F")

        menubar = tk.Menu(self)
        self.config(menu=menubar)

        option_Game = tk.Menu(menubar, tearoff=0)
        option_Game.add_command(label="Tetris Game", command=self.open_tetris)
        option_Game.add_command(label="Snake Game", command=self.open_snake)
        option_Game.add_command(label="Ping Pong Game", command=self.open_pingPong)

        menubar.add_cascade(label="Selecciona tu Juego de matrices", menu=option_Game)

    def open_tetris(self):
        self.run_script("Tetris.py")

    def open_snake(self):
        self.run_script("Snake.py")
        
    def open_pingPong(self):
        self.run_script("Ping_Pong.py")

    def run_script(self, script_name):
        if os.path.isfile(script_name):
            subprocess.run(["python", script_name], check=True)
        else:
            messagebox.showerror("Error", f"No se encontró el archivo {script_name}")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
