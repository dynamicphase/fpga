import re
from port import port
from fpga_io import fpga_io

class file_ports(object):

    dim_regex = re.compile(r'\[(\d+)\s*:\s*0+\s*\]')

    def __init__(self, name):
        self.name = name
        self.file = file
        self.ports_list = []
        self.single_ports = []
        self.multi_port_dict = {}
        self.fpga_io = fpga_io('fpga_io')

    def create_ports(self):
        for each in self.single_ports:
            pin = self.fpga_io.extract_pins(self.file,each)
            self.ports_list.append(port(each,self.name,pin[0]))
        for each in self.multi_port_dict:
            pins = self.fpga_io.extract_pins(self.file,each)
            for i in range(self.multi_port_dict[each]):
                name = each + '[' + str(i) + ']'
                self.ports_list.append(port(name,self.name,pins[i]))
        #for each in self.ports_list:
           # print 'Port Name: %s\tDirection: %s\tAssigned Pin: %s' %(each.name,each.dir,each.pin)

    def parse_single_ports(self, regex):
        matched = re.findall(regex, self.file)
        for each in matched:
            dim = re.search(self.dim_regex, each)
            if not dim:
                temp = re.sub(r'\s', '', each)
                self.single_ports = self.single_ports + re.split(r',', temp)

    def parse_multi_ports(self, regex):
        dim_items = []
        matched = re.findall(regex, self.file)
        for each in matched:
            dim = re.search(self.dim_regex, each)
            if dim:
                temp = re.sub(r'\[\d+\s*:\s*\d+\s*\]', '', each)
                temp = re.sub(r'\s', '', temp)
                dim_items = dim_items + re.split(r',', temp)
                for each in dim_items:
                    self.multi_port_dict[each] = 1 + int(dim.group(1))

    def extract_ports(self, file):
        self.file = file
        regex = re.compile(r''+ self.name + ' (.*);')
        self.parse_multi_ports(regex)
        self.parse_single_ports(regex)
        self.create_ports()
        if self.ports_list:
            print 'Found %d %s port(s):' % (len(self.ports_list), self.name)
        else:
            print "No %s ports found." % (self.name)