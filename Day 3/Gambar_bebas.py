import turtle 
def drawRectangle( ttl , x , y , width , height):
    """ Draw a rectangle of dimensions width and height , with upper """ 
    ttl . up()
    ttl . goto(x , y)
    ttl . setheading(0)
    ttl . down()
    for i in range (2):
        ttl . forward(width)
        ttl . right(90)
        ttl . forward(height)
        ttl . right(90)
    ttl . up()
def drawTriangle(ttl , x1 , y1 , x2 , y2 , x3 , y3):
    ttl . penup()
    ttl . goto(x1 , y1)
    ttl . pendown()
    ttl . goto(x2 , y2)
    ttl . goto(x3 , y3)
    ttl . goto(x1 , y1)
    ttl . penup()
def fillTriangle(ttl , x1 , y1 , x2 , y2 , x3 , y3 , color):
    ttl . fillcolor(color) 
    ttl . begin_fill()
    drawTriangle(ttl , x1 , y1 , x2 , y2 , x3 , y3)
    ttl . end_fill()
turtle . setup(1500 , 1000 , 0, 0)
myOrange = "#FF7A00"
myBlack  = "#000000"
myBrown  = "#8B4513"
myYellow = "#FFD700"
myPurple = "#6A0DAD"
Joe = turtle . Turtle ()
Joe . screen . colormode (225)
drawRectangle(Joe , 0, 300 , 600 , 300)
Joe . goto(0 , 0)
fillTriangle(Joe , 0, 0, 0 , 300 , 200 , 300 , myOrange)
fillTriangle(Joe , 0, 0, 200 , 300 , 400 , 300 , myBlack)
fillTriangle(Joe , 0, 0, 400 , 300 , 600 , 300 , myBrown)
fillTriangle(Joe , 0, 0, 600 , 300 , 600 , 150 , myYellow)
fillTriangle(Joe , 0, 0, 600 , 150 , 600 , 0 , myPurple)
Joe . hideturtle()
ts = turtle . getscreen()
tc = ts . getcanvas()
tc . postscript(file = " SeychellesFlag . eps ")
turtle.done()