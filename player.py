class Player:
        


        def __init__(self, name, root, canvas, x):
            self.name = name
            self.canvas = canvas
            self.root = root
            self.x = x
            self.canvas.create_rectangle(self.x, 50, self.x + 10, 100, fill="#f50", tags=(self.name))
            self.positionY = 50
            self.points = 0
           
        def changePlayerPosition(self, y): 
            self.canvas.move(self.name, 0, y)
            self.positionY += y