from threading import Thread
from Queue import Queue
from afmserial import msg_handler,msg_gen
from cmdstru.definition import modelist,modedict

class datathread(Thread, msg_handler):

	def __init__(self, commName, commBrate):
		Thread.__init__(self)
		msg_handler.__init__(self, commName, commBrate)

		self.sendQ = Queue(maxsize = 20)
		self.stopQ = Queue(maxsize = 1)

		self.msgbuilder = msg_gen(modelist)
		self.last_content = ''
		self.modedict = modedict


	def stoploop(self):
		self.stopQ.put(True)

	def cmdrequire(self):
		cmd, self.last_content = self.msgbuilder.generator()
		self.sendQ.put(cmd)

	def msgsendout(self):
		if not self.sendQ.empty():
			return self.sendQ.get()
		return None

	def msgdeliver(self, msg):
		self.last_content = msg
		modedict[msg[0]+msg[1]].dispatch(msg)

	def run(self):

		self.openSerial()

		while True:
			if not self.stopQ.empty():
				print("The loop is stoped")
				break
			self.serialReadandSend()
			pass



if __name__ =="__main__":
	a = datathread(1, '/dev/ttyUSB0', 112500)
	a.start()
	a.join()
