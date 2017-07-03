module  mux_using_assign_wrapper(
    pin4,
    pin2,
    pin1,
    pin7,
    );

input pin4, pin2, pin1;
output pin7;

mux_using_assign    mux_using_assign_inst(
    .din_0(pin4),
    .din_1(pin2),
    .sel(pin1),
    .mux_out(pin7),
    );

endmodule