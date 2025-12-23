`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 12/22/2025 07:44:01 PM
// Design Name: 
// Module Name: image_proc
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module image_proc(
    input [7:0] r,
    input [7:0] g,
    input [7:0] b,
    input [7:0] threshold,
    output [7:0] gray,
    output [7:0] segmented
);
    // Intermediate wire for calculation
    wire [15:0] gray_calc;

    // Integer approximation of Gray = 0.299R + 0.587G + 0.114B
    assign gray_calc = (77 * r) + (150 * g) + (29 * b);
    assign gray = gray_calc[15:8]; // Divide by 256 by shifting

    // Segmentation (Thresholding)
    assign segmented = (gray > threshold) ? 8'hFF : 8'h00;

endmodule
