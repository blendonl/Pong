from tkinter import *
import tkinter as tk
import keyboard
import pong
import pages


class Game(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.width = 510
        self.height = 410
        self.container = tk.Frame(self)
        self.geometry(str(self.width) + "x" + str(self.height))
        self.config(bg="black")
        self.container.pack(fill="both", expand = False)
        self.update()
        
      
        self.frames = {}

        for F in (pages.StartPage, pages.PageOne):

            frame = F(self.container, self)
            frame.config(bg="black")
            self.frames[F] = frame
            frame.pack(side="bottom", fill="both", expand=False)



        self.show_frame(pages.StartPage)

    def show_frame(self, cont):
        for F in self.frames.values():
            F.pack_forget()
     
        if(cont == pages.PageOne):
            self.addFrame( cont)            
            self.frames[cont].pack(fill="both", expand = False)
            self.frames[cont].movBall()
        else:
            self.frames[pages.PageOne].destroy()
            frame = self.frames[cont]
            frame.pack(fill="both", expand = False)
        
    def addFrame(self, cont, *winner):
        if(cont == pages.PageTwo):
            frame = cont(self.container, self, winner)
        else:
            frame = cont(self.container, self)
        frame.config(bg="black")
        self.frames[cont] = frame
        frame.pack(side="bottom", fill="both", expand=False)
        frame.pack_forget()



def main():
    game = Game()
 

    game.mainloop()

if __name__ == '__main__':
    main()
 


