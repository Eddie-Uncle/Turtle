import turtle

t=turtle.Turtle()
t.speed(0)

def square(length, angle):
	for i in range(4):
		t.forward(length)
		t.right(angle)
	
for i in range(100):
	square(100, 90)
	t.right(11)