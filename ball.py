class Ball:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.canvas.create_oval(15, 15, 20, 20, fill="#fb0", tags=('ball'))
        self.positionX = 20 
        self.positionY = 20 
        self.x = x
        self.y = y   

    def changeBallPosition(self, x, y):
        self.canvas.move('ball', x, y)
        self.positionX += x
        self.positionY += y

   
