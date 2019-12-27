from tkinter import *
import tkinter as tk
import keyboard
import player
import ball




def key(event):
    if event.char == 'w':
        player1.changePlayerPosition(-10) 
        canvas.pack(fill=BOTH, expand=1)   
        root.update()
    elif event.char == 's': 
        player1.changePlayerPosition(10)
        canvas.pack(fill=BOTH, expand=1)   
        root.update()
    elif event.keycode == 38:
        player2.changePlayerPosition(-10) 
        canvas.pack(fill=BOTH, expand=1)   
        root.update()
    elif event.keycode == 40: 
        player2.changePlayerPosition(10)
        canvas.pack(fill=BOTH, expand=1)   
        root.update()


root = Tk()
width = 510
height = 300
root.geometry(str(width) + "x" + str(height))
root.bind("<Key>", key)
canvas = Canvas(root)
player1 = player.player("Avdush", root, canvas, 0)
player1.createPlayer()



player2 = player.player("Avdushi", root, canvas, 500)
player2.createPlayer()
canvas.pack(fill=BOTH, expand=1)
player1.changePlayerPosition(0) 
canvas.pack(fill=BOTH, expand=1)   
root.update()
player2.changePlayerPosition(0) 
canvas.pack(fill=BOTH, expand=1)   
root.update()

root.update()
player1Points = tk.Label(root, text = player1.points)
player2Points = tk.Label(root, text = player2.points)
##ll.place(x=0, y=250, anchor='sw')
##lr.place(x=1000, y=250, anchor='se')
player1Points.config(font=("Courier", 44))
player2Points.config(font=("Courier", 44))
player1Points.place(relx=0.0, rely=1.0, anchor='sw')
player2Points.place(relx=1.0, rely=1.0, anchor='se')

b = ball.Ball(root, canvas, width/2, height/2, player1, player2, player1Points, player2Points)


n = -50

b.movBall()

    


root.mainloop()


