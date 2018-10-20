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
	def drawHourHand(self, hour, min, color, thick, length):
		self.hourPen.pensize(thick) # Make the hour hand thick
		self.hourPen.color(color) # Color the hour hand
		self.hourPen.clear()
		self.hourPen.setheading(90)
		self.hourPen.right(hour * 30 + min/2)
		self.hourPen.forward(length)
		self.hourPen.backward(length)
	def drawMinuteHand(self, min, color, thick, length):
		self.minutePen.pensize(thick) # Make the minute hand medium
		self.minutePen.color(color) # Color the minute hand
		self.minutePen.clear()
		self.minutePen.setheading(90)
		self.minutePen.right(min * 6)
		self.minutePen.forward(length)
		self.minutePen.backward(length)
	def drawSecondHand(self, sec, color, thick, length):
		self.secondPen.pensize(thick) # Make the second hand thin
		self.secondPen.color(color) # Color the second hand
		self.secondPen.clear()
		self.secondPen.setheading(90)
		self.secondPen.right(sec * 6)
		self.secondPen.forward(length)
		self.secondPen.backward(length)

	# The method below is used to draw the 
	def drawHourDots(self, color, less = False):
		self.clockPen.color(color)
		if not less:
			for i in range(0, 12):
				self.clockPen.forward(300)
				self.clockPen.dot(20)
				self.clockPen.backward(300)
				self.clockPen.right(30)
		if less:
			for i in range(0, 4):
				self.clockPen.forward(300)
				self.clockPen.dot(20)
				self.clockPen.backward(300)
				self.clockPen.right(90)
	def drawHourNumbers(self, color, less = False):
		self.clockPen.color(color)
		self.clockPen.setheading(270)
		self.clockPen.forward(25)
		self.clockPen.setheading(90)
		if not less:
			self.clockPen.right(30)
			currentNumber = 1
			for i in range(0, 12):
				self.clockPen.forward(300)
				self.clockPen.write(currentNumber, align='center',
									font=('Avenir Next', 36, 'normal'))
				self.clockPen.backward(300)
				self.clockPen.right(30)
				currentNumber += 1
		if less:
			self.clockPen.right(90)
			currentNumber = 3
			for i in range(0, 4):
				self.clockPen.forward(300)
				self.clockPen.write(currentNumber, align='center',
									font=('Avenir Next', 36, 'normal'))
				self.clockPen.backward(300)
				self.clockPen.right(90)
				currentNumber += 3
		self.clockPen.home()
	def drawHourNumerals(self, color, less = False):
		self.clockPen.color(color)
		self.clockPen.setheading(270)
		self.clockPen.forward(20)
		self.clockPen.setheading(90)
		currentNumeral = 0
		if not less:
			self.clockPen.right(30)
			numerals = ['I', 'II', 'III', 'IV',
						'V', 'VI', 'VII', 'VIII',
						'IX', 'X', 'XI', 'XII']
			for i in range(0, 12):
				self.clockPen.forward(300)
				self.clockPen.write(numerals[currentNumeral], align='center',
									font=('Times New Roman', 36, 'normal'))
				self.clockPen.backward(300)
				self.clockPen.right(30)
				currentNumeral += 1
		if less:
			self.clockPen.right(90)
			numerals = ['III', 'VI', 'IX', 'XII']
			for i in range(0, 4):
				self.clockPen.forward(300)
				self.clockPen.write(numerals[currentNumeral], align='center',
									font=('Times New Roman', 36, 'normal'))
				self.clockPen.backward(300)
				self.clockPen.right(90)
				currentNumeral += 1
		self.clockPen.home()

	def minuteDots(self, size, color):
		self.clockPen.color(color)
		self.clockPen.right(6)
		for i in range(0, 12):
			for i in range(0, 4):
				self.clockPen.forward(300)
				self.clockPen.dot(size)
				self.clockPen.backward(300)
				self.clockPen.right(6)
			self.clockPen.right(6)

	def mainloop(self):
		try:
			self.clockPen.setheading(90)

			if self.style == 'simple':
				self.drawHourDots(self.hourDotColor)
				self.(10, self.minuteSecondDotColor)
				self.minuteDots(10, self.minuteSecondDotColor)
			elif self.style == 'minimal':
				self.drawHourDots(self.hourDotColor, True)
			elif self.style == 'clean':
				self.drawHourDots(self.hourDotColor)
			elif self.style == 'modern':
				self.drawHourNumbers(self.hourDotColor)
				self.clockPen.left(90)
				self.minuteDots(10, self.minuteSecondDotColor)
			elif self.style == 'minimal-modern':
				self.drawHourNumbers(self.hourDotColor, True)
			elif self.style == 'clean-modern':
				self.drawHourNumbers(self.hourDotColor)
			elif self.style == 'classic':
				self.drawHourNumerals(self.hourDotColor)
				self.clockPen.left(90)
				self.minuteDots(5, self.minuteSecondDotColor)
			elif self.style == 'minimal-classic':
				self.drawHourNumerals(self.hourDotColor, True)
			elif self.style == 'clean-classic':
				self.drawHourNumerals(self.hourDotColor)
			else:
				print('No style called "%s"' % self.style)
				print('Defaulting to "simple"')
				self.drawHourDots(self.hourDotColor)
				self.minuteDots(10, self.minuteSecondDotColor)

			self.clockPen.setheading(90)

			currentTime = datetime.datetime.now()
			currentHour = currentTime.hour
			currentMinute = currentTime.minute
			currentSecond = currentTime.second

			self.drawHourHand(currentHour, currentMinute, self.hourHandColor,
							  self.hourHandThickness, self.hourHandLength)
			self.drawMinuteHand(currentMinute, self.minuteHandColor,
								self.minuteHandThickness, self.minuteHandLength)
			self.drawSecondHand(currentSecond, self.secondHandColor,
								self.secondHandThickness, self.secondHandLength)

			while True:
				time.sleep(1)

				currentTime = datetime.datetime.now()
				currentHour = currentTime.hour
				currentMinute = currentTime.minute
				currentSecond = currentTime.second

				self.drawSecondHand(currentSecond, self.secondHandColor,
									self.secondHandThickness,
									self.secondHandLength)

				if currentSecond == 0:
					self.minutePen.clear()
					if currentMinute == 59:
						currentMinute = 0
					else:
						currentMinute += 1

					self.drawMinuteHand(currentMinute, self.minuteHandColor,
										self.minuteHandThickness,
										self.minuteHandLength)
					self.drawHourHand(currentHour, currentMinute,
									  self.hourHandColor,
									  self.hourHandThickness,
									  self.hourHandLength)

					if currentMinute == 0:
						if currentHour == 24:
							currentHour = 1
						else:
							currentHour += 1
		except KeyboardInterrupt:
			exit()
