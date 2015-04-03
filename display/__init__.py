from display import display
from threading import Thread

class fixlogo_display(display):
	"""docstring for fixlogo_display"""
	def __init__(self, screen, content, input_content, x, y):
		display.__init__(self, screen, content, input_content, x, y)
		
	def getInput(self):
		pass

class SystemStatus_display(display):

	def __init__(self, screen, content, input_content, x, y):
		display.__init__(self, screen, content, input_content, x, y)
		pass

	def updateStatus(self, status):
		self.content = status

	def getInput(self):
		pass

class Input_display(display):
	"""docstring for Input_display"""
	def __init__(self, screen, content, input_content, x, y):
		display.__init__(self, screen, content, input_content, x, y)
		
Display_class = {
	'logo': fixlogo_display,
	'status': SystemStatus_display,
	'input': Input_display,
}

class displayThread(display, Thread):
	
	def __init__(self, screen, content, input_content, x, y, sendQ, reciveQ, screenlock):
		display.__init__(self, screen, content, input_content, x, y)
		Thread.__init__(self)
		
		self.screenlock = screenlock
		self.sendQ = sendQ
		self.reciveQ = reciveQ
		
	def updateContent(self):
		if not self.reciveQ.empty():
			newcontent = self.reciveQ.get()
			display.updateContent(newcontent)

	def run():
		while True:
			screenlock.acquire(blocking = True)
			self.updateContent()
			self.displayContent()
			screenlock.release()


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

