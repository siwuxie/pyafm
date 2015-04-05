"""
Motor
"""
import motor

motorCmdDict = {
'head_name': 'motor',
'head': '\x00\x02',
'task': {
'move': '\x00',
},
'cmd': {
'set_origin': '\x00',
'auto_forward': '\x01',
'auto_backward': '\x02',
'stop': '\x03',
'step_forward': '\x04',
'step_backward': '\x05',
'originate': '\x06'
},
'report': {
'steps': '\x00',
'stop': '\x01',
'originate': '\x02',
'movement': '\x03',
},
}

"""
The modelist stru
"""
modelist = [motorCmdDict]
modedict = {
motorCmdDict['head']: motor.Motor(motorCmdDict)
}
