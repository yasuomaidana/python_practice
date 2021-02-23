import turtle
import random as rand
import winsound

wn = turtle.Screen()
wn.title("Pong by Yasuo Maidana")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

class Paddle(turtle.Turtle):
    def __init__(self,x=0,y=0):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x,y)
    def goUp(self):
        y = self.ycor()
        y += 20
        self.sety(y)
    def goDown(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
class Ball(Paddle):
    dx = 0.5
    dy = 0.5
    cR=0
    cL=0
    def __init__(self):
        super().__init__(0,0)
        self.shapesize(1,1)
    def goCenter(self):
        self.dx=pow(-1,rand.randint(0,1))*0.5
        self.dy=pow(-1,rand.randint(0,1))*0.5
        self.goto(0,0)
    def checkEdgeX(self):
        if self.xcor()>390 or self.xcor()<-390:
            xcor = self.xcor()
            self.goCenter()
            if xcor>390: 
                self.cR+=1
            else: 
                self.cL+=1

            return self.cR,self.cL
        return False,False

    def checkEdgeY(self):
        if self.ycor()>290 or self.ycor()<-290:
            self.dy*=-1
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    def move(self):
        self.checkEdgeY()
        self.setx(self.xcor()+self.dx)
        self.sety(self.ycor()+self.dy)
    def collitionLeft(self,pL):
        if (self.xcor()< -340 and self.xcor()>-350) and (self.ycor()<pL+40) and (self.ycor()>pL-40):
            self.dx*=-1
            self.setx(-339)
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
            
    def collitionRight(self,pR):
        if (self.xcor()>340 and self.xcor()<350) and (self.ycor()<pR+40) and (self.ycor()>pR-40):
            self.dx*=-1
            self.setx(339)
            winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
class Pen(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.write("Player A:0 Player B: 0",align="center",font=("Courier",24,"normal"))
    def wr(self,cR,cL):
        text="Player A:{} Player B: {}".format(cR,cL)
        
        self.clear()
        self.write(text,align="center",font=("Courier",24,"normal"))


#Paddle definition
paddle_A=Paddle(-350)
paddle_B=Paddle(350)

#Ball
ball=Ball()

#Pen
pen = Pen()

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_A.goUp,"w")
wn.onkeypress(paddle_A.goDown,"s")
wn.onkeypress(paddle_B.goUp,"Up")
wn.onkeypress(paddle_B.goDown,"Down")


while True:
    wn.update()
    ball.move()
    cR,cL = ball.checkEdgeX()
    if cR + cL:
        pen.wr(cR,cL)
    ball.collitionLeft(paddle_A.ycor())
    ball.collitionRight(paddle_B.ycor())
