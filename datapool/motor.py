import data


init_content = [
    ['Direction', '+'],
    ['Steps', 0],
    ['Position', 0],
    ['Status', 'Stop']
]

motorCmdDict = {
    'motor': '\x00\x02',
    'move': '\x00',
    'set_origin': '\x00',
    'auto_forward': '\x01',
    'auto_backward': '\x02',
    'stop': '\x03',
    'step_forward': '\x04',
    'step_backward': '\x05',
    'originate': '\x06',
}


class motor_data(data.moduletype):
    def __init__(self, name, cmddicts):
        data.moduletype.__init__(self, name, cmddicts)
        self.display_content = init_content

    def work_cmd(self, cmd):
        if len(cmd) != 10:
            raise ValueError("The lenth of the data is incorrect")

        direction = int(cmd[4:6].encode('hex'), 16)
        steps = int(cmd[6:8].encode('hex'), 16)
        motorsta = int(cmd[8:10].encode('hex'), 16)

        if direction == 1:
            self.display_content[0][1] = '+'
            self.display_content[2][1] += steps
        else:
            self.display_content[0][1] = '-'
            self.display_content[2][1] -= steps

        self.display_content[1][1] = steps

        if motorsta == 1:
            self.display_content[3][1] = 'Moving'
        elif motorsta == 0:
            self.display_content[3][1] = 'Stopping'

        self.is_newcontent = True











