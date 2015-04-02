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

system_disp = {
	"last_command:":"None"
}

motor_status_disp = {
	"Motor Position":0,
	"Motor status":'Stop',
}

class pyafm():
	"""docstring for pyafm"""
	def __init__(self):
		self.pipe = dt.datathread('/dev/ttyUSB0', 115200)

	def fixed_display(self):
		os.system('clear')
		for item in content_disp:
			sys.stdout.write(item)

		for item in self.pipe.modedict.keys():
			for item2 in self.pipe.modedict[item].report_status.keys()
				sys.stdout.write(item2)
				sys.stdout.write(":\t\t"+str(self.pipe.modedict[item].report_status[item2]+'\n'))

		sys.stdout.write("Last command:\t\t"+str(self.pipe.last_content)+'\n')

	def status_display(self, status_disp):
		for item in status_disp.keys():
			sys.stdout.write(item)
			sys.stdout.write(':\t\t'+str(status_disp[item])+"\n")

	def waitinput(self):
		sys.stdout.write("Please enter your selection:\t")
		case = raw_input()
		if case == 'cmd':
			self.pipe.cmdrequire()
			return False
		elif case == 'exit':
			return True

	def work(self):
		self.pipe.start()
		while True:
			self.fixed_display()
			flag = self.waitinput()
			if flag:
				self.pipe.stoploop()
				break

if __name__ == "__main__":
	test = pyafm()
	test.work()

		