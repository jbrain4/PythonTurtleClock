# Import the required modules.
import turtle # The turtle module used to draw the clock.
import datetime # The datetime module used to get the current time.
import time # The time module used to wait one second.

class PythonTurtleClock():
	# __init__ initializes the PythonTurtleClock class
	def __init__(self):
		# Define four new instance of the turtle object
		# to use when drawing the clock.
		self.clockPen = turtle.Turtle()
		self.hourPen = turtle.Turtle()
		self.minutePen = turtle.Turtle()
		self.secondPen = turtle.Turtle()

		# Define 12 variables to store different attributes of the clock.
		# Each value listed below is the default for the attribute.
		self.style = 'simple' # Stores the style of the clock (9 styles total).
		self.hourHandColor = 'black' # Stores hour hand's color.
		self.minuteHandColor = 'black' # Stores the minute hand's color.
		self.secondHandColor = 'red' # Stores the second hand's color.
		self.hourDotColor = 'black' # Stores the hour markers' color.
		self.minuteSecondDotColor = 'black' # Stores the minute markers' color.
		self.hourHandThickness = 15 # Stores the hour hand's thickness in px.
		self.minuteHandThickness = 10 # Stores the minute hand's thickness in px.
		self.secondHandThickness = 5 # Stores the second hand's thinkness in px.
		self.hourHandLength = 175 # Stores the hour hand's length in px.
		self.minuteHandLength = 225 # Stores the minute hand's length in px.
		self.secondHandLength = 225 # Stores the second hand's length in px.

		# Hide each of the turtle icons from the user.
		self.clockPen.hideturtle()
		self.hourPen.hideturtle()
		self.minutePen.hideturtle()
		self.secondPen.hideturtle()

		# Prevent the clockPen from drawing a line behind it.
		self.clockPen.penup()

		# Disable the animation of each of the pens to speed up the program.
		self.clockPen.speed(0)
		self.hourPen.speed(0)
		self.minutePen.speed(0)
		self.secondPen.speed(0)

	# The function below is used to draw the hour hand of the clock.
	# The "hour" and "min" arguments are used to calculate the position
	# of the hour hand on the clock face. The "color" argument is the color
	# of the hour hand line. The "thick" argument is used to set the
	# thickness of the line to be drawn in pixels. The "length"
	# argument is how far the line will be drawn from the center of the clock.
	def drawHourHand(self, hour, min, color, thick, length):
		self.hourPen.pensize(thick) # Set the thickness of the line.
		self.hourPen.color(color) # Set the color of the line.
		self.hourPen.clear() # Clear the previous hour hand.
		self.hourPen.setheading(90) # Face 12 o'clock
		self.hourPen.right(hour * 30 + min/2) # Rotate 30 degrees for every hour
											  # then .5 degrees for every minute.
		self.hourPen.forward(length) # Draw the line to the distance specified.
		self.hourPen.backward(length) # Return to the center of the clock.

	# The function below is used to draw the minute hand of the clock.
	# The "min" argument is used to calculate the position of the minute
	# hand on the clock face. The "color" argument is the color of the minute
	# hand line. The "thick" argument is used to set the thickness of the
	# line to be drawn in pixels. The "length" argument is how far the
	# line will be drawn from the center of the clock.
	def drawMinuteHand(self, min, color, thick, length):
		self.minutePen.pensize(thick) # Set the thickness of the line.
		self.minutePen.color(color) # Set the color of the line.
		self.minutePen.clear() # Clear the previous minute hand.
		self.minutePen.setheading(90) # Face 12 o'clock
		self.minutePen.right(min * 6) # Rotate 6 degrees for every minute.
		self.minutePen.forward(length) # Draw the line to the distance specified.
		self.minutePen.backward(length) # Return to the center of the clock.

	# The function below is used to draw the second hand of the clock.
	# The "sec" argument is used to calculate the position of the second
	# hand on the clock face. The "color" argument is the color of the hour
	# hand line. The "thick" argument is used to set the thickness of the
	# line to be drawn in pixels. The "length" argument is how far the
	# line will be drawn from the center of the clock.
	def drawSecondHand(self, sec, color, thick, length):
		self.secondPen.pensize(thick) # Set the thickness of the line.
		self.secondPen.color(color) # Set the color of the line.
		self.secondPen.clear() # Clear the previous second hand.
		self.secondPen.setheading(90) # Face 12 o'clock
		self.secondPen.right(sec * 6) # Rotate 6 degrees for every second.
		self.secondPen.forward(length) # Draw the line to the distance specified.
		self.secondPen.backward(length) # Return to the center of the clock.

	# The function below is used to draw the hour indicators (dot style).
	# The "color" argument is the color of the dots. When the "less" argument
	# is True the function will only draw the 12, 3, 6, and 9 o'clock dots.
	def drawHourDots(self, color, less = False):
		self.clockPen.color(color) # Set the color of the dots
		if not less: # If "less" is False, draw all 12 dots.
			for i in range(0, 12): # Draw the dot, 12 times.
				self.clockPen.forward(300) # Move to the edge of the clock face.
				self.clockPen.dot(20) # Draw the dot.
				self.clockPen.backward(300) # Move back to the center.
				self.clockPen.right(30) # Point to the next hour position.
		if less: # If "less" is True, draw only the 12, 3, 6, and 9 o'clock dots.
			for i in range(0, 4): # Draw the dot, 4 times.
				self.clockPen.forward(300) # Move to the edge of the clock face.
				self.clockPen.dot(20) # Draw the dot.
				self.clockPen.backward(300) # Move back to the center.
				self.clockPen.right(90) # Point to the next hour position.

	# The function below is used to draw the hour indicators (number style).
	# The "color" argument is the color of the number. When the "less" argument
	# is True the function will only draw the 12, 3, 6, and 9 o'clock numbers.
	def drawHourNumbers(self, color, less = False):
		self.clockPen.color(color) # Set the color of the dots
		self.clockPen.setheading(270) # Face 6 o'clock.
		self.clockPen.forward(25) # Shifts the text down 25px to make it centered.
		self.clockPen.setheading(90) # Face 12 o'clock.
		if not less: # If "less" is False, draw all 12 numbers.
			self.clockPen.right(30) # Face 1 o'clock.
			currentNumber = 1 # Store the time to keep track of what was written.
			for i in range(0, 12): # Draw the numbers for each hour.
				self.clockPen.forward(300) # Move to the edge of the clock face.
				self.clockPen.write(currentNumber, align='center',
									font=('Avenir Next', 36, 'normal')) # Write
									# the number.
				self.clockPen.backward(300) # Move back to the center.
				self.clockPen.right(30) # Point to the next hour position.
				currentNumber += 1 # Increment the time.
		if less: # If "less" is True, draw only 12, 3, 6, and 9 o'clock numbers.
			self.clockPen.right(90) # Face to 3 o'clock.
			currentNumber = 3 # Store the time to keep track of what was written.
			for i in range(0, 4): # Draw the 4 numbers
				self.clockPen.forward(300) # Move to the edge of the clock face.
				self.clockPen.write(currentNumber, align='center',
									font=('Avenir Next', 36, 'normal')) # Write
									# the number.
				self.clockPen.backward(300) # Move back to the center.
				self.clockPen.right(90) # Point to the next hour position.
				currentNumber += 3 # Increment the time.
		self.clockPen.home() # Return to the center of the clock.

	# The function below is used to draw the hour indicators (numeral style).
	# The "color" argument is the color of the numeral. When the "less" argument
	# is True the function will only draw the 12, 3, 6, and 9 o'clock numeral.
	def drawHourNumerals(self, color, less = False):
		self.clockPen.color(color) # Set the color of the dots
		self.clockPen.setheading(270) # Face 6 o'clock.
		self.clockPen.forward(20) # Shifts the text down 20px to make it centered.
		self.clockPen.setheading(90) # Face 3 o'clock.
		currentNumeral = 0 # Store the current index of the numeral
		if not less: # If "less" is False, draw all 12 numerals.
			self.clockPen.right(30) # Face 1 o'clock.
			numerals = ['I', 'II', 'III', 'IV',
						'V', 'VI', 'VII', 'VIII',
						'IX', 'X', 'XI', 'XII'] # Store the 12 numerals
			for i in range(0, 12): # Draw the numerals for each hour.
				self.clockPen.forward(300) # Move to the edge of the clock face.
				self.clockPen.write(numerals[currentNumeral], align='center',
									font=('Times New Roman', 36, 'normal'))
									# Write the numeral.
				self.clockPen.backward(300) # Move back to the center.
				self.clockPen.right(30) # Point to the next hour position.
				currentNumeral += 1 # Increment the index.
		if less: # If "less" is True, draw only 12, 3, 6, and 9 o'clock numbers.
			self.clockPen.right(90) # Face to 3 o'clock.
			numerals = ['III', 'VI', 'IX', 'XII'] # Store the 4 numerals
			for i in range(0, 4): # Draw the 4 numerals
				self.clockPen.forward(300) # Move to the edge of the clock face.
				self.clockPen.write(numerals[currentNumeral], align='center',
									font=('Times New Roman', 36, 'normal'))
									# Write the numeral.
				self.clockPen.backward(300) # Move back to the center.
				self.clockPen.right(90) # Point to the next hour position.
				currentNumeral += 1 # Increment the index
		self.clockPen.home() # Return to the center of the clock.

	# The function below is used to draw the minute/second indicators.
	# The "size" argument sets the size of the dots. The "color" argument
	# sets the color of the dots.
	def minuteDots(self, size, color):
		self.clockPen.color(color) # Set the color of the dot
		self.clockPen.right(6) # Skip over the 12 o'clock indicator.
		for i in range(0, 12): # Draw all 12 sections of 4 dots.
			for i in range(0, 4): # Draw the 4 dots that make up a section.
				self.clockPen.forward(300) # Move to the outside of the clock.
				self.clockPen.dot(size) # Draw the dot.
				self.clockPen.backward(300) # Move to the center.
				self.clockPen.right(6) # Move to the next indicator position.
			self.clockPen.right(6) # Skip over the hour indicator.

	# The function below draws the clock face and then draws the clock hands.
	# This function is the only function that needs to be called from the file
	# running it. "mainloop" takes no arguments from the user.
	def mainloop(self):
		try: # Try to run the program, exit if ^c is pressed.
			self.clockPen.setheading(90) # Face 12 o'clock.

			# Check the clock style then draw the clock face.
			# Draw the simple face.
			if self.style == 'simple':
				self.drawHourDots(self.hourDotColor) # Draw the dots.
				self.minuteDots(10, self.minuteSecondDotColor) # Draw the minute/second dots.
			# Draw the simple minimal face.
			elif self.style == 'minimal':
				self.drawHourDots(self.hourDotColor, True) # Draw the 4 dots.
			# Draw the simple clean face.
			elif self.style == 'clean':
				self.drawHourDots(self.hourDotColor) # Draw the dots.
			# Draw the modern face.
			elif self.style == 'modern':
				self.drawHourNumbers(self.hourDotColor) # Draw the numbers.
				self.clockPen.left(90) # Face 12 o'clock.
				self.minuteDots(10, self.minuteSecondDotColor) # Draw the minute/second dots.
			# Draw the modern minimal face.
			elif self.style == 'minimal-modern':
				self.drawHourNumbers(self.hourDotColor, True) # Draw the 4 numbers.
			# Draw the modern clean face.
			elif self.style == 'clean-modern':
				self.drawHourNumbers(self.hourDotColor) # Draw the numbers.
			# Draw the classic face.
			elif self.style == 'classic':
				self.drawHourNumerals(self.hourDotColor) # Draw the numerals
				self.clockPen.left(90)
				self.minuteDots(5, self.minuteSecondDotColor) # Draw the minute/second dots.
			# Draw the classic minimal face.
			elif self.style == 'minimal-classic':
				self.drawHourNumerals(self.hourDotColor, True) # Draw the 4 numerals
			# Draw the classic clean face.
			elif self.style == 'clean-classic':
				self.drawHourNumerals(self.hourDotColor) # Draw the numerals.
			# If nothing matches or no style was given, draw the simple face.
			else:
				print('No style called "%s"' % self.style) # Print the error.
				print('Defaulting to "simple"') # Alert action
				self.drawHourDots(self.hourDotColor) # Draw the dots
				self.minuteDots(10, self.minuteSecondDotColor) # Draw the
															   # minute/second
															   # dots.

			# Face 12 o'clock.
			self.clockPen.setheading(90)

			# Store the current time to use to set the
			# clock's initial hand position.
			currentTime = datetime.datetime.now() # Store the current time object.
			currentHour = currentTime.hour # Store the current hour.
			currentMinute = currentTime.minute # Store the current minute.
			currentSecond = currentTime.second # Store the current second.

			# Draw the hands' initial position.
			# Draw the hour hand.
			self.drawHourHand(currentHour, currentMinute, self.hourHandColor,
							  self.hourHandThickness, self.hourHandLength)
			# Draw the minute hand.
			self.drawMinuteHand(currentMinute, self.minuteHandColor,
								self.minuteHandThickness, self.minuteHandLength)
			# Draw the second hand.
			self.drawSecondHand(currentSecond, self.secondHandColor,
								self.secondHandThickness, self.secondHandLength)

			# Update the clock every second.
			while True:
				time.sleep(1) # Wait a second

				# Keep the time updated
				currentTime = datetime.datetime.now() # Store the current time object.
				currentHour = currentTime.hour # Store the current hour.
				currentMinute = currentTime.minute # Store the current minute.
				currentSecond = currentTime.second # Store the current second.

				# Draw the second hand.
				self.drawSecondHand(currentSecond, self.secondHandColor,
									self.secondHandThickness,
									self.secondHandLength)

				# Check if the minute has updated
				if currentSecond == 0:
					self.minutePen.clear() # Clear the minute hand.
					if currentMinute == 59: # If incrementing will create
											# a non real time, reset to 0.
						currentMinute = 0 # Reset the current minute to 0.
					else: # If it wont, increment.
						currentMinute += 1 # Increment the minute.

					# Draw the minute hand.
					self.drawMinuteHand(currentMinute, self.minuteHandColor,
										self.minuteHandThickness,
										self.minuteHandLength)

					# Draw the hour hand.
					self.drawHourHand(currentHour, currentMinute,
									  self.hourHandColor,
									  self.hourHandThickness,
									  self.hourHandLength)

					# Check if the hour has updated.
					if currentMinute == 0:
						if currentHour == 24: # If incrementing will create
											  # a non real time, reset to 0.
							currentHour = 1 # Reset the hour.
						else: # If it wont, increment.
							currentHour += 1 # Increment the hour.

		# If ^c is pressed, exit the program.
		except KeyboardInterrupt:
			exit() # Exit
