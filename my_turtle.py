import turtle

turtle.setup(500,500)              # Determine the window size
wn = turtle.Screen()               # Get a reference to the window
wn.title("Use the Tab key to toggle between turtles") # Change the window title
wn.bgcolor("lightgrey")           # Set the background color
tess = turtle.Turtle()             # Create two turtles
tess.color("purple")
tess.pensize(0)
alex = turtle.Turtle()
alex.color("orange")
alex.pensize(0)

current_pensize = 0
current_turtle = tess


def toggle_handler():
	global current_turtle
	if current_turtle == tess:
		current_turtle = alex
		wn.title("{0} is the current turtle, pen size is {1}".format('Alex', current_pensize))
		wn.onclick(handler_for_alex)
	else:
		current_turtle = tess
		wn.title("{0} is the current turtle, pen size is {1}".format('Tess', current_pensize))
		wn.onclick(handler_for_tess)

def handler_for_tess(x, y):
    wn.title("Tess going to {0}, {1}".format(x, y))
    tess.goto(x, y)

def handler_for_alex(x, y):
    wn.title("Alex going to {0}, {1}".format(x, y))
    alex.goto(x, y)

def increase_pensize():
	global current_pensize
	current_pensize += 1
	tess.pensize(current_pensize)
	alex.pensize(current_pensize)
	wn.ontimer(increase_pensize, 2000)

wn.onkey(toggle_handler, "Tab")

wn.listen()
wn.ontimer(increase_pensize, 2000)
turtle.mainloop()