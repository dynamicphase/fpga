class verilog_wrapper(object):
    def __init__(self, file_name, module_name, input_ports, output_ports, inout_ports, input_pins, output_pins, inout_pins):
        self.file_name = file_name
        self.module_name = module_name
        self.input_ports = input_ports
        self.output_ports = output_ports
        self.inout_ports = inout_ports
        self.input_pins = input_pins
        self.output_pins = output_pins
        self.inout_pins = inout_pins

    def connect_port(self, ports, pins):
        for i,n in enumerate(ports):
            self.f.write('    .' + n + '(' + pins[i]+ '),\n' )

    def create_module_instance(self):
        self.f.write(self.module_name + '    ' + self.module_name + '_inst(\n')
        self.connect_port(self.input_ports, self.input_pins)
        self.connect_port(self.output_ports, self.output_pins)
        self.connect_port(self.inout_ports, self.inout_pins)
        self.f.write('    );\n')
        self.f.write('\n')

    def create_top_port(self, n, end):
        if end == True:
            self.f.write('    ' + n + ',\n')
            self.f.write('    ' + n + '_dir\n')
        else:
            self.f.write('    ' + n + ',\n')
            self.f.write('    ' + n + '_dir,\n')

    def declare_top_ports(self):
        self.f.write('module  ' + self.module_name + '_wrapper(\n')
        if self.input_pins:
            for i, n in enumerate(self.input_pins):
                if i == (len(self.input_pins) - 1) and len(self.output_pins) == 0 and len(self.inout_pins) == 0:
                    self.create_top_port(n, True)
                else:
                    self.create_top_port(n, False)
        if self.output_pins:
            for i, n in enumerate(self.output_pins):
                if i == (len(self.output_pins) - 1) and len(self.inout_pins) == 0:
                    self.create_top_port(n, True)
                else:
                    self.create_top_port(n, False)
        if self.inout_pins:
            for i, n in enumerate(self.inout_pins):
                if i != (len(self.inout_pins) - 1):
                    self.create_top_port(n, True)
                else:
                    self.create_top_port(n, False)
        self.f.write('    );\n')

    def set_pins_dir(self, dir):
        self.f.write('inout ')
        for i, n in enumerate(dir):
            if i != (len(dir) - 1):
                self.f.write(n + ', ')
            else:
                self.f.write(n + ';\n')

    def set_dir_pins_dir(self, dir):
        self.f.write('output ')
        for i, n in enumerate(dir):
            if i != (len(dir) - 1):
                self.f.write(n + '_dir, ')
            else:
                self.f.write(n + '_dir;\n\n')

    def assign_dir(self, dir, bin):
        bin_dict = {1 : '1b\'1', 0 : '1b\'0'}
        for n in dir:
            self.f.write('assign ' + n + '_dir = ' + bin_dict[bin] + ';\n')

    def create_new_file(self):

        self.f = open(self.file_name, 'w+')

        self.declare_top_ports()
        self.f.write('\n')

        if self.input_pins:
            self.f.write("//Inputs\n")
            self.set_pins_dir(self.input_pins)
            self.set_dir_pins_dir(self.input_pins)

        if self.output_pins:
            self.f.write('//Outputs\n')
            self.set_pins_dir(self.output_pins)
            self.set_dir_pins_dir(self.output_pins)

        if self.inout_pins:
            self.f.write('//Inouts')
            self.set_pins_dir(self.inout_pins)
            # TBD: Need to handle searching for dir pins in top level

        if self.input_pins:
            # assign direction pins inputs to 1b'1
            self.assign_dir(self.input_pins, 1)
            
        if self.output_pins:
            # assign direction pins outputs to 1b'0
            self.assign_dir(self.output_pins, 0)

        self.f.write('\n')
        self.create_module_instance()
        self.f.write('endmodule')


