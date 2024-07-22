## Cascode Common Gate

## Purpose

A cascode common gate is a type of amplifier. It provides high voltage gain while also limiting noise. This makes the cascode common gate a very useful high gain amplififer that can be used to decrease noise and impedance.

## Layout Description

A cascode common gate conssits of 2 nmos components typically called "input" and "output". Move output above input. Route the source of input to the drain of output.

## Parameters

The cascode common gate has the following configurable parameters:

input length: a float parameter specifying the length of the input Component part of the cascode common gate.
input width: a float parameter specifying the width of the input Component part of the cascode common gate.
input fingers: an integer parameter which modifies the number of fingers in the input Component which is part of the cascode common gate.
output length: a float parameter specifying the length of the output Component part of the cascode common gate.
output width: a float parameter specifying the width of the output Component part of the cascode common gate.
output fingers: an integer parameter which modifies the number of fingers in the output Component which is part of the cascode common gate.

## Ports

The following are some examples of valid ports for a cascode common gate:
input_gate_E
input_source_W
input_drain_N
output_gate_E
output_source_W
output_drain_S