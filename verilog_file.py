import re

class verilog_file(object):
    module_name = ''
    input_ports = []
    input_pins = []

    def __init__(self, filename):
        self.filename = filename

    def get_module_name(self):
        regex = re.compile('.*module\s+(.\w*)')
        matched = re.search(regex, self.file)
        if matched:
            self.module_name = matched.group(1)
            print "Module name: %s" %self.module_name

    def find(self, regex):
        items = []
        matched = re.findall(regex, self.file)
        for each in matched:
            temp = re.sub(r'\s', '', each)
            items = items + re.split(r',', temp)
        return items

    def extract_ports(self, dir):
        ports = []
        regex = re.compile(dir + ' (.*);')
        ports = self.find(regex)
        if ports:
            print 'Found %d %s port(s):' % (len(ports), dir)
        else:
            print "No %s ports found." % (dir)
        return ports

    def extract_pins(self, dir):
        pins = []
        regex = re.compile('[$]' + dir + ' (.*)[$]')
        pins = self.find(regex)
        if pins:
            print 'Found %d %s pins(s):' % (len(pins), dir)
        else:
            print "No %s pins found." % (dir)
        return pins

    def extract_info(self):
        self.source =  open(self.filename, 'r')
        self.file = self.source.read().decode('utf8')
        self.get_module_name()
        #get ports
        self.input_ports = self.extract_ports('input')
        self.output_ports = self.extract_ports('output')
        self.inout_ports = self.extract_ports('inout')
        #get pins
        self.input_pins = self.extract_pins('input')
        self.output_pins = self.extract_pins('output')
        self.inout_pins = self.extract_pins('inout')
        # Note: if inout, will need to find the direction pin. Maybe require a naming convention?



