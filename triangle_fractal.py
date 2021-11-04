import turtle as tl

def draw_fractal(scale):
    if scale > 2:
        for i in range(3):
            tl.forward(scale)
            tl.left(120)
        tl.forward(scale/2)
        tl.left(60)
        scale *= 0.5
        draw_fractal(scale)

scale = 500
tl.speed(10)
tl.pensize(2)
tl.penup()
tl.goto(-scale/2, -scale/2)
tl.pendown()

draw_fractal(scale)
tl.done()