from tkinter import *
import random
import math
from tkinter import messagebox

root = Tk()
root.title = "Ping Pong Game"
root.resizable(0,0)

canvas = Canvas(root, width="700", height="500",bd=1, highlightthickness=1)
canvas.config(bg="Black")
canvas.pack()

text = canvas.create_text(350,30,font=("Times New Roman",30,"bold"), text=":",fill="White")
canvas.create_line(350,0,350,700,fill="White")

root.update()


#initializing the class ball
class Ball:
    def __init__(self, canvas, paddle1, paddle2, color):

        #creating the ball in the center
        self.id = canvas.create_oval(10,10,100,100,fill=color)
        self.canvas.move(self.id,350,250)

        #Ball velocity, randomized
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[1]
        self.y = starts[3]

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)


class Paddle1:
    pos = [0,0,0,0]
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,150,10,250,fill=color)
        self.y = 0


class Paddle2:
    pos = [0,0,0,0]
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,150,690,250,fill=color)
        self.y = 0


root.mainloop()