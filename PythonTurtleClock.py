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

		# Defing Customization Variables (default values)
		self.style = 'simple'
		self.hourHandColor = 'black'
		self.minuteHandColor = 'black'
		self.secondHandColor = 'red'
		self.hourDotColor = 'black'
		self.minuteSecondDotColor = 'black'
		self.hourHandThickness = 15
		self.minuteHandThickness = 10
		self.secondHandThickness = 5
		self.hourHandLength = 175
		self.minuteHandLength = 225
		self.secondHandLength = 225

		# Hide all the pens
		self.clockPen.hideturtle()
		self.hourPen.hideturtle()
		self.minutePen.hideturtle()
		self.secondPen.hideturtle()

		# Configure each pen
		self.clockPen.penup() # Disable drawing for clockPen
		
		# Disable pen animation
		self.clockPen.speed(0)
		self.hourPen.speed(0)
		self.minutePen.speed(0)
		self.secondPen.speed(0)

	# Define the drawing functions
	def drawHourHand(self, hour, min):
		self.hourPen.pensize(self.hourHandThickness) # Make the hour hand thick
		self.hourPen.color(self.hourHandColor) # Color the hour hand
		self.hourPen.clear()
		self.hourPen.setheading(90)
		self.hourPen.right((int(hour) * 30) + (int(min)/2))
		self.hourPen.forward(self.hourHandLength)
		self.hourPen.backward(self.hourHandLength)
	def drawMinuteHand(self, min):
		self.minutePen.pensize(self.minuteHandThickness) # Make the minute hand medium
		self.minutePen.color(self.minuteHandColor) # Color the minute hand
		self.minutePen.clear()
		self.minutePen.setheading(90)
		self.minutePen.right(int(min) * 6)
		self.minutePen.forward(self.minuteHandLength)
		self.minutePen.backward(self.minuteHandLength)
	def drawSecondHand(self, sec):
		self.secondPen.pensize(self.secondHandThickness) # Make the second hand thin
		self.secondPen.color(self.secondHandColor) # Color the second hand
		self.secondPen.clear()
		self.secondPen.setheading(90)
		self.secondPen.right(int(sec) * 6)
		self.secondPen.forward(self.secondHandLength)
		self.secondPen.backward(self.secondHandLength)

	# Functions for drawing dots
	def hourDots(self):
		self.clockPen.color(self.hourDotColor)
		for i in range(0, 12):
			self.clockPen.forward(300)
			self.clockPen.dot(20)
			self.clockPen.backward(300)
			self.clockPen.right(30)
	def hourNumbers(self):
		self.clockPen.color(self.hourDotColor)
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
		self.clockPen.color(self.hourDotColor)
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

	# 12, 3, 6, 9 only
	def lessHourDots(self):
		self.clockPen.color(self.hourDotColor)
		for i in range(0, 12):
			self.clockPen.forward(300)
			self.clockPen.dot(20)
			self.clockPen.backward(300)
			self.clockPen.right(90)
	def lessHourNumbers(self):
		self.clockPen.color(self.hourDotColor)
		self.clockPen.setheading(270)
		self.clockPen.forward(25)
		self.clockPen.setheading(90)
		self.clockPen.right(90)
		currentNumber = 3
		for i in range(0, 4):
			self.clockPen.forward(300)
			self.clockPen.write(currentNumber, align='center', font=('Avenir Next', 36, 'normal'))
			self.clockPen.backward(300)
			self.clockPen.right(90)
			currentNumber += 3
		self.clockPen.home()
	def lessHourNumerals(self):
		self.clockPen.color(self.hourDotColor)
		self.clockPen.setheading(270)
		self.clockPen.forward(20)
		self.clockPen.setheading(90)
		self.clockPen.right(90)
		currentNumeral = 0
		numerals = ['III', 'VI', 'IX', 'XII']
		for i in range(0, 4):
			self.clockPen.forward(300)
			self.clockPen.write(numerals[currentNumeral], align='center', font=('Times New Roman', 36, 'normal'))
			self.clockPen.backward(300)
			self.clockPen.right(90)
			currentNumeral += 1
		self.clockPen.home()


	def minuteDots(self, size):
		# Draw the minute/second dots
		self.clockPen.color(self.minuteSecondDotColor)
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
			# Face north
			self.clockPen.setheading(90)

			# Draw the  dots
			if self.style == 'simple':
				self.hourDots()
				self.minuteDots(10)
			elif self.style == 'minimal':
				self.lessHourDots()
			elif self.style == 'clean':
				self.hourDots()
			elif self.style == 'modern':
				self.hourNumbers()
				self.clockPen.left(90)
				self.minuteDots(10)
			elif self.style == 'minimal-modern':
				self.lessHourNumbers()
			elif self.style == 'clean-modern':
				self.hourNumbers()
			elif self.style == 'classic':
				self.hourNumerals()
				self.clockPen.left(90)
				self.minuteDots(5)
			elif self.style == 'minimal-classic':
				self.lessHourNumerals()
			elif self.style == 'clean-classic':
				self.hourNumerals()
			else:
				print('No style called "%s"' % self.style)
				print('Defaulting to "simple"')
				self.hourDots()
				self.minuteDots(10)

			# Face north
			self.clockPen.setheading(90)

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
