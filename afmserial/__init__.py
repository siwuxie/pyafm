import serial 

class msg_resive:
    def __init__(self, name, brate):
        self.name = name
        self.brate = brate
        self.com = None        
        pass
    
    def openSerial(self):
        if self.com.isOpen():
            self.com.close()
            self.com = serial.Serial(self.name, self.brate)
        self.com.open()
        
    def closeSerial(self):
        self.com.close()
    
    def msgdeliver(self, msg):
        pass
    
    def serialRead(self):
        while 1:
            msg = self.read(10)
            self.msgdeliver(msg)
            print(msg)
            
        