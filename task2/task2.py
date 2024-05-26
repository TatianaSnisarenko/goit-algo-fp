import turtle


def pifagor_tree(t, length, level):
    if level == 0:
        return
    t.forward(length)
    t.left(45)
    pifagor_tree(t, length * 0.8, level - 1)
    t.right(90)
    pifagor_tree(t, length * 0.8, level - 1)
    t.left(45)
    t.backward(length)


def draw_pifagor_tree(level):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.setpos(0, -200)
    t.pendown()

    t.color("red")

    length = 120
    t.left(90)

    pifagor_tree(t, length, level)

    window.mainloop()


def get_recoursion_level():
    try:
        return int(input("Введіть рівень рекурсії: "))
    except:
        return 8


if __name__ == "__main__":
    level = get_recoursion_level()
    draw_pifagor_tree(level)
