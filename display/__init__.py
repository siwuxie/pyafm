import sys
sys.path.append(r'/home/livincent/workspace/pyafm')

from threading import Thread
import time

from display import displayMange as dm
from data import pipeman,datapipe
import curses

class displayThread(Thread, dm):
    def __init__(self, pipe, cols, rows, namelist, stopq):
        Thread.__init__(self)
        screen = curses.initscr()
        maxy, maxx = screen.getmaxyx()
        dm.__init__(self, screen, maxx, maxy, namelist, cols, rows)

        self.screen = screen
        self.stopq = stopq

        assert isinstance(pipe, datapipe)

        self.pipe = pipe
        screen.nodelay(1)

        curses.nocbreak()
        curses.curs_set(0)
        curses.noecho()

    def updateContent(self):
        newcontent = self.pipe.reciving()
        if newcontent is not None:
            self.updateStatus(newcontent[0], newcontent[1])

    def run(self):
        self.content_display()
        while True:
            self.updateContent()
            k = self.screen.getch()

            if k == ord('q'):
                self.stopq.sendstop()
                break
            elif k == ord('c'):
                msg = self.getinput_display()
                self.pipe.sending(msg)
                self.content_display()


if __name__ == "__main__":
    import curses
    # from Queue import Queue
    content = [ \
        ['Device Specification', 'Horizontal AFM'],
        ['Version', "0.4.1"],
        ['Author', 'Liwen Zhang'],
        ['Email', 'LiVincentZhang@gmail.com'],
        ['Time', 1123],
        ]
    status_content = [ \
        ["Task Number", "No Count"],
        ["Runing Task", "TaskName"],
        ["Mod Number", "No Count"],
        ['Time', 1],
        ]
    namelist = ['logo', 'motor', 'a', 'b']
    pipx, pipy = pipeman(100).getPipe()

    th = displayThread(pipx, 2, 2, namelist)
    th.start()
    pipy.sending(('logo', content))
    for item in range(0, 100):
        time.sleep(0.01)
        status_content[3][1] = item
        content[4][1] = item
        pipy.sending(('motor', status_content))
        pipy.sending(('logo', content))
    th.join()
    curses.endwin()


