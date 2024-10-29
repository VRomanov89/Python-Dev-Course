import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


#Main Program
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title = "Guess the state!", 
                                    prompt = "What's another state's name?").title()
    print(answer_state)

    #If the answer is one of the answers?
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        #If right
            #We need to add label onto the image.


screen.exitonclick()