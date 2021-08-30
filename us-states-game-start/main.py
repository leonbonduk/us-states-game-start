import turtle
import pandas

def check_guess(guess, states):
    guess = guess.title()
    print(guess)
    state_extract = states[states.state == guess]

    print(state_extract)
    print(state_extract.index)

    if state_extract.size > 0:
        print("Yes")
        state_writer = turtle.Turtle()
        state_writer.hideturtle()+
        state_writer.penup()
        state_writer.goto(float(state_extract.x), float(state_extract.y))
        state_writer.write(guess)
        return True

    else:
        print("No")
        return False

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

game_is_on =True

score = 0

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

    if answer_state == "end":
        game_is_on = False
    else:
        if check_guess(answer_state, states_data):
            score += 1
    screen.title("U.S. State Game: " + str(score) + "/50")

screen.exitonclick()