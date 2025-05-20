import turtle
from turtle import Turtle, Screen
import pandas

FONT = ("Courier", 10, "bold")
screen = Screen()
screen.title("Türkiye İller Oyunu")
image = "turkiye_haritasi.gif"
screen.addshape(image)
turtle.shape(image)

# def cord(x, y):
#     print(x, y)
#
# screen.onscreenclick(cord)

states_data = pandas.read_csv("iller.csv")
iller = states_data.il.to_list()

guessed_states = []
while len(guessed_states) < 81:
    guessed_state = screen.textinput(title=f"{len(guessed_states)}/81 İl Bulundu", prompt="İl adı?")
    for il in iller:
        if guessed_state.title() == il and guessed_state not in guessed_states:
            guessed_states.append(guessed_state)
            row = states_data[states_data.il == il]
            x = int(row.x)
            y = int(row.y)
            t = Turtle()
            t.penup()
            t.color("blue")
            t.hideturtle()
            t.goto(x, y)
            t.write(il, font=FONT)
        elif guessed_state == "İstanbul" or guessed_state == "istanbul" or guessed_state == "İSTANBUL" and\
                guessed_state not in guessed_states:
            guessed_states.append("İstanbul")
            t = Turtle()
            t.penup()
            t.color("blue")
            t.hideturtle()
            t.goto(-354.0, 148.0)
            t.write("İstanbul", font=FONT)
            break
        elif guessed_state == "İzmir" or guessed_state == "izmir" or guessed_state == "İZMİR"\
                and guessed_state not in guessed_states:
            guessed_states.append("İzmir")
            t = Turtle()
            t.penup()
            t.color("blue")
            t.hideturtle()
            t.goto(-440.0, -42.0)
            t.write("İzmir", font=FONT)
            break

t = Turtle()
t.penup()
t.hideturtle()
t.color("red")
t.goto(-150, 0)
t.write("Tebrikler!", font=("Courier", 40, "bold"))
t.goto(-150, -50)
t.write("Oyun Bitti!", font=("Courier", 40, "bold"))

screen.mainloop()