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

    def create_new_file(self):
        f = open(self.file_name, 'w+')
        f.write('module  ' + self.module_name + '_wrapper(\n')
        if len(self.input_pins):
            for i,n in enumerate(self.input_pins):
                if i != (len(self.input_pins)-1) and len(self.output_pins) == 0 and len(self.inout_pins) == 0:
                    f.write('    ' + n + '\n')
                else:
                    f.write('    ' + n + ',\n')
        if len(self.output_pins):
            for i,n in enumerate(self.output_pins):
                if i != (len(self.output_pins)-1) and len(self.inout_pins) == 0:
                    f.write('    ' + n + '\n')
                else:
                    f.write('    ' + n + ',\n')
        if len(self.inout_pins):
            print 'test'
            for i,n in enumerate(self.inout_pins):
                if i != (len(self.inout_pins)-1):
                    f.write('    ' + n + '\n')
                else:
                    f.write('    ' + n + ',\n')
        f.write('    );\n')
        f.write('\n')

        if self.input_pins:
            f.write('input ')
            for i,n in enumerate(self.input_pins):
                if i != (len(self.input_pins)-1):
                    f.write(n + ', ')
                else:
                    f.write(n + ';\n')

        if self.output_pins:
            f.write('output ')
            for i,n in enumerate(self.output_pins):
                if i != (len(self.output_pins)-1):
                    f.write(n + ', ')
                else:
                    f.write(n + ';\n')

        if self.inout_pins:
            f.write('inout ')
            for i, n in enumerate(self.inout_pins):
                if i != (len(self.inout_pins) - 1):
                    f.write(n + ', ')
                else:
                    f.write(n + ';\n')
        f.write('\n')
        f.write(self.module_name + '    ' + self.module_name + '_inst(\n')
        for i,n in enumerate(self.input_ports):
            f.write('    .' + n + '(' + self.input_pins[i]+ '),\n' )
        for i,n in enumerate(self.output_ports):
            f.write('    .' + n + '(' + self.output_pins[i]+ '),\n' )
        for i,n in enumerate(self.inout_ports):
            f.write('    .' + n + '(' + self.inout_pins[i]+ '),\n' )
        f.write('    );\n')
        f.write('\n')
        f.write('endmodule')


