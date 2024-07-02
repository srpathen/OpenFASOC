# Current Mirror
## Purpose

The purpose of a current mirror is to copy a current from one branch of a circuit to another, maintaining a consistent current ratio.
## Layout Description

A current mirror consists of two transistors (either NFET or PFET). One transistor, labeled as the reference, accepts an input current at its drain, while the other, labeled as the mirror, has the output current at its drain. The sources of both transistors are connected, and their gates are also connected. The drain of the reference transistor is connected to its gate.
## Parameters
ratio: The width ratio between the mirror and reference transistors, used to tune the relative current between the mirror transistor drain and the reference transistor drain.
length: a float parameter specifying the length of all transistor Components part of the current mirror.
width: a float parameter specifying the width of all transistor Components part of the current mirror.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the current mirror.
## Ports
The following are just some examples of the valid ports for current mirror:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E