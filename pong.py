from tkinter import *
import random
import math
from tkinter import messagebox

root = Tk()
root.title = "Ping Pong Game"
root.resizable(0,0)
root.wm_attributes("-topmost",1)

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
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.canvas = canvas

        #Ball velocity, randomized
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[1]
        self.y = starts[3]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.score1 = 0
        self.score2 = 0

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 4

        if pos[3] >= self.canvas_height:
            self.y = -4

        if pos[0] <= 0:
            self.x = 4
            self.score1 += 1
            print(self.score1)

            canvas.itemconfigure(l,text=str(self.score1) + ":" + str(self.score2))

        if pos[2] >= self.canvas_width:
            self.x = -4
            self.score2 += 1
            print(self.score2)

            canvas.itemconfigure(l,text=str(self.score1) + ":" + str(self.score2))

        if self.hit_paddle1(pos) == True:
            self.x = 4

        if self.hit_paddle2(pos) == True:
            self.x = -4

    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False
        
    def hit_paddle2(self, pos):
        paddle_pos = self.canvas.coords(self.paddle2.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False

        


class Paddle1:
    pos = [0,0,0,0]
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,150,25,250,fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height
        self.canvas_width = self.canvas.winfo_width

        #bind keys (key events)
        self.canvas.bind_all("a",self.turn_up)
        self.canvas.bind_all("d",self.turn_down)
        #'a' = move up
        #'d' = move down

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.y = 0
        
        if pos[3] >= self.canvas_height:
            self.y = 0
    
    def turn_up(self,event):
        self.y = -4

    def turn_down(self, event):
        self.y = 4


class Paddle2:
    pos = [0,0,0,0]
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(675,150,690,250,fill=color)
        self.y = 0


root.mainloop()
