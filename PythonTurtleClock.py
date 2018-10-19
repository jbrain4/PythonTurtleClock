import turtle
import datetime
import time

class PythonTurtleClock():
	def __init__(self):
		# Declare new instances of turtle
		self.clockPen = turtle.Turtle()
		self.hourPen = turtle.Turtle()
		self.minutePen = turtle.Turtle()
		self.secondPen = turtle.Turtle()

		# Hide all the pens
		self.clockPen.hideturtle()
		self.hourPen.hideturtle()
		self.minutePen.hideturtle()
		self.secondPen.hideturtle()

		# Configure each pen
		self.clockPen.penup() # Disable drawing for clockPen
		self.hourPen.pensize(15) # Make the hour hand thick
		self.minutePen.pensize(10) # Make the minute hand medium
		self.secondPen.pensize(5) # Make the second hand thin
		self.secondPen.color('red') # Make the second hand red

		# Disable pen animation
		self.clockPen.speed(0)
		self.hourPen.speed(0)
		self.minutePen.speed(0)
		self.secondPen.speed(0)

	# Define the drawing functions
	def drawHourHand(self, hour, min):
		self.hourPen.clear()
		self.hourPen.setheading(90)
		self.hourPen.right((int(hour) * 30) + (int(min)/2))
		self.hourPen.forward(175)
		self.hourPen.backward(175)
	def drawMinuteHand(self, min):
		self.minutePen.clear()
		self.minutePen.setheading(90)
		self.minutePen.right(int(min) * 6)
		self.minutePen.forward(225)
		self.minutePen.backward(225)
	def drawSecondHand(self, sec):
		self.secondPen.clear()
		self.secondPen.setheading(90)
		self.secondPen.right(int(sec) * 6)
		self.secondPen.forward(225)
		self.secondPen.backward(225)
	def hourDots(self):
		for i in range(0, 12):
			self.clockPen.forward(300)
			self.clockPen.dot(20)
			self.clockPen.backward(300)
			self.clockPen.right(30)
	def hourNumbers(self):
		self.clockPen.setheading(270)
		self.clockPen.forward(25)
		self.clockPen.setheading(90)
		self.clockPen.right(30)
		currentNumber = 1
		for i in range(0, 12):
			self.clockPen.forward(300)
			self.clockPen.write(currentNumber, align='center', font=('Avenir Next', 36, 'normal'))
			self.clockPen.backward(300)
			self.clockPen.right(30)
			currentNumber += 1
		self.clockPen.home()
	def hourNumerals(self):
		self.clockPen.setheading(270)
		self.clockPen.forward(20)
		self.clockPen.setheading(90)
		self.clockPen.right(30)
		currentNumeral = 0
		numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
		for i in range(0, 12):
			self.clockPen.forward(300)
			self.clockPen.write(numerals[currentNumeral], align='center', font=('Times New Roman', 36, 'normal'))
			self.clockPen.backward(300)
			self.clockPen.right(30)
			currentNumeral += 1
		self.clockPen.home()
	def minuteDots(self, size):
		# Draw the minute/second dots
		self.clockPen.right(6) # Skip over the 12 o'clock dot
		for i in range(0, 12):
			for i in range(0, 4):
				self.clockPen.forward(300)
				self.clockPen.dot(size)
				self.clockPen.backward(300)
				self.clockPen.right(6)
			self.clockPen.right(6)

	def mainloop(self):
		try:
			time.sleep(1)
			# Draw the dots
			# Face north
			self.clockPen.setheading(90)

			# Draw the hour dots
			#hourNumerals()
			#hourNumbers()
			self.hourDots()

			# Face north
			self.clockPen.setheading(90)

			self.minuteDots(10)

			# Store the current time
			currentTime = datetime.datetime.now()
			currentHour = currentTime.hour
			currentMinute = currentTime.minute
			currentSecond = currentTime.second

			self.drawHourHand(currentHour, currentMinute) # Draw the initial hour hand
			self.drawMinuteHand(currentMinute) # Draw the initial minute hand
			self.drawSecondHand(currentSecond) # Draw the initial second hand

			# Update the clock
			while True:
				time.sleep(1)

				# Check and update the time after 2 minutes
				currentTime = datetime.datetime.now()
				currentHour = currentTime.hour
				currentMinute = currentTime.minute
				currentSecond = currentTime.second

				# Update and draw the hour and minute hands
				self.drawSecondHand(currentSecond)

				if currentSecond == 0:
					self.minutePen.clear()
					if currentMinute == 59:
						currentMinute = 0
					else:
						currentMinute += 1

					# Draw the hands
					self.drawMinuteHand(currentMinute)
					self.drawHourHand(currentHour, currentMinute)

					# Update the hour if the minute hand is at minute 0
					if currentMinute == 0:
						if currentHour == 24:
							currentHour = 1
						else:
							currentHour += 1
		except KeyboardInterrupt:
			exit()
