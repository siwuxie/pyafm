import data
import function as fc

init_content = [
    ['pid_run', 'disable'],
    ['P_gain', '0'],
    ['I_gain', '0'],
    ['D_gain', '0'],
    ['Set_point', '0'],
    ['Z', '0'],
    ['Error', '0']
 ]

pidCmdDict = {
    'pid': '\x00\x10',
    'pid_run': '\x00',
    'set_P': '\x01',
    'set_I': '\x02',
    'set_D': '\x03',
    'Set_point': '\x05',
    'Err_report': '\x06',
    'Z_report': '\x07',
}

class pid_data(data.moduletype):
    def __init__(self, name, cmddicts):
        data.moduletype.__init__(self, name, cmddicts)
        self.display_content = init_content

    def work_cmd(self, cmd):
        if len(cmd) != 10:
            raise ValueError("The lenth of the data is incorrect")

        cmd = fc.CMDclean(cmd)

        pid_data= int((cmd[4:6]).encode('hex'),16)
        self.display_content[0][1] = 'enable'

        if pid_data==1:
            pid_run = int((cmd[9:10]).encode('hex'), 16)

            if pid_run ==1:
                    P_gain = int((cmd[6:7]).encode('hex'), 16)
                    I_gain = int((cmd[7:8]).encode('hex'), 16)
                    D_gain = int((cmd[8:9]).encode('hex'), 16)
                    self.display_content[1][1] =P_gain
                    self.display_content[2][1] =I_gain
                    self.display_content[3][1] =D_gain
            elif pid_run ==0:
                    self.display_content[0][1] = 'disable'

        elif pid_data == 2:
                Set_point = int((cmd[6:8]).encode('hex'), 16)
                Z =int((cmd[8:10]).encode('hex'),16)
                self.display_content[4][1] =Set_point
                self.display_content[6][1] =Z
        elif pid_data ==3:
                Error= int((cmd[6:10]).encode('hex'),16)
                self.display_content[5][1] =Error
        self.is_newcontent = True


config_dict = {
    'pid':{
       'head':pidCmdDict['pid'] ,
       'name':'pid',
       'data':pid_data('pid',pidCmdDict)
    }
}
