//-----------------------------------------------------
// Design Name : mux_using_assign
       // File Name   : mux_using_assign.v
// Function    : 2:1 Mux using Assign
// Coder       : Deepak Kumar Tala
//-----------------------------------------------------
module  mux_using_assign(
din_0      , // Mux first input
din_1      , // Mux Second input
sel        , // Select input
mux_out      // Mux output
);
//-----------Input Ports---------------
input din_0, din_1, sel ; //$input pin1, pin2, pin3 $
input din_2, din_3, sel2 ; //$input pin4, pin5, pin6 $
input din_4, din_5, sel3 ; //$input pin7, pin8, pin9 $
//-----------Output Ports---------------
output mux_out;			  //$output pin10 $
output mux_out1;	      //$output pin11 $
inout testing;            //$inout pin12 $
//------------Internal Variables--------
wire  mux_out;
//-------------Code Start-----------------
assign mux_out = (sel) ? din_1 : din_0;

endmodule //End Of Module mux