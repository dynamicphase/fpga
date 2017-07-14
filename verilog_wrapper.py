class verilog_wrapper(object):
    def __init__(self, file_name, topfile):
        self.file_name = file_name
        self.topfile = topfile

    def create_wrapper_port(self, n, need_dir, end):
        if end == True:
            if need_dir == True:
                self.f.write('\t' + n + ',\n')
                self.f.write('\t' + n + '_dir\n')
            else:
                self.f.write('\t' + n + '\n')
        else:
            self.f.write('\t' + n + ',\n')
            if need_dir == True:
                self.f.write('\t' + n + '_dir,\n')

    def write_wrapper_ports(self):
        self.f.write('module  ' + self.topfile.module_name + '_wrapper(\n')
        if self.topfile.input_ports.ports_list:
            for i, port in enumerate(self.topfile.input_ports.ports_list):
                if i == (len(self.topfile.input_ports.ports_list) - 1) and len(self.topfile.output_ports.ports_list) == 0 and len(self.topfile.inout_ports.ports_list) == 0:
                    self.create_wrapper_port(port.pin, True, True)
                else:
                    self.create_wrapper_port(port.pin, True, False)
        if self.topfile.output_ports.ports_list:
            for i, port in enumerate(self.topfile.output_ports.ports_list):
                if i == (len(self.topfile.output_ports.ports_list) - 1) and len(self.topfile.inout_ports.ports_list) == 0:
                    self.create_wrapper_port(port.pin, True, True)
                else:
                    self.create_wrapper_port(port.pin, True, False)
        if self.topfile.inout_ports.ports_list:
            for i, port in enumerate(self.topfile.inout_ports.ports_list):
                if i == (len(self.topfile.inout_ports.ports_list) - 1):
                    self.create_wrapper_port(port.pin, False, True)
                else:
                    self.create_wrapper_port(port.pin, False, False)
        self.f.write('\t);\n')

    def write_pins_dir(self, dir, ports):
        self.f.write(dir + ' ')
        for i, each in enumerate(ports):
            if (i != len(ports)-1):
                self.f.write(each.pin + ', ')
            else:
                self.f.write(each.pin + ';\n')

    def write_dir_pins_dir(self, ports):
        self.f.write('output ')
        for i, each in enumerate(ports):
            if (i != len(ports)-1):
                self.f.write(each.pin + '_dir, ')
            else:
                self.f.write(each.pin + '_dir;\n\n')

    def write_assign_dir(self, port, bin):
        bin_dict = {1: '1b\'1', 0: '1b\'0'}
        for each in port:
            self.f.write('assign ' + each.pin + '_dir = ' + bin_dict[bin] + ';\n')

    def connect_ports(self):
        if self.topfile.input_ports.ports_list:
            for i, each in enumerate(self.topfile.input_ports.ports_list):
                if i == (len(self.topfile.input_ports.ports_list)-1) and len(self.topfile.output_ports.ports_list) == 0 and len(self.topfile.inout_ports.ports_list) == 0:
                    self.f.write('    .' + each.name + '(' + each.pin + ')\n')
                else:
                    self.f.write('    .' + each.name + '(' + each.pin + '),\n')
        if self.topfile.output_ports.ports_list:
            for i, each in enumerate(self.topfile.output_ports.ports_list):
                if i == (len(self.topfile.output_ports.ports_list) - 1) and len(self.topfile.inout_ports.ports_list) == 0:
                    self.f.write('    .' + each.name + '(' + each.pin + ')\n')
                else:
                    self.f.write('    .' + each.name + '(' + each.pin + '),\n')
        if self.topfile.inout_ports.ports_list:
            for i, each in enumerate(self.topfile.inout_ports.ports_list):
                if i == (len(self.topfile.inout_ports.ports_list) - 1):
                    self.f.write('    .' + each.name + '(' + each.pin + ')\n')
                else:
                    self.f.write('    .' + each.name + '(' + each.pin + '),\n')

    def create_module_instance(self):
        self.f.write(self.topfile.module_name + '    ' + self.topfile.module_name + '_inst(\n')
        self.connect_ports();
        self.f.write('    );\n')
        self.f.write('\n')

    def create_new_file(self):

        self.f = open(self.file_name, 'w+')

        # Write wrapper ports extracted from top level pins
        self.write_wrapper_ports()
        self.f.write('\n')

        # Give wrapper ports (including direction port) direction
        if self.topfile.input_ports.ports_list:
            self.f.write("//Inputs\n")
            self.write_pins_dir('input', self.topfile.input_ports.ports_list)
            self.write_dir_pins_dir(self.topfile.input_ports.ports_list)
        if self.topfile.output_ports.ports_list:
            self.f.write('//Outputs\n')
            self.write_pins_dir('output',self.topfile.output_ports.ports_list)
            self.write_dir_pins_dir(self.topfile.output_ports.ports_list)
        if self.topfile.inout_ports.ports_list:
            self.f.write('//Inouts\n')
            self.write_pins_dir('inout',self.topfile.inout_ports.ports_list)
            # TBD: Need to handle searching for dir pins in top level
        self.f.write('\n')

        # Write 1 or 0 to wrapper port inputs and outputs
        if self.topfile.input_ports.ports_list:
            # assign direction pins inputs to 1b'1
            self.write_assign_dir(self.topfile.input_ports.ports_list, 1)
        if self.topfile.output_ports.ports_list:
            # assign direction pins outputs to 1b'0
            self.write_assign_dir(self.topfile.output_ports.ports_list, 0)
        self.f.write('\n')

        # Insantiate top verilog file
        self.create_module_instance()

        # Close out the wrapper module
        self.f.write('endmodule')
