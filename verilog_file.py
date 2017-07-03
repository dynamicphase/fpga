import re

class verilog_file(object):
    module_name = ''
    def __init__(self, filename):
        self.filename = filename

    def get_module_name(self):
        regex = re.compile('.*module\s+(.\w*)')
        matched = re.search(regex, self.file)
        if matched:
            self.module_name = matched.group(1)
            print "Module name: %s" %self.module_name

    def get_ports(self):
        regex1 = re.compile('input (.*);')
        regex2 = re.compile('output (.*);')
        regex3 = re.compile('inout (.*);')
        matched1 = re.search(regex1, self.file)
        matched2 = re.search(regex2, self.file)
        matched3 = re.search(regex3, self.file)
        if matched1:
            self.input_ports = matched1.group(1)
            self.input_ports = re.sub(r'\s', '', self.input_ports)
            self.input_ports = re.split(r',',self.input_ports)
            print 'Found %d input port(s):'%len(self.input_ports)
        else:
            print "No input ports found."
            self.input_ports= []
        if matched2:
            self.output_ports = matched2.group(1)
            self.output_ports = re.sub(r'\s', '', self.output_ports)
            self.output_ports = re.split(r',',self.output_ports)
            print 'Found %d output port(s):' % len(self.output_ports)
        else:
            print "No output ports found."
            self.output_ports = []
        if matched3:
            self.inout_ports = matched3.group(1)
            self.inout_ports = re.sub(r'\s', '', self.inout_ports)
            self.inout_ports = re.split(r',', self.inout_ports)
            print 'Found %d inout port(s):' % len(self.inout_ports)
        else:
            print "No inout ports found."
            self.inout_ports = []
         #Note: if inout, will need to find the direction pin. Maybe require a naming convention?

    def get_pins(self):
        regex1 = re.compile('[$]input (.*)[$]')
        regex2 = re.compile('[$]output (.*)[$]')
        regex3 = re.compile('[$]inout (.*)[$]')
        matched1 = re.search(regex1, self.file)
        matched2 = re.search(regex2, self.file)
        matched3 = re.search(regex3, self.file)
        if matched1:
            self.input_pins = matched1.group(1)
            self.input_pins = re.sub(r'\s', '', self.input_pins)
            self.input_pins = re.split(r',',self.input_pins)
            print 'Found %d input pin(s):'%len(self.input_pins)
        else:
            print "No input pins found."
            self.input_pins = []
        if matched2:
            self.output_pins = matched2.group(1)
            self.output_pins = re.sub(r'\s', '', self.output_pins)
            self.output_pins = re.split(r',',self.output_pins)
            print 'Found %d output pin(s):' % len(self.output_pins)
        else:
            print "No output pins found."
            self.output_pins = []
        if matched3:
            self.inout_pins = matched3.group(1)
            self.inout_pins = re.sub(r'\s', '', self.inout_pins)
            self.inout_pins = re.split(r',', self.inout_pins)
            print 'Found %d inout pins(s):' % len(self.inout_pins)
        else:
            print "No inout pins found."
            self.inout_pins = []

    def open_vfile(self):
        self.source =  open(self.filename, 'r')
        self.file = self.source.read().decode('utf8')
        self.get_module_name()
        self.get_ports()
        self.get_pins()



