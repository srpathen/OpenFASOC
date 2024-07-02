# Common Drain Amplifier
## Purpose
The purpose of a common drain amplifier, also known as a source follower, is to provide buffering with high input impedance, low output impedance, and a voltage gain close to unity.
## Layout Description
A typical source follower schematic includes an NMOS transistor with the drain connected to VDD and the input signal applied to the gate. A resistor (Rs) connects the source to ground, and the output is taken from the source of the transistor.

If another NMOS transistor replaces the resistor, its source is connected to ground, its drain to the source of the first transistor, and its gate to a voltage called Vbias, which controls the NMOS's resistance.
## Parameters
The common drain amplifier has the following configurable parameters:
length: a float parameter specifying the length of all transistor Components part of the common drain amplifier.
width: a float parameter specifying the width of all transistor Components part of the common drain amplifier.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the common drain amplifier.
## Ports
The following are just some examples of the valid ports for common drain amplifier:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E
