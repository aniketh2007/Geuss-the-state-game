import turtle
from turtle import Screen
import pandas
screen = Screen()
screen.title("Guess the state")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the state",
                                    prompt="What's another state name ? ").title()
    # Exit keyword from the user to exit and generation of state_to_learn.csv which the user missed 
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break
    
    # If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:
        guessed_state.append(answer_state)
        # Create a turtle to write the name of state at the state's X and Y position
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state==answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(arg=answer_state)



    






