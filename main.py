import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)
import csv
import pandas
data = pandas.read_csv("50_states.csv")
all_state = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

game_is_on = True
guessed_states = []

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in all_state and answer_state not in guessed_states:
        index = all_state.index(answer_state)
        guessed_states.append(answer_state)

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x_cor[index], y_cor[index])
        writer.write(answer_state)

    elif answer_state in guessed_states:
        screen.textinput(title="Already Guessed", prompt="You already guessed that one!")

    else:
        screen.textinput(title="Oops!", prompt="That's not a valid state. Try again.")


screen.exitonclick()
