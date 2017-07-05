module  mux_using_assign_wrapper(
    pin1,
    pin1_dir,
    pin2,
    pin2_dir,
    pin3,
    pin3_dir,
    pin4,
    pin4_dir,
    pin5,
    pin5_dir,
    pin6,
    pin6_dir,
    pin7,
    pin7_dir,
    pin8,
    pin8_dir,
    pin9,
    pin9_dir,
    pin10,
    pin10_dir,
    pin11,
    pin11_dir,
    pin12,
    );

//Inputs
inout pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9;
output pin1_dir, pin2_dir, pin3_dir, pin4_dir, pin5_dir, pin6_dir, pin7_dir, pin8_dir, pin9_dir;

//Outputs
inout pin10, pin11;
output pin10_dir, pin11_dir;

//Inouts
inout pin12;

assign pin1_dir = 1b'1;
assign pin2_dir = 1b'1;
assign pin3_dir = 1b'1;
assign pin4_dir = 1b'1;
assign pin5_dir = 1b'1;
assign pin6_dir = 1b'1;
assign pin7_dir = 1b'1;
assign pin8_dir = 1b'1;
assign pin9_dir = 1b'1;
assign pin10_dir = 1b'0;
assign pin11_dir = 1b'0;

mux_using_assign    mux_using_assign_inst(
    .din_0(pin1),
    .din_1(pin2),
    .sel(pin3),
    .din_2(pin4),
    .din_3(pin5),
    .sel2(pin6),
    .din_4(pin7),
    .din_5(pin8),
    .sel3(pin9),
    .mux_out(pin10),
    .mux_out1(pin11),
    .testing(pin12),
    );

endmodule