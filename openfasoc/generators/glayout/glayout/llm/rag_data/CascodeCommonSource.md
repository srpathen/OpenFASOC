## Cascode Common Source

## Purpose

A cascode common source combines a cascode with a common source amplififer, increasing the gain and stability of a normal common source amplifier. This makes the cascode common source useful at taking high impedance and power sources and biasing maximum power with limited noise and impedence.

## Layout Description

A cascode common source consists of 2 nmos components typically called "input" and "bias". Bias is moved above input. Route the source of bias to the drain of input. 

## Parameters

The cascode common source has the following configurable parameters:

input length: a float parameter specifying the length of the input Component part of the cascode common source.
input width: a float parameter specifying the width of the input Component part of the cascode common source.
input fingers: an integer parameter which modifies the number of fingers in the input Component which is part of the cascode common source.
bias length: a float parameter specifying the length of the bias Component part of the cascode common source.
bias width: a float parameter specifying the width of the bias Component part of the cascode common source.
bias fingers: an integer parameter which modifies the number of fingers in the bias Component which is part of the cascode common source.

## Ports

The following are some examples of valid ports for a cascode common source:
input_gate_E
input_source_W
input_drain_N
bias_gate_E
bias_source_W
bias_drain_S