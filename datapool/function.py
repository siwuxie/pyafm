__author__ = 'livincent'


def CMDclean(cmd):
    result = ''
    for item in (cmd[2*i+1]+cmd[2*i] for i in range(0, 5)):
        result += item
    return result
