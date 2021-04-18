import turtle

star = turtle.Turtle()
star.shape('turtle')

for i in range(50):
    star.forward(i)
    star.forward(100)
    star.right(144)

turtle.done()