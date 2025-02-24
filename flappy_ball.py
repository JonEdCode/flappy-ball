import pgzrun 
WIDTH = 600
HEIGHT = 600
TITLE = "flappy ball"

class Ball():
    def __init__(self,c,s,y,x):
        self.colour = c
        self.size = s
        self.y = y
        self.x = x
        self.vx = 20
        self.vy = 0 
    def draw_ball(self):
        screen.draw.filled_circle((self.x , self.y),self.size,self.colour)

ball1 = Ball("red",100,500,500)

        

def draw():
    screen.fill("black")
    ball1.draw_ball()
def update():

    pass

pgzrun.go()