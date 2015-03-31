from msg_stru import msg

class cmd_stru(msg):

	def __init__(self, p1, p2,p3,p4,p5):
		self.msg(p1,p2,p3,p4,p5) 
		self.cmddict = {
			'head':self.msglist[0],
			'word':self.msglist[1],
			'p1':self.msglist[2],
			'p2':self.msglist[3],
			'p3':self.msglist[4],
			}
	def cmddict(self):
		return self.cmddict

class data_stru(msg):

	def __init__(self, p1, p2, p3, p4, p5):
		self.msg(p1,p2,p3,p4,p5)
		self.cmddict = {
			'head':self.msglist[0],
			'd1':self.msglist[1],
			'd2':self.msglist[2],
			'd3':self.msglist[3],
			'd4':self.msglist[4],
		}
	def datadict(self):
		return self.cmddict