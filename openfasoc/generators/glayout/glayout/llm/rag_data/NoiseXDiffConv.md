## Noise Cross Differential Converter

## Purpose

A Noise Cross Differential Converter is used to reduce signal noice and improve signal integrity. It does this by converting signals from single-ended to differential form and vice versa. This improves the performance of a circuit by cleaning outputed and inputed signals.

## Layout Description

A noise cross differential converter consists of 2 nmos components typically called "input" and "bias". Input is moved above bias. Route the gate of input to the source of bias. 

## Parameters

The noise cross differential converter has the following configurable parameters:

input length: a float parameter specifying the length of the input Component part of the noise cross differential converter.
input width: a float parameter specifying the width of the input Component part of the noise cross differential converter.
input fingers: an integer parameter which modifies the number of fingers in the input Component which is part of the noise cross differential converter.
bias length: a float parameter specifying the length of the bias Component part of the noise cross differential converter.
bias width: a float parameter specifying the width of the bias Component part of the noise cross differential converter.
bias fingers: an integer parameter which modifies the number of fingers in the bias Component which is part of the noise cross differential converter.

## Ports

The following are some examples of valid ports for a noise cross differential converter:
input_gate_E
input_source_W
input_drain_N
bias_gate_E
bias_source_W
bias_drain_S