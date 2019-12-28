from tkinter import *
import tkinter as tk
import pong
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Pong")
        label.config(bg="black", fg="white",font=("Courier", 44))
        label.pack(pady=100,padx=10)
        
        button = tk.Button(self, text="Play",
                            command=lambda: controller.show_frame(PageOne))
        button.config(bg="black", fg="white",width=50)
        button.pack()

        button2 = tk.Button(self, text="Exit",
                            command=lambda: controller.destroy())
        button2.config(bg="black", fg="white",width=50)
        button2.pack(side="bottom")
        

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.n = 1
        self.m = 1
        self.width = 510
        self.height = 400
        self.canvas = Canvas(self)
        self.canvas.config(bg="black", height=500)
        self.player1 = pong.Player("Avdush", self, self.canvas, 0, "#f50")
        self.player2 = pong.Player("Avdushi", self, self.canvas, parent.winfo_width() - 20, "#05f")
        controller.bind("<Key>", self.key)
        self.canvas.create_line(10, 90, parent.winfo_width(), 90,fill="white")
        self.player1Name = tk.Label(self, text = self.player1.name)
        self.player2Name = tk.Label(self, text = self.player2.name) 
        self.player1Points = tk.Label(self, text = self.player1.points)
        self.player2Points = tk.Label(self, text = self.player2.points) 
        
        self.b = pong.Ball(self.canvas, self.width, self.height)
        self.canvas.pack(fill=BOTH, expand=False)

        self.player1Points.config(font=("Courier", 40), fg="white", bg="black")
        self.player2Points.config(font=("Courier", 40), fg="white", bg="black")
        self.player1Name.config(font=("Courier", 24), fg="white", bg="black")
        self.player2Name.config(font=("Courier", 24), fg="white", bg="black")
        self.player1Points.place(relx=0.45, rely=0.1, anchor=CENTER)
        self.player2Points.place(relx=0.6, rely=0.1, anchor=CENTER)
        self.player1Name.place(relx=0.2, rely=0.1, anchor=CENTER)
        self.player2Name.place(relx=0.8, rely=0.1, anchor=CENTER)

    
    def movBall(self):

        if((self.player1.points < 10)) and ((self.player2.points < 10)):
            self.b.changeBallPosition(self.n, self.m)
            if self.b.positionX > self.width:
                self.b.changeBallPosition(-self.width/2, 0) 
                self.player1.points += 1
                self.player1Points.config(text=self.player1.points)
            if self.b.positionY > self.height - 20:
                 self.m = -1  
                 self.b.changeBallPosition(self.n, self.m)
            if self.b.positionX < 0:
                self.b.changeBallPosition(self.width/2, 0)
                self.player2.points += 1
                self.player2Points.config(text=self.player2.points)
        
            if self.b.positionY < 75:
                self.m = 1 
                self.b.changeBallPosition(self.n, self.m)
            if (self.b.positionX == self.player1.x ) and ( self.player1.positionY <= self.b.positionY <= self.player1.positionY + 50):
                self.n = -self.n
                self.m = -self.m
                self.b.changeBallPosition(self.n, self.m)
            elif (self.b.positionX == self.player2.x ) and ((self.player2.positionY <= self.b.positionY <= self.player2.positionY + 50)):
                self.n = -self.n
                self.m = -self.m
                self.b.changeBallPosition(self.n, self.m)

            
            self.parent.after(10, self.movBall)
        else:
            if self.player1.points == 10:
                winner = tk.Label(self, text = "The Winner is " + str(self.player1.name))
                winner.config(font=("Courier", 25), bg="black", fg="white")
                winner.place(relx=0.5, rely=0.5, anchor=CENTER)
            else:
                winner = tk.Label(self, text = "The Winner is " + str(self.player1.name))
                winner.config(font=("Courier", 25), bg="black", fg="white")
                winner.place(relx=0.5, rely=0.5, anchor=CENTER)
        

    def key(self, event):
        if event.char == 'w':
            if(self.player1.positionY >= 85): 
                self.player1.changePlayerPosition(-10) 
                self.canvas.pack(fill=BOTH, expand=1)   
                self.parent.update()
            
        elif event.char == 's': 
            if(self.player1.positionY <= 340):
                self.player1.changePlayerPosition(10)
                self.canvas.pack(fill=BOTH, expand=1)   
                self.parent.update()
        elif event.keycode == 38:
            if(self.player2.positionY >= 85): 
                self.player2.changePlayerPosition(-10) 
                self.canvas.pack(fill=BOTH, expand=1)   
                self.parent.update()
        elif event.keycode == 40: 
            if(self.player2.positionY <= 340):
                self.player2.changePlayerPosition(10)
                self.canvas.pack(fill=BOTH, expand=1)   
                self.parent.update()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!")
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

