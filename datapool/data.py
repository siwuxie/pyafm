__author__ = 'LiVincent'

from Queue import Queue

"""
datapipe generats a pipe to conmunication with other modules.
"""


class datapipe:
    def __init__(self, maxsend, maxrecive):
        self.sendq = Queue(maxsize=maxsend)
        self.reciveq = Queue(maxsize=maxrecive)

    def get_queues(self):
        return self.sendq, self.reciveq

    def reciving(self):
        if not self.reciveq.empty():
            return self.reciveq.get()
        return None

    def sending(self, data):
        self.sendq.put(data)


class moduletype:
    def __init__(self, name, cmddicts):
        """
        :param name: The name of a specific module
        :param status: a list of all the status name of the module
        :param cmddicts: a dictionary of cmd in a specific module
        """
        self.name = name
        # us = status
        self.cmddicts = cmddicts
        self.display_content = []
        self.is_newcontent = True

    def _praser(self, para):
        temp = hex(int(para)).replace('0x', '')
        temp = '0' * (4 - len(temp)) + temp
        # while len(temp) < 4: temp = '0' + temp
        return temp.decode('hex')

    def cmdgenerator(self, cmd):
        cmdl = cmd.split(' ')

        result = self.cmddicts[cmdl[0]] + self.cmddicts[cmdl[1]] + self.cmddicts[cmdl[2]]
        result += self._praser(cmdl[3]) + self._praser(cmdl[4]) + self._praser(cmdl[5])

        return result

    def work_cmd(self, cmd):
        """This function need to be overrided to deal with different cmds"""
        raise ValueError("This function should be overrided")

    def get_dispcontent(self):
        self.is_newcontent = False
        return self.display_content

        # def






