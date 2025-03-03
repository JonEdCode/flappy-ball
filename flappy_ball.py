import pgzrun 
WIDTH = 600
HEIGHT = 600
TITLE = "flappy ball"
gravity = 200

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

ball1 = Ball("red",30,200,200)

        

def draw():
    screen.fill("black")
    ball1.draw_ball()
def update(dt):
    u = ball1.vy 
    ball1.vy += gravity * dt 
    ball1.y = ball1.y + (u + ball1.vy )/ 2 * dt
    
    if ball1.y >= 570:
        ball1.y = 570
        ball1.vy = ball1.vy * -0.8
    ball1.x += ball1.vx * dt
    if ball1.x >= 570:
        ball1.x = 570
        ball1.vx = ball1.vx * -1
    if ball1.x <= 30:
        ball1.x = 30
        ball1.vx = ball1.vx * -1




    

pgzrun.go()