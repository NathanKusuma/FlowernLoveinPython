import turtle

a=turtle.Turtle()
b=turtle.Screen()

b.bgcolor('black')
a.pencolor('white')
a.speed(125)
euy=('red','yellow','green','blue')

for n in range(10):
    for x in range(8):
        a.speed(x+10)
        for i in range(2):
            a.pensize(2)
            a.circle(80+n*20,90)
            a.lt(90)
        a.lt(45)
    a.pencolor(euy[n%4])
b.exitonclick()
