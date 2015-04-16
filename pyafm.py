from datapool import dataThread
from display import displayThread
from afmserial import commThread
from data import pipeman, stoppipe
from time import sleep


class pyafm():

    def __init__(self, maxq, namelist):

        self.pip_dis2data_x, self.pip_dis2data_y = pipeman(maxq).getPipe()
        self.pip_ser2data_x, self.pip_ser2data_y = pipeman(maxq).getPipe()

        self.stoptriger = stoppipe(2)
        self.stoplist = self.stoptriger.getstops()

        self.displayT = displayThread(self.pip_dis2data_x, 2, 2, namelist, self.stoptriger)
        self.serialT = commThread('/dev/ttyUSB1', 115200, self.pip_ser2data_x, self.stoplist[0])
        self.dataT = dataThread(self.pip_ser2data_y, self.pip_dis2data_y, self.stoplist[1])

    def tstart(self):
        self.serialT.start()
        sleep(1)
        self.displayT.start()
        sleep(1)
        self.dataT.start()
        sleep(1)

    def waiting(self):
        self.displayT.join()
        self.serialT.join()
        self.dataT.join()

    def test(self):
        i = 0
        while i < 100:
            cmd = '\x00\x02\x00\x00\x00\x01\x00\x01\x00\x01'
            sleep(0.5)
            self.pip_ser2data_y.sending(cmd)
            i += 1

        while True:
            result = self.pip_ser2data_x.reciving()
            if result is not None:
                # print result.encode('hex')
                break

        self.waiting()


if __name__ == '__main__':
    test = pyafm(10000, ['motor','pid'])

    test.tstart()
    # test.test()
    test.waiting()
