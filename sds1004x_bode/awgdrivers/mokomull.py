import serial

from base_awg import BaseAWG

class MOKOMULL(BaseAWG):
    SHORT_NAME = "mokomull"

    def __init__(self, port, baudrate):
        self.port = port

    def initialize(self):
        self.ser = serial.Serial(self.port)

    def get_id(self):
        pass

    def enable_output(self, channel, on):
        pass

    def set_phase(self, phase):
        pass

    def set_wave_type(self, channel, wave_type):
        pass
    
    def set_amplitue(self, channel, amplitude):
        send = amplitude * 1000
        print "setting amplitude to %d" % send
        self.ser.write("v%d\n" % send)
    
    def set_offset(self, channel, offset):
        pass
    
    def set_load_impedance(self, channel, z):
        pass
        
    def set_frequency(self, channel, freq):
        print "sending %d" % freq
        self.ser.write("f%d\n" % freq)
