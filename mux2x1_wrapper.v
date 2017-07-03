module  mux_using_assign_wrapper(
    pin4,
    pin4_dir,
    pin2,
    pin2_dir,
    pin1,
    pin1_dir,
    pin7,
    pin7_dir
    );

//Inputs
inout pin4, pin2, pin1;
output pin4_dir, pin2_dir, pin1_dir;

//Outputs
inout pin7;
output pin7_dir;

assign pin4_dir = 1b'1;
assign pin2_dir = 1b'1;
assign pin1_dir = 1b'1;
assign pin7_dir = 1b'0;

mux_using_assign    mux_using_assign_inst(
    .din_0(pin4),
    .din_1(pin2),
    .sel(pin1),
    .mux_out(pin7),
    );

endmodule