import turtle
import random

def draw_branch(t, branch_length, pen_size):
    if branch_length > 5:
        t.pensize(pen_size)
        t.forward(branch_length)
        angle = random.randint(22, 30)
        right_branch_length = random.randint(15, 25)
        t.right(angle)
        draw_branch(t, branch_length - right_branch_length, pen_size - 1)
        t.left(angle * 2)
        left_branch_length = random.randint(15, 25)
        draw_branch(t, branch_length - left_branch_length, pen_size - 1)
        t.right(angle)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.setpos(0, -300)
    t.left(90)
    t.pendown()
    t.color("purple")

    draw_branch(t, 120, 10)

    screen.mainloop()

if __name__ == "__main__":
    main()
