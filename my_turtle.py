import turtle

turtle.setup(500,500)              # Determine the window size
wn = turtle.Screen()               # Get a reference to the window
wn.title("Use the Tab key to toggle between turtles") # Change the window title
wn.bgcolor("lightgrey")           # Set the background color
tess = turtle.Turtle()             # Create two turtles
current_turtle = tess
tess.color("purple")
alex = turtle.Turtle()             # Move them apart
alex.color("orange")


def toggle_handler():
	global current_turtle
	if current_turtle == tess:
		current_turtle = alex
		wn.title("Alex is the current turtle")
		wn.onclick(handler_for_alex)
	else:
		current_turtle = tess
		wn.title("Tess is the current turtle")
		wn.onclick(handler_for_tess)

def handler_for_tess(x, y):
    wn.title("Tess going to {0}, {1}".format(x, y))
    tess.goto(x, y)

def handler_for_alex(x, y):
    wn.title("Alex going to {0}, {1}".format(x, y))
    alex.goto(x, y)

wn.onkey(toggle_handler, "Tab")

wn.listen()
turtle.mainloop()