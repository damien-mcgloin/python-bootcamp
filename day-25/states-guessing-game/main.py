import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

text = turtle.Turtle()
text.hideturtle()
text.penup()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
x_list = data["x"].to_list()
y_list = data["y"].to_list()

game_continue = True

count = 0

while game_continue:
    answer_state = screen.textinput(title=f"Guess the State {count}/50", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in states_list:
        count += 1
        index = states_list.index(answer_state)
        text.goto(x_list[index], y_list[index])
        text.write(answer_state)
        states_list.remove(answer_state)

    if count == 50:
        game_continue = False


states_data_dict = pandas.DataFrame(states_list)

states_data_dict.to_csv("States_To_Learn.csv")

turtle.mainloop()
