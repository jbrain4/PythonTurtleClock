import turtle
import datetime
import time

# Declare new instances of turtle
clockPen = turtle.Turtle()
hourPen = turtle.Turtle()
minutePen = turtle.Turtle()
secondPen = turtle.Turtle()

# Hide all the pens
clockPen.hideturtle()
hourPen.hideturtle()
minutePen.hideturtle()
secondPen.hideturtle()

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
def drawSecondHand(sec):
	secondPen.clear()
	secondPen.setheading(90)
	secondPen.right(int(sec) * 6)
	secondPen.forward(225)
	secondPen.backward(225)
def hourDots():
	for i in range(0, 12):
		clockPen.forward(300)
		clockPen.dot(20)
		clockPen.backward(300)
		clockPen.right(30)
def hourNumbers():
	clockPen.setheading(270)
	clockPen.forward(25)
	clockPen.setheading(90)
	clockPen.right(30)
	currentNumber = 1
	for i in range(0, 12):
		clockPen.forward(300)
		clockPen.write(currentNumber, align='center', font=('Avenir Next', 36, 'normal'))
		clockPen.backward(300)
		clockPen.right(30)
		currentNumber += 1
	clockPen.home()
def hourNumerals():
	clockPen.setheading(270)
	clockPen.forward(20)
	clockPen.setheading(90)
	clockPen.right(30)
	currentNumeral = 0
	numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
	for i in range(0, 12):
		clockPen.forward(300)
		clockPen.write(numerals[currentNumeral], align='center', font=('Times New Roman', 36, 'normal'))
		clockPen.backward(300)
		clockPen.right(30)
		currentNumeral += 1
	clockPen.home()
def minuteDots(size):
	# Draw the minute/second dots
	clockPen.right(6) # Skip over the 12 o'clock dot
	for i in range(0, 12):
		for i in range(0, 4):
			clockPen.forward(300)
			clockPen.dot(size)
			clockPen.backward(300)
			clockPen.right(6)
		clockPen.right(6)

# Configure each pen
clockPen.penup() # Disable drawing for clockPen
hourPen.pensize(15) # Make the hour hand thick
minutePen.pensize(10) # Make the minute hand medium
secondPen.pensize(5) # Make the second hand thin
secondPen.color('red') # Make the second hand red

# Disable pen animation
clockPen.speed(0)
hourPen.speed(0)
minutePen.speed(0)
secondPen.speed(0)

try:
	time.sleep(1)
	# Draw the dots
	# Face north
	clockPen.setheading(90)

	# Draw the hour dots
	#hourNumerals()
	#hourNumbers()
	hourDots()

	# Face north
	clockPen.setheading(90)

	minuteDots(10)

	# Store the current time
	currentTime = datetime.datetime.now()
	currentHour = currentTime.hour
	currentMinute = currentTime.minute
	currentSecond = currentTime.second

	drawHourHand(currentHour, currentMinute) # Draw the initial hour hand
	drawMinuteHand(currentMinute) # Draw the initial minute hand
	drawSecondHand(currentSecond) # Draw the initial second hand

	# Update the clock
	while True:
		time.sleep(1)

		# Check and update the time after 2 minutes
		currentTime = datetime.datetime.now()
		currentHour = currentTime.hour
		currentMinute = currentTime.minute
		currentSecond = currentTime.second

		# Update and draw the hour and minute hands
		drawSecondHand(currentSecond)

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
