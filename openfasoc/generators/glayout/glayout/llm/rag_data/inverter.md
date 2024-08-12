# Static CMOS Inverter
## Purpose
The purpose of an inverter is to invert the input signal, producing a high output voltage for a low input voltage and vice versa.
## Layout Description
A static CMOS inverter consists of a PMOS transistor placed above an NMOS transistor. The PMOS source is connected to VDD, and the NMOS source is connected to ground. The drains of both transistors are connected to form the output node. The gates of both transistors are also connected to form the input node.
## Parameters
sizing ratio: The ratio between the PMOS width and the NMOS width, typically optimized at 2:1.
length: a float parameter specifying the length of all transistor Components part of the inverter.
width: a float parameter specifying the width of all transistor Components part of the inverter.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the inverter.
## Ports
The following are just some examples of the valid ports for inverter:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E
