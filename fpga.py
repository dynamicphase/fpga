from fpga_pin import fpga_pin

class fpga(object):

    pins = ['pin1','pin2','pin3','pin4','pin5','pin6','pin7','pin8','pin9','pin10']

    def __init__(self, filename):
        self.filename = filename

    def generate_pins(self):
        for n in self.pins:
            self.n = fpga_pin(n, 'in') #input pin by default
        print self.pin1

