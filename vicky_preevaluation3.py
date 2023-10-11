import turtle				# import the turtle module

sides = 3

window = turtle.Screen()	# define the window
t = turtle.Turtle()			# create the turtle object

t.speed(10)					# set the turtle's speed



for i in range (0,sides):

    t.left(360/sides)					# turn left 90 degrees
    t.forward(70)				# move forward 70 pixels
    t. right (190)
    t. forward (70)
    t. left (190)


turtle.mainloop()				# stop the window from closings
