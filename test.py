from cmdstru import definition as df
from afmserial import msg_gen

modullist = [df.motorCmdDict]
genner = msg_gen(modullist)

result = genner.generator()
print(result)
result = result.encode('hex')
print(result)
