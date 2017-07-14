import sys,os

import sys
from verilog_file import verilog_file
from verilog_wrapper import verilog_wrapper

filename = sys.argv[1]

if not os.path.isfile(filename):

    print 'Invalid Verilog File Error: No file found'

elif filename.lower().endswith('.v'):     #Only works with .v files for now

    filename_base = filename[:len(filename)-2]
    topfile = verilog_file(filename)
    topfile.extract_info()
    wrapper = (verilog_wrapper(filename_base+'_wrapper.v', topfile))
    wrapper.create_new_file()
else:
    print 'Invalid Verilog File Error: File must end in .v'


