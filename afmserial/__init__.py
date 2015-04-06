import sys
sys.path.append(r'/home/livincent/workspace/pyafm')

from threading import Thread
from Queue import Queue
import serial

from data import datapipe, pipeman



class transaction:
    def __init__(self, name, brate):
        self.comm_name = name
        self.comm_brate = brate

        self.com = None
        pass

    def dataSendAcquire(self):  # only for test
        print('This function should be overrided')
        return '\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10'

    def dataDispatch(self, msg):  # only for test
        print('This function should be overrided')
        print(msg)

    def openSerial(self):
        self.com = serial.Serial(self.comm_name, self.comm_brate)
        if not self.com.isOpen:
            print("Serial did not open!")

    def closeSerial(self):
        self.com.close()

    def read_send_serial(self):
        msglist = self.dataSendAcquire()
        if msglist != None:
            self.com.write(msglist)

        count = self.com.inWaiting()
        if count >= 10:
            msg = self.com.read(count - count % 10)
            self.dataDispatch(msg)


class commThread(Thread, transaction):
    def __init__(self, name, brate, pipe, stopQ):
        Thread.__init__(self)
        transaction.__init__(self, name, brate)
        self.test_count = 0

        assert isinstance(pipe, datapipe)

        self.pipe = pipe
        self.stopQ = stopQ

    def dataDispatch(self, msg):
        # self.reciveQ.put(msg)
        # print("recived cmd length: "+str(len(msg)) + ' and the Count is  '+str(self.test_count)+ "\t"+msg)
        # self.test_count += len(msg)
        # print(msg)
        for item in range(0, len(msg)/10):
            self.pipe.sending(msg[item:10+item])
            # print msg[item:10+item].encode('hex')+'\t\n'

    def dataSendAcquire(self):
        return self.pipe.reciving()

    def run(self):
        self.openSerial()
        self.com.flushInput()
        while True:
            self.read_send_serial()
            if not self.stopQ.empty():
                self.com.close()
                break


if __name__ == "__main__":
    from time import sleep
    pipe1x, pipe1y = pipeman(10000).getPipe()
    stopQ = Queue(maxsize=1)
    com = commThread('/dev/ttyUSB0', 115200, pipe1x, stopQ)
    com.start()
    i=0
    count = 0
    while i<50:
        a = '12345678901234567890'
        print("length = "+str(count))
        pipe1y.sending(a)
        count += len(a)
        i += 1
        sleep(0.01)
    sleep(1)
    stopQ.put('')

