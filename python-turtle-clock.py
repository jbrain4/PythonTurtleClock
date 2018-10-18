import turtle
import datetime
import time

# Declare new instances of turtle
clockPen = turtle.Turtle()
hourPen = turtle.Turtle()
minutePen = turtle.Turtle()
#secondPen = turtle.Turtle()

# Hide all the pens
clockPen.hideturtle()
hourPen.hideturtle()
minutePen.hideturtle()
#secondPen.hideturtle()

# Define the drawing functions
def drawHourHand(hour, min):
	hourPen.clear()
	hourPen.setheading(90)
	hourPen.right((int(hour) * 30) + (int(min)/2))
	hourPen.forward(175)
	hourPen.backward(175)

def drawMinuteHand(min):
	minutePen.clear()
	minutePen.setheading(90)
	minutePen.right(int(min) * 6)
	minutePen.forward(225)
	minutePen.backward(225)

# Configure each pen
clockPen.penup() # Disable drawing for clockPen
hourPen.pensize(15) # Make the hour hand thick
minutePen.pensize(10) # Make the minute hand

# Disable pen animation
clockPen.speed(0)
hourPen.speed(0)
minutePen.speed(0)

try:
	# Draw the dots
	# Face north
	clockPen.setheading(90)

	# Draw the hour dots
	for i in range(0, 12):
		clockPen.forward(300)
		clockPen.dot(20)
		clockPen.backward(300)
		clockPen.right(30)

	# Face north
	clockPen.setheading(90)

	# Draw the minute/second dots
	clockPen.right(6) # Skip over the 12 o'clock dot
	for i in range(0, 12):
		for i in range(0, 4):
			clockPen.forward(300)
			clockPen.dot(10)
			clockPen.backward(300)
			clockPen.right(6)
		clockPen.right(6)

	# Store the current time
	currentTime = datetime.datetime.now()
	currentHour = currentTime.hour
	currentMinute = currentTime.minute

	drawHourHand(currentHour, currentMinute) # Draw the initial hour hand
	drawMinuteHand(currentMinute) # Draw the initial minute hand

	# Update the clock
	while True:
		time.sleep(1)

		# Check and update the time after 2 minutes
		currentTime = datetime.datetime.now()
		currentHour = currentTime.hour
		currentMinute = currentTime.minute

		# Update and draw the hour and minute hands
		if currentSecond == 0:
			minutePen.clear()
			if currentMinute == 59:
				currentMinute = 0
			else:
				currentMinute += 1

			# Draw the hands
			drawMinuteHand(currentMinute)
			drawHourHand(currentHour, currentMinute)

			# Update the hour if the minute hand is at minute 0
			if currentMinute == 0:
				if currentHour == 24:
					currentHour = 1
				else:
					currentHour += 1
except KeyboardInterrupt:
	exit()
