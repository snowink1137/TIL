import turtle

s = turtle.Screen()
p = turtle.Pen()

class MagicBrush:
    p.color('red')
    def draw_square(self):
        for i in range(4):
            p.forward(100)
            p.right(90)


    def draw_triangle(self):
        for i in range(3):
            p.forward(100)
            p.right(120)


    def go(self):
        p.forward(200)


    def turn(self):
        p.right(90)
        


m1 = MagicBrush()
m2 = MagicBrush()

brad = turtle.Turtle()
brad.shape('turtle')
brad.speed(2)
brad.forward(100)



s.mainloop()


