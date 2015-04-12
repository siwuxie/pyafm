from threading import Thread
from Queue import Queue
from cfg import config_list
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

        self.model = dict()
        self.head = dict()

        for mod in config_list:
            self.model.update(mod)

        for name in self.model.keys():
            self.head[self.model[name]['head']] = name


    def run(self):
        while True:
            for mod in self.model.keys():
                if self.model[mod]['data'].is_newcontent:
                    self.d2d.sending([self.model[mod]['name'],self.model[mod]['data'].get_dispcontent()])

            cmd_from_disp = self.d2d.reciving()
            if cmd_from_disp is not None:
                cmd = self.model[cmd_from_disp.split(' ')[0]]['data'].cmdgenerator(cmd_from_disp)
                self.d2s.sending(cmd)

            recive_serial = self.d2s.reciving()
            if recive_serial is not None:
                head_name = self.head[recive_serial[2:4][::-1]]
                self.model[head_name]['data'].work_cmd(recive_serial)

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

