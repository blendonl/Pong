class Ball:
    def __init__(self, root, canvas, x, y, player1, player2, points1, points2):
        self.root = root
        self.canvas = canvas
        self.canvas.create_oval(15, 15, 20, 20, fill="#fb0", tags=('ball'))
        self.canvas.move('ball', x, y)
        self.positionX = x 
        self.positionY = y 
        self.player1Points = points1
        self.player2Points = points2
        self.x = x
        self.y = y   
        self.n = 1
        self.m = 1
        self.points1 = 0
        self.points2 = 0
        self.player1 = player1
        self.player2 = player2
    def changeBallPosition(self, x, y):
        self.canvas.move('ball', x, y)
        self.positionX += x
        self.positionY += y

    def movBall(self):
        if self.positionX > self.x * 2:
            self.changeBallPosition(-self.x, 0) 
            self.player1.points += 1
            self.player1Points.config(text=self.player1.points)
        if self.positionY >= self.y * 2 - 20:
            self.m = -1  
        if self.positionX < 0:
            self.changeBallPosition(self.x, 0)
            self.player2.points += 1
            self.player2Points.config(text=self.player2.points)

        if self.positionY < 0:
            self.m = 1 
        if (self.positionX == self.player1.x) & ((self.positionY >= self.player1.positionY) & (self.positionY <= self.player1.positionY + 50)):
            self.n = -self.n
            self.m = -self.m
        if (self.positionX == self.player2.x - 10) & ((self.positionY >= self.player2.positionY) & (self.positionY <= self.player2.positionY + 50)):
            self.n = -self.n
            self.m = -self.m

        self.changeBallPosition(self.n, self.m)
        self.root.after(10, self.movBall)
