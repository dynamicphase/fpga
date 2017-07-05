class verilog_wrapper(object):
    def __init__(self, file_name, topfile):
        self.file_name = file_name
        self.topfile = topfile

    def create_wrapper_port(self, n, need_dir, end):
        if end == True:
            self.f.write('    ' + n + ',\n')
            if need_dir == True:
                self.f.write('    ' + n + '_dir\n')
        else:
            self.f.write('    ' + n + ',\n')
            if need_dir == True:
                self.f.write('    ' + n + '_dir,\n')

    def write_wrapper_ports(self):
        self.f.write('module  ' + self.topfile.module_name + '_wrapper(\n')
        if self.topfile.input_pins:
            for i, n in enumerate(self.topfile.input_pins):
                if i == (len(self.topfile.input_pins) - 1) and len(self.topfile.output_pins) == 0 and len(self.topfile.inout_pins) == 0:
                    self.create_wrapper_port(n, True, True)
                else:
                    self.create_wrapper_port(n, True, False)
        if self.topfile.output_pins:
            for i, n in enumerate(self.topfile.output_pins):
                if i == (len(self.topfile.output_pins) - 1) and len(self.topfile.inout_pins) == 0:
                    self.create_wrapper_port(n, True, True)
                else:
                    self.create_wrapper_port(n, True, False)
        if self.topfile.inout_pins:
            for i, n in enumerate(self.topfile.inout_pins):
                if i != (len(self.topfile.inout_pins) - 1):
                    self.create_wrapper_port(n, False, True)
                else:
                    self.create_wrapper_port(n, False, False)
        self.f.write('    );\n')

    def write_pins_dir(self, dir):
        self.f.write('inout ')
        for i, n in enumerate(dir):
            if i != (len(dir) - 1):
                self.f.write(n + ', ')
            else:
                self.f.write(n + ';\n')

    def write_dir_pins_dir(self, dir):
        self.f.write('output ')
        for i, n in enumerate(dir):
            if i != (len(dir) - 1):
                self.f.write(n + '_dir, ')
            else:
                self.f.write(n + '_dir;\n\n')

    def write_assign_dir(self, dir, bin):
        bin_dict = {1: '1b\'1', 0: '1b\'0'}
        for n in dir:
            self.f.write('assign ' + n + '_dir = ' + bin_dict[bin] + ';\n')

    def connect_port(self, ports, pins):
        for i, n in enumerate(ports):
            self.f.write('    .' + n + '(' + pins[i] + '),\n')

    def create_module_instance(self):
        self.f.write(self.topfile.module_name + '    ' + self.topfile.module_name + '_inst(\n')
        self.connect_port(self.topfile.input_ports, self.topfile.input_pins)
        self.connect_port(self.topfile.output_ports, self.topfile.output_pins)
        self.connect_port(self.topfile.inout_ports, self.topfile.inout_pins)
        self.f.write('    );\n')
        self.f.write('\n')

    def create_new_file(self):

        self.f = open(self.file_name, 'w+')

        # Write wrapper ports extracted from top level pins
        self.write_wrapper_ports()
        self.f.write('\n')

        # Give wrapper ports (including direction port) direction
        if self.topfile.input_pins:
            self.f.write("//Inputs\n")
            self.write_pins_dir(self.topfile.input_pins)
            self.write_dir_pins_dir(self.topfile.input_pins)
        if self.topfile.output_pins:
            self.f.write('//Outputs\n')
            self.write_pins_dir(self.topfile.output_pins)
            self.write_dir_pins_dir(self.topfile.output_pins)
        if self.topfile.inout_pins:
            self.f.write('//Inouts\n')
            self.write_pins_dir(self.topfile.inout_pins)
            # TBD: Need to handle searching for dir pins in top level
        self.f.write('\n')

        # Write 1 or 0 to wrapper port inputs and outputs
        if self.topfile.input_pins:
            # assign direction pins inputs to 1b'1
            self.write_assign_dir(self.topfile.input_pins, 1)
        if self.topfile.output_pins:
            # assign direction pins outputs to 1b'0
            self.write_assign_dir(self.topfile.output_pins, 0)
        self.f.write('\n')

        # Insantiate top verilog file
        self.create_module_instance()

        # Close out the wrapper module
        self.f.write('endmodule')
