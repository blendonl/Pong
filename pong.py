class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.canvas.create_oval(15, 15, 20, 20, fill="#fb0", tags=('ball'))
        self.canvas.move('ball', x/2, y/2)
        self.positionX = x/2
        self.positionY = y/2

    def changeBallPosition(self, x, y):
        self.canvas.move('ball', x, y)
        self.positionX += x
        self.positionY += y

class Player:
        
    def __init__(self, name, root, canvas, x, color):
        self.name = name
        self.canvas = canvas
        self.root = root
        self.x = x + 5
        self.canvas.create_rectangle(self.x, 400/2, self.x + 10, 400/2 + 50, fill=color, tags=(self.name))
        self.positionY = 400/2
        self.points = 0
        
    def changePlayerPosition(self, y): 
        self.canvas.move(self.name, 0, y)
        self.positionY += y  