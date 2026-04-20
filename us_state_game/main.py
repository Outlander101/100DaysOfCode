import pandas
import turtle
import os

IMAGE = "./blank_states_img.gif"
STATES_CSV = "./50_states.csv"
MISSING_STATES_CSV = "./missed_us_states.csv"
TOTAL_STATES = 50
EXIT_KEY = "Exit"

# def get_mouse_click_cursor(x, y):
#     print(x, y)

def main():
    screen = turtle.Screen()
    screen.title("U.S. State Game")
    screen.addshape(IMAGE)
    turtle.shape(IMAGE)

    # Get the coordinates in the states Image corresponding to states
    # turtle.onscreenclick(get_mouse_click_cursor)
    # turtle.mainloop()

    if os.path.isfile(STATES_CSV):
        data = pandas.read_csv(STATES_CSV)
        all_states = data.state.to_list()
        guessed_states = []

        while len(guessed_states) < 50:
            guessed_state = screen.textinput(title=f"{len(guessed_states)}/{TOTAL_STATES} State Correct", prompt="Guess anothr State").title()

            if guessed_state == EXIT_KEY:
                # missed_states = []
                # for state in all_states:
                #     if state not in guessed_states:
                #         missed_states.append(state)
                missed_states = [state for state in all_states if state not in guessed_states]
                df = pandas.DataFrame(missed_states)
                df.to_csv(MISSING_STATES_CSV)
                break

            elif guessed_state in all_states and guessed_state not in guessed_states:
                guessed_states.append(guessed_state)
                t = turtle.Turtle()
                t.penup()
                state_data = data[data.state == guessed_state]
                t.goto(state_data.x.item(), state_data.y.item())
                t.write(state_data.state.item())
                # t.write(guessed_state)
    else:
        print(f"Invalid path: {STATES_CSV}")

    screen.exitonclick()

if __name__ == "__main__":
    main()