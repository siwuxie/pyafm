import curses


class display_areas():
    def __init__(self, screen, starty, startx, name):
        self.maxy, self.maxx = screen.getmaxyx()
        self.screen = screen
        self.name = name
        self.win_status = self.screen.subwin(self.maxy, self.maxx / 2, starty, startx)
        self.win_values = self.screen.subwin(self.maxy, self.maxx / 2, starty, startx + self.maxx / 2)
        self.content = []

    def print_status(self):
        x, y = 1, 2
        self.screen.border()
        self.screen.addstr(1, 1, "Status of " + str(self.name), curses.A_BOLD + curses.A_UNDERLINE)
        for item in self.content:
            self.win_status.addstr(y, x, str(item[0]))
            self.win_values.addstr(y, x, str(item[1]) + ' ' * (2))
            y += 1

        self.win_status.refresh()
        self.win_values.refresh()
        pass


class displayMange():
    def __init__(self, screen, maxx, maxy, statuslist, cols=2, rows=2):
        self.screen = screen
        curses.nocbreak()
        self.maxx = maxx
        self.maxy = maxy
        self.cols = cols
        self.rows = rows
        self.statuslist = statuslist
        self.areadict = {}

        width, height = self.maxx / cols, self.maxy / rows

        x, y = 0, 0
        for item in statuslist:
            temp = screen.subwin(height, width, y, x)
            temp.border()
            self.areadict[item] = display_areas(temp, y, x, item)

            x += width
            if x == width * cols:
                x = 0
                y += height

        self.getinput_win = screen.subwin(3, self.maxx, self.maxy - 3, 0)

    def getinput_display(self):
        curses.echo()

        self.getinput_win.clear()
        self.getinput_win.refresh()

        self.getinput_win.border()
        self.getinput_win.addstr(1, 1, "CMD:")
        result = self.getinput_win.getstr()

        self.getinput_win.clear()
        self.getinput_win.refresh()
        curses.noecho()

        return result

    def content_display(self):
        for item in self.statuslist:
            self.areadict[item].print_status()

    def single_display(self, name):
        self.areadict[name].print_status()

    def updateStatus(self, name, newstatus):
        self.areadict[name].content = newstatus
        self.single_display(name)


if __name__ == "__main__":
    def main(screen):
        statuslist = ['motor', 'tto', 'test', 'asfd']
        maxy, maxx = screen.getmaxyx()
        test = displayMange(screen, maxx, maxy, statuslist, 3, 3)
        test.updateStatus('motor', content)
        test.updateStatus('test', content)
        test.content_display()
        screen.getch()
        curses.endwin()

    content = [ \
        ['Device Specification', 'Horizontal AFM'],
        ['Version', "0.4.1"],
        ['Author', 'Liwen Zhang'],
        ['Email', 'LiVincentZhang@gmail.com'],
        ]
    curses.wrapper(main)

	
