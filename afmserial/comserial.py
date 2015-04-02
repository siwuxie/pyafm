import serial
from threading import Thread
from Queue import Queue
class transaction:

	def __init__(self, name, brate):
		self.comm_name = name
		self.comm_brate = brate

		self.com = None
		pass

	def dataSendaAcquire(self): #only for test
		print('This function should be overrided')
		return '\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10'

	def dataDispatch(self,msg): #only for test
		print('This function should be overrided')
		print(msg)

	def openSerial(self):
		self.com = serial.Serial(self.comm_name, self.comm_brate)
		if not self.com.isOpen:
			print("Serial did not open!")

	def closeSerial(self):
		self.com.close()

	def read_send_serial(self):
		msglist = self.dataSendaAcquire()
		if msglist != None: 
			self.com.write(msglist)
		for i in range(0,1000000): pass
		count = self.com.inWaiting()
		if count>=10:
			msg = self.com.read(count - count%10)
			self.dataDispatch(msg)




class commThread(Thread, transaction):

	def __init__(self, name, brate, sendQ, reciveQ, StopQ):
		Thread.__init__(self)
		transaction.__init__(self, name, brate)

		self.sendQ = sendQ
		self.reciveQ = reciveQ
		self.stopQ = stopQ

	def dataDispatch(self, msg):
		#self.reciveQ.put(msg)
		print(len(msg))
		print(msg)


	def dataSendaAcquire(self):
		if not self.sendQ.empty():
			return self.sendQ.get()
		return None

	def run(self):
		self.openSerial()
		while True:
			self.read_send_serial()
			if not self.stopQ.empty():
				self.com.close()
				break

if __name__ == "__main__":
	sendQ = Queue(maxsize=20)
	reciveQ = Queue(maxsize = 100)
	stopQ = Queue(maxsize = 1)
	com = commThread('/dev/ttyUSB0', 115200, sendQ, reciveQ, stopQ)
	com.start()

	a = 'Hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n'
	print(len(a))
	sendQ.put(a)
	stopQ.put('')

