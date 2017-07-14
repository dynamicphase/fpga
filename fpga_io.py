import re

class fpga_io(object):

    pins = [] #All pins for every object

    def __init__(self, name):
        self.name = name

    def parse_pins(self, file, regex):
        pin_list = []
        matched = re.findall(regex, file)
        if matched:
            temp = re.sub(r'\s', '', matched[0])
            pin_list = pin_list + re.split(r',', temp)
            return pin_list
        else:
            return False

    def extract_pins(self, v_file, port_name):
        regex = re.compile(r'\$pin\s*' + port_name + '\s*:(.*)\$')
        found_pins = self.parse_pins(v_file, regex)
        for each in found_pins:
            self.pins.append(each)
        if found_pins == False:
            print "Error: No pins found for port \"%s\"." % (port_name)
        return found_pins

