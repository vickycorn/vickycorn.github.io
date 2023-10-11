# simple python turtle script to draw a K
import turtle				# import the turtle module


window = turtle.Screen()	# define the window
t = turtle.Turtle()			# create the turtle object

t.speed(1)					# set the turtle's speed

t.left(90)					# turn left 90 degrees
Length = 20	
t.forward(70)				# move forward 70 pixels
t.back(0)					# move back 0 pixels
t.right(90)					# turn right 0 degrees
Width = 70
t.forward(70)				# move forward 70 pixels
t.back(0)					# move back 0 pixels
t.right(90)					# turn right 90 degrees
Length = 20
t.forward(70)				# move forward 70 pixels
t.back(0)					# move back 0 pixels
t.right(90)                 # move right 90 degrees
Width = 70
t.forward(70)               # move forward 70 pixels

turtle.mainloop()				# stop the window from closings
