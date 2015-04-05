from threading import Thread
import time

from display import displayMange as dm


class displayThread(Thread, dm):
    def __init__(self, sendQ, reciveQ, cols, rows, namelist):
        Thread.__init__(self)
        screen = curses.initscr()
        maxy, maxx = screen.getmaxyx()
        dm.__init__(self, screen, maxx, maxy, namelist, cols, rows)

        self.screen = screen
        self.sendQ = sendQ
        self.reciveQ = reciveQ
        screen.nodelay(1)

        curses.nocbreak()
        curses.curs_set(0)
        curses.noecho()

    def updateContent(self):
        if not self.reciveQ.empty():
            newcontent = self.reciveQ.get()
            self.updateStatus(newcontent[0], newcontent[1])

    def run(self):
        self.content_display()
        while True:
            self.updateContent()
            k = self.screen.getch()

            if k == ord('q'):
                break
            elif k == ord('c'):
                msg = self.getinput_display()
                sendQ.put(msg)
                self.content_display()


if __name__ == "__main__":
    import curses
    from Queue import Queue

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
    sendQ = Queue(maxsize=1000)
    reciveQ = Queue(maxsize=1000)

    th = displayThread(sendQ, reciveQ, 2, 2, namelist)
    th.start()
    reciveQ.put(('logo', content))
    for item in range(0, 100):
        time.sleep(0.01)
        status_content[3][1] = item
        content[4][1] = item
        reciveQ.put(('motor', status_content))
        reciveQ.put(('logo', content))
    th.join()
    curses.endwin()


