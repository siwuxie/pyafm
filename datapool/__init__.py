from threading import Thread

import motor
import data


# class manger_pipes:
#
# def __init__(self, serialmax, displaymax):
# self.data2serial = data.datapipe(serialmax, serialmax)
#         self.data2display = data.datapipe(displaymax, displaymax)
#
#


class dataThread(Thread):
    def __init__(self, data2serial, data2display):

        assert isinstance(data2serial, data.datapipe)
        assert isinstance(data2display, data.datapipe)

        self.d2s = data2serial
        self.d2d = data2display

        self.motor = motor.motor_data('motor', motor.motorCmdDict)

    def run(self):
        while True:
            if self.motor.is_newcontent:
                self.d2d.sending(self.motor.get_dispcontent())

            recive_disp = self.d2d.reciving()
            if recive_disp is not None:
                cmd = self.motor.cmdgenerator(recive_disp)
                self.d2s.sending(cmd)

            recive_serial = self.d2s.reciving()
            if recive_serial is not None:
                self.motor.work_cmd(recive_serial)


if __name__ == "__main__":