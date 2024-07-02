# Differential Pair
## Purpose
The differential pair amplifies the difference between two input signals while rejecting common-mode signals
## Layout Description
The diff_pair is created using 2 nfet Components. The nfet Components are referred to as “A” and “B” respectively. Place B right of A. Route the source of A to the source of B.
## Parameters
The diff pair has the following configurable parameters:
length: a float parameter specifying the length of all transistor Components part of the diff pair.
width: a float parameter specifying the width of all transistor Components part of the diff pair.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the diff pair.
## Ports
The following are just some examples of the valid ports for diff_pair:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E
