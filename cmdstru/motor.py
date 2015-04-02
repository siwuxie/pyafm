import analysis

class Motor(analysis.msgdispatch):

	def __init__(self, args):
		analysis.msgdispatch.__init__(self, args
		self.dispcontent['Motor Position']='0'
		self.dispcontent['Motor Status']='Stop'

		self.report_status = ['Stop', 'Forward', "Backward", "Originate"]

	def dispatch(self, cmd):
		"""only report data will be sent from AFM"""

		self.dispcontent['Motor Position']+="<--->"+str(int((cmd[6]+cmd[7]).encode('hex'),16))

		temp = int((cmd[4]+cmd[5]).encode('hex'),16)
		self.dispcontent['Motor Status'] = self.report_status[temp]