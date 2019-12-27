from tkinter import *
import tkinter as tk
import keyboard
import player
import ball


class Game:
    def __init__(self):
        self.n = 1
        self.m = 1
        self.root = Tk()
        self.width = 510
        self.height = 300
        self.root.geometry(str(self.width) + "x" + str(self.height))
        self.root.bind("<Key>", self.key)
        self.canvas = Canvas(self.root)
        self.player1 = player.Player("Avdush", self.root, self.canvas, 0)
        self.player2 = player.Player("Avdushi", self.root, self.canvas, 500)

    
        self.player1Points = tk.Label(self.root, text = self.player1.points)
        self.player2Points = tk.Label(self.root, text = self.player2.points)
        ##ll.place(x=0, y=250, anchor='sw')
        ##lr.place(x=1000, y=250, anchor='se')
    
        self.b = ball.Ball(self.canvas, self.width/2, self.height/2)

    def movBall(self):
       
        if self.b.positionX > (self.b.x * 2):
            self.b.changeBallPosition(-self.b.x, 0) 
            self.player1.points += 1
            self.player1Points.config(text=self.player1.points)
        if self.b.positionY >= (self.b.y * 2):
            self.m = -1  
        if self.b.positionX < 0:
            self.b.changeBallPosition(self.b.x, 0)
            self.player2.points += 1
            self.player2Points.config(text=self.player2.points)

        if self.b.positionY < 0:
            self.m = 1 
        if (self.b.positionX == self.player1.x + 10) & ((self.b.positionY >= self.player1.positionY) & (self.b.positionY <= self.player1.positionY + 50)):
            self.n = -self.n
            self.m = -self.m
        if (self.b.positionX == self.player2.x - 5) & ((self.b.positionY >= self.player2.positionY) & (self.b.positionY <= self.player2.positionY + 50)):
            self.n = -self.n
            self.m = -self.m

        self.b.changeBallPosition(self.n, self.m)
        self.root.after(10, self.movBall)


    def key(self, event):
        if event.char == 'w':
            self.player1.changePlayerPosition(-10) 
            self.canvas.pack(fill=BOTH, expand=1)   
            self.root.update()
        elif event.char == 's': 
            self.player1.changePlayerPosition(10)
            self.canvas.pack(fill=BOTH, expand=1)   
            self.root.update()
        elif event.keycode == 38:
            self.player2.changePlayerPosition(-10) 
            self.canvas.pack(fill=BOTH, expand=1)   
            self.root.update()
        elif event.keycode == 40: 
            self.player2.changePlayerPosition(10)
            self.canvas.pack(fill=BOTH, expand=1)   
            self.root.update()

def main():
    game = Game()
    game.canvas.pack(fill=BOTH, expand=1)
    game.player1Points.config(font=("Courier", 44))
    game.player2Points.config(font=("Courier", 44))
    game.player1Points.place(relx=0.0, rely=1.0, anchor='sw')
    game.player2Points.place(relx=1.0, rely=1.0, anchor='se')
    game.movBall()
    game.root.mainloop()

if __name__ == '__main__':
    main()
 


