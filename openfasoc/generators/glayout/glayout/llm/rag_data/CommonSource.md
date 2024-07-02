# Common Source Amplifier
## Purpose
The purpose of a common source amplifier is to amplify the input signal, providing high gain and moderate input and output impedances.
## Layout Description
A common source amplifier consists of two MOSFETs: M1, which acts as the amplifying stage, and M2, which serves as the active load. Depending on the type of active load, the port of M2 corresponding to the direction of current is connected to the drain of M1. The source of M1 is connected to a lower voltage level than the supply.
## Parameters
The common source amplifier has the following configurable parameters:
length: a float parameter specifying the length of all transistor Components part of the common source amplifier.
width: a float parameter specifying the width of all transistor Components part of the common source amplifier.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the common source amplifier.
## Ports
The following are just some examples of the valid ports for common source amplifier:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E