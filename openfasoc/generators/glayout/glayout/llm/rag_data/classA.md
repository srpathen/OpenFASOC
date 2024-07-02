# Class A Amplifier
## Purpose
The purpose of a Class A amplifier is to provide linear amplification of an input signal with low distortion.
## Layout Description
A Class A amplifier can be created with two NMOS transistors, M1 and M2. The gate of M1 is connected to the input voltage, and its drain is connected to the drain of M2. The source of M1 is tied to VSS, and the source of M2 is connected to VDD. The gate of M2 is connected to VGG. The node between the drains of M1 and M2 is connected to VOUT, which can be connected to a capacitor and resistor in parallel to block unwanted signals from reaching the load.
## Parameters
The class A amplifier has the following configurable parameters:
length: a float parameter specifying the length of all transistor Components part of the class A amplifier.
width: a float parameter specifying the width of all transistor Components part of the class A Aamplifier.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the class A amplifier.
## Ports
The following are just some examples of the valid ports for class A amplifier:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E
