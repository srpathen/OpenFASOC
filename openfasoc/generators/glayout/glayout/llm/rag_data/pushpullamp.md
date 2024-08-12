# Push Pull Amp (Class B Amplifier)
## Purpose
A push-pull amplifier, also known as a Class B amplifier, is designed to amplify signals with improved efficiency and reduced distortion compared to single-ended amplifiers.
## Layout Description

A push-pull amplifier typically consists of two transistors: an NMOS and a PMOS.

    NMOS: Its source is connected to the ground or a common reference point, and its drain is connected to the positive supply voltage (VDD).
    PMOS: Its source is connected to the positive supply voltage (VDD), and its drain is connected to the ground or a common reference point.

## Parameters
The push pull amplifier has the following configurable parameters:
length: a float parameter specifying the length of all transistor Components part of the push pull amplifier.
width: a float parameter specifying the width of all transistor Components part of the push pull amplifier.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the push pull amplifier.
## Ports
The following are just some examples of the valid ports for push pull amplifier:
ComponentRef_A_source_E
ComponentRef_B_drain_W
ComponentRef_A_gate_E