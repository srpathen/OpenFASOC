# D Flip-Flop
## Purpose

A D flip-flop, also known as a data or delay flip-flop, is a digital storage element that captures the value of the input (D) on the rising or falling edge of the clock signal (CLK) and holds this value until the next clock edge. It is commonly used for synchronization and data storage in digital circuits.
## Layout Description

A D flip-flop typically consists of a series of interconnected logic gates and latches to form the following key components:

    Input Stage: Includes the data input (D) and clock input (CLK).
    Edge-Triggering Mechanism: Ensures that the D flip-flop captures the input value only on a specific clock edge (either rising or falling).
    Storage Element: Comprises a master-slave latch configuration to store the captured value until the next clock cycle.
    Output Stage: Provides the stored value as the output (Q), with an optional complementary output (Q‾Q​).

The general connections are as follows:

    The data input (D) is connected to the input stage.
    The clock input (CLK) is connected to the edge-triggering mechanism, which controls the timing of data capture.
    The output (Q) reflects the value of the data input (D) as captured on the clock edge.
    An optional complementary output (Q‾Q​) provides the inverse of the output (Q).
    
## Parameters
The d flip flop has the following configurable parameters:
length: a float parameter specifying the length of all transistor Components part of the d flip flop.
width: a float parameter specifying the width of all transistor Components part of the d flip flop.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the d flip flop.
## Ports
The following are just some examples of the valid ports for diff_pair:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E
