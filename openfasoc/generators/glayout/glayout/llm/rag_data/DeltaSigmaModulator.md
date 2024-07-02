# Delta Sigma Modulator ADC
## Purpose
The purpose of a delta sigma modulator ADC is to convert analog signals into digital signals with high accuracy and resolution.
## Layout Description
A delta sigma modulator consists of several existing components, including an opamp and a latched comparator. The latched comparator includes a D flip-flop and a strong arm latch, all of which can be directly imported. The outputs of the opamp should be connected to the inputs of the latched comparator.
## Parameters
The delta sigma modulator has the following configurable parameters:
length: a float parameter specifying the length of all transistor Components part of the delta sigma modulator.
width: a float parameter specifying the width of all transistor Components part of the delta sigma modulator.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the delta sigma modulator.
## Ports
The following are just some examples of the valid ports for delta sigma modulator:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E