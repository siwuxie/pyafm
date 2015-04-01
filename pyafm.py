import datathread as dt
import afmserial
import cmdstru

import os,sys

content_disp = \
	[
		"Atomic\tForce\tMicroscopy\n",
		"LiVincent.Zhang\tLiVincentzhang@gmail.com\n"
		"----------------------------------------------\n",
		"Status of AFM\n"
		"----------------------------------------------\n",
	]

motor_status_disp = {
	"Motor Position":0,
	"Motor status":'Stop',
}

class pyafm():
	"""docstring for pyafm"""
	def __init__(self):
		self.pipe = dt.datathread('', 115200)

	def fixed_display(self):
		os.system('clear')
		for item in content_disp:
			sys.stdout.write(item)
		self.status_display(motor_status_disp)

	def status_display(self, status_disp):
		for item in status_disp.keys():
			sys.stdout.write(item)
			sys.stdout.write(':\t\t'+str(status_disp[item])+"\n")

	def waitinput(self):
		case = raw_input('Please enter your selection:\t')
		if case == 'cmd':
			self.pipe.cmdrequire()
			return False
		elif case == 'exit':
			return True

	def work(self):
		self.pipe.run()

		while True:
			self.fixed_display()
			flat = waitinput()
			if flat:
				break


if __name__ == "__main__":
	test = pyafm()
	test.fixed_display()

		