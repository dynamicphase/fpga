import re
from file_ports import file_ports

class verilog_file(object):

    def __init__(self, filename):
        self.module_name = ''
        self.filename = filename
        self.input_ports = file_ports('input')
        self.output_ports = file_ports('output')
        self.inout_ports = file_ports('inout')

    def get_module_name(self):
        regex = re.compile(r'.*module(.\w*)\b\(')
        matched = re.search(regex, self.file)
        if matched:
            self.module_name = matched.group(1)
            print "Module name: %s" %self.module_name

    def extract_info(self):
        self.source =  open(self.filename, 'r')
        self.file = self.source.read().decode('utf8')
        self.get_module_name()

        # get input ports/pins
        self.input_ports.extract_ports(self.file)

        # get output ports/pins
        self.output_ports.extract_ports(self.file)

        # get inout ports/pins
        self.inout_ports.extract_ports(self.file)
        # Note: if inout, will need to find the direction pin. Maybe require a naming convention?



