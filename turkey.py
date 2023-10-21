import random
import turtle
def draw_turkey():
    t = turtle.Turtle()
    t.speed(0)

    # Draw turkey body
    t.color("brown")
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()

    # Draw turkey head
    t.penup()
    t.goto(115,95)
    t.pendown()
    t.color("red")
    t.circle(20)
    
     # Draw turkey eyes
    t.penup()
    t.goto(120,100)
    t.pendown()
    t.color("green")
    t.circle(5)
    
    t.penup()
    t.goto(105,120)
    t.pendown()
    t.color("green")
    t.circle(5)

    # Draw turkey feathers
    feather_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

    for _ in range(100):
        feather_color = random.choice(feather_colors)
        draw_feather(t, feather_color)

    turtle.done()

def draw_feather(t, color):
    t.penup()
    t.goto(random.randint(0, 70), random.randint(0, 70))
    t.pendown()
    
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(30)
        t.left(120)
    t.end_fill()

if __name__ == "__main__":
    draw_turkey()

