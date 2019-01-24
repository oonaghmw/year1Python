from exturtle import * # import all turtle functions
from math import cos, sin, pi #importing functions from math module

turtle = Turtle() #making new turtle to manipulate

def star(turtle, x, y, points, R, r):
	"""
	Draws a star shape using exturtle.
	Args:
		'turtle' - which Turtle to use
		'x', 'y' - the (x, y) coordinates of centre of star
		'points' - how many points star has
		'R'      - radius of outer corners
		'r'      - radius of inner corners
	Returns:   None
	"""
	A = 2*pi/points #the angle between points
	penup(turtle) # to not draw
	goto(turtle, x, y) # go to centre of star
	for n in range(points):
		coord_ax = x + r*sin((n-0.5)*A) # x coordinate for start of a point
		coord_ay = y + r*cos((n-0.5)*A) # y coordinate for start of a point
		goto(turtle, coord_ax, coord_ay)
		pendown(turtle) # start drawing
		coord_Px = x + R*sin(A*n) # x coordinate for tip of point
		coord_Py = y + R*cos(A*n) # y coordinate for tip of point
		goto(turtle, coord_Px, coord_Py)
		coord_bx = x + r*sin((n+0.5)*A) #x coordinate for end of point
		coord_by = y + r*cos((n+0.5)*A) #y coordinate for end of point
		goto(turtle, x - coord_bx, coord_by)
	
#row of stars:
star(turtle, -300, 0, 5, 80, 35)
star(turtle, -100, 0, 6, 80, 35)
star(turtle, 100, 0, 7, 80, 35)
star(turtle, 300, 0, 8, 80, 35)

clear(turtle) 

def ring(turtle, cx, cy, Nstars, radius, points, R, r):
	"""
	Draws a ring of stars using previous star function and exturtle.
	Args:
		'turtle'   - Turtle being used to draw
		'cx', 'cy' - (x, y) coordinates for centre of ring
		'Nstars'   - number of stars
		'Radius'   - radius of ring
		'points'   - how many points stars have
	Returns:     None
	"""
	A2 = 2*pi/Nstars # angle between stars
	penup(turtle) #stop drawing
	goto(turtle, cx, cy) # go to centre of ring
	for s in range(Nstars):
		locationx = cx + radius*cos(s*A2) # x coordinate of centre of individual star
		locationy = cy + radius*sin(s*A2) # y coordinate of centre of individual star
		star(turtle, locationx, locationy, points, R, r) # draw star with centre as calculated position in ring
		
ring(turtle, 0, 0, 12, 200, 5, 30, 11)


mainloop()

#I AM THE FINAL COPY