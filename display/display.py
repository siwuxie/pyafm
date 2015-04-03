import sys,os
import curses
from threading import Thread

class display():
	"""docstring for display"""
	def __init__(self, screen, content, input_content, x, y):
		Thread.__init__(self)

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

	def updateContent(self, newcontent):
		self.content = newcontent
		self.lines = len(self.content)
		pass
