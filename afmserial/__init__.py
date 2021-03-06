import serial 
import sys

class msg_gen:
	def __init__(self, modullist):
		self.mods = {}
		for item in modullist:
			self.mods[item['head_name']]=item

	def _praser(self, para):
		temp = hex(int(para)).replace('0x','')
		while len(temp)<4: temp = '0'+temp
		return temp.decode('hex')

	def generator(self):
		result = ''
		msgstr = raw_input("Pleas input your mssages to AFM:\t").replace('\n','').split(' ')
		if len(msgstr) != 6:
			sys.stdout.write('Wrong Cmd!\t')
		elif len(msgstr)==6:
			temp = self.mods[msgstr[0]]
			result = temp['head']+temp['task'][msgstr[1]]+temp['cmd'][msgstr[2]]
			result += self._praser(msgstr[3])+self._praser(msgstr[4])+self._praser(msgstr[5])
			return result, msgstr
		return '', msgstr

class msg_handler:
	def __init__(self, name, brate):
		self.name = name
		self.brate = brate
		self.com = serial.Serial(self.name, self.brate)
		pass

	def openSerial(self):
		if self.com.isOpen():
			self.com.close()
			self.com = serial.Serial(self.name, self.brate)
		else:
			self.com = serial.Serial(self.name, self.brate)
			self.com.open()

	def closeSerial(self):
		self.com.close()

	def msgdeliver(self, msg):
		# print(msg)#for test only
		pass

	def msgsendout(self):

		return []#for test only
		pass

	def _getmsglist(self, raw_msg):
		count = len(raw_msg)/10
		result = [ raw_msg[10*(i-1):10*i] for i in range(1,count+1) ]
		return result
		pass

	def serialReadandSend(self):
		count = self.com.inWaiting()
		if count>=10:
			# print (count-count%10)
			msg = self.com.read(count - count%10)
			# print(msg.encode('hex'))
			msglist = self._getmsglist(msg)
			self.msgdeliver(msglist)

		msglist = self.msgsendout()
		if msglist != None: 
			a = self.com.write(msglist)
		pass



