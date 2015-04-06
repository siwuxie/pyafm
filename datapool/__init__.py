from threading import Thread
from Queue import Queue

import motor
import data


class dataThread(Thread):
    def __init__(self, data2serial, data2display, stoptriger):
        Thread.__init__(self)
        assert isinstance(data2serial, data.datapipe)
        assert isinstance(data2display, data.datapipe)
        assert isinstance(stoptriger, Queue)

        self.d2s = data2serial
        self.d2d = data2display
        self.stoptriger = stoptriger

        self.motor = motor.motor_data('motor', motor.motorCmdDict)

    def run(self):
        while True:
            if self.motor.is_newcontent:
                self.d2d.sending(['motor',self.motor.get_dispcontent()])

            recive_disp = self.d2d.reciving()
            if recive_disp is not None:
                cmd = self.motor.cmdgenerator(recive_disp)
                self.d2s.sending(cmd)

            recive_serial = self.d2s.reciving()
            if recive_serial is not None:
                self.motor.work_cmd(recive_serial)

            if not self.stoptriger.empty():
                break


if __name__ == "__main__":

    pipe1 = data.pipeman(100)
    pipe2 = data.pipeman(100)

    dp1x, dp1y = pipe1.getPipe()
    dp2x, dp2y = pipe2.getPipe()
    stopq = Queue()

    dt = dataThread(dp1x, dp2x, stopq)
    dt.start()

    import time
    while True:
        time.sleep(0.5)
        temp = dp2y.reciving()
        print(temp)
        cmd = 'motor move set_origin 1 2 3'
        dp2y.sending(cmd)
        time.sleep(0.5)
        temp = dp1y.reciving()
        print(temp)
        cmd = '\x00\x02\x00\x00\x00\x05\x00\x08\x00\x01'
        dp1y.sending(cmd)

    dt.join()

