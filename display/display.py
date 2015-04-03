import sys,os
import curses

class display:
	"""docstring for display"""
	def __init__(self, screen, content, input_content, x, y):
		self.content = content
		self.screen = screen
		self.input_content = input_content
		self.lines = len(self.content)
		curses.nocbreak()
		self.x = x
		self.y = y

	def displayContent(self):
		i = 0
		for item in self.content:
			self.screen.addstr(self.y+i, self.x, item[0] + str(item[1]))
			i += 1
		self.screen.refresh()

	def getInput(self):
		self.screen.addstr(self.y+self.lines, self.x, self.input_content)
		inputstr = self.screen.getstr()
		return inputstr.split(' ')

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

if __name__ == "__main__":
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
	# print(dis.getInput())