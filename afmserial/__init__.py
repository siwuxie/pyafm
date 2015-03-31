import serial 
import sys

class msg_gen:
	def __init__(self, modullist):
		self.mods = {}
		for item in modullist:
			self.mods[item['head_name']]=item
		print(self.mods)

	def praser(self, para):
		temp = hex(int(para)).replace('0x','')
		while len(temp)<4: temp = '0'+temp
		return temp.decode('hex')

	def  generator(self):
		while True:
			msgstr = raw_input("Pleas input your mssages to AFM:\t").replace('\n','').split(' ')
			if len(msgstr) != 6:
				sys.stdout.write('Wrong Cmd!\t')
				continue
			elif len(msgstr)==6:
				temp = self.mods[msgstr[0]]
				result = temp['head']+temp['task'][msgstr[1]]+temp['cmd'][msgstr[2]]
				result += self.praser(msgstr[3])+self.praser(msgstr[4])+self.praser(msgstr[5])
				return result

class msg_handler:
	def __init__(self, name, brate):
		self.name = name
		self.brate = brate
		self.com = None
		pass

	def openSerial(self):
		if self.com.isOpen():
			self.com.close()
			self.com = serial.Serial(self.name, self.brate)
		self.com.open()

	def closeSerial(self):
		self.com.close()

	def msgdeliver(self, msg):
		pass

	def msgsendout(self):
		pass

	def _getmsglist(self, raw_msg):
		count = len(raw_msg)/10
		result = [ raw_msg[10(i-1):10*i] for i in range(1,count+1) ]
		return result
		pass

	def serialReadandSend(self):
		while True:
			
			count = self.com.inWaiting()
			if self.com.inWaiting()>10:
				msg = self.com.read(count - count%10)
				msglist = self._getmsglist(msg)
				self.msgdeliver(msglist)
			self.msgdeliver(msg)
			print(msglist)

			
			msglist = self.sendout()
			for item in msglist:
				self.com.write(item)
		pass



