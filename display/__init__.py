from display import display

class fixlogo_display(display):
	"""docstring for fixlogo_display"""
	def __init__(self, screen, content, input_content, x, y):
		display.__init__(self, screen, content, input_content, x, y)
		
	def getInput(self):
		pass

class SystemStatus_display(display):

	def __init__(self, screen, content, input_content, x, y):
		display.__init__(self, screen, content, input_content, x, y)
		self.status = [('NoStatusLabel','NoStatus')]
		pass

	def updateStatus(self, status):
		self.status = status

	def getInput(self):
		pass

class Input_display(display):
	"""docstring for Input_display"""
	def __init__(self, screen, content, input_content, x, y):
		display.__init__(self, screen, content, input_content, x, y)
		


if __name__ == "__main__":
	import curses
	content = \
		[ 
		('====================',"====================="),
		('Device Specification', '\tHorizontal AFM'),
		('Version',"\t0.4.1"),
		('Author','\tLiwen Zhang'),
		('Email','\tLiVincentZhang@gmail.com'),
		('====================',"====================="),
		]
	input_content = 'No Input!'
	screen = curses.initscr()
	logo = fixlogo_display(screen, content, input_content, 0, 0)
	logo.displayContent()
	status_content = \
		[
			("Task Number\t", "No Count"),
			("Runing Task\t", "TaskName"),
			("Mod Number\t","No Count"),
		]

	status = SystemStatus_display(screen, status_content, input_content, 0, len(content))
	status.displayContent()
	
	input_content = "Please enter the cmd sent to device\t"
	inputdis = Input_display(screen, [], input_content, 0, len(content)+len(status_content))
	print(inputdis.getInput())

