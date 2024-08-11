## LowNoiseAmp

## Purpose

A Low Noise Amplifier is designed to amplify weak signals. They boost weak, recieved signals and output an amplified signal while also reducing noise interference which improves the detectablity of the signal and makes it easier to be deteced by recievers. 

## Layout Description

A Low Noise Amplifier consists of 2 nmos components typically called "gain" and "input". Gain is placed below input. The source of input is routed to the drain of gain. The gate of input is routed to the source of gain.

## Parameters

The Low Noise Amplifier has the following configurable parameters:

input length: a float parameter specifying the length of the input transistor Component part of the Low Noise Amplifier.
input width: a float parameter specifying the width of the input transistor Component part of the Low Noise Amplifier.
input fingers: an integer parameter which modifies the number of fingers in the input transistor Component part of the Low Noise Amplifier.
gain length: a float parameter specifying the length of the gain transistor Component part of the Low Noise Amplifier.
gain width: a float parameter specifying the width of the gain transistor Component part of the Low Noise Amplifier.
gain fingers: an integer parameter which modifies the number of fingers in the gain transistor Component part of the Low Noise Amplifier.

## Ports

The following are some examples of valid ports for a Low Noise Amplifier:
input_source_S
input_drain_N
input_gate_W
gate_source_E
gate_drain_N
gate_gate_S