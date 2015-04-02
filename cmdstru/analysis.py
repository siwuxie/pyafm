
class msgdispatch:

	def __init__(self, args):
		self.info = args
		self.dispcontent = {}

	def exchange(cmd):
		i = 0
		result = []
		while i<len(cmd):
			result += cmd[i+1] + cmd[i]
			i += 2
		return result

	def dispatch(cmd):
		"""Used fo override"""
		print("This function need to be override")
		pass