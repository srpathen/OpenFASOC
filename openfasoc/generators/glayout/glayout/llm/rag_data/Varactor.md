## Varactor

## Purpose

Varactors are designed to act as capacitors whos capacitance varies based on a voltage. They are commonly used in to stabilize frequencies and for tuning in circuits. 

## Layout Description

A varactor consists of 2 nmos components typically called "control" and "accumulation". control is moved right of accumulation. Route the drain of control to the drain of accumulation. Route the source of control to the source of accumulation. Route the source of control to the drain of accumulation.

## Parameters

The varactor has the following configurable parameters:

control length: a float parameter specifying the length of the control Component part of the varactor.
control width: a float parameter specifying the width of the control Component part of the varactor.
control fingers: an integer parameter which modifies the number of fingers in the control Component which is part of the varactor.
accumulation length: a float parameter specifying the length of the accumulation Component part of the varactor.
accumulation width: a float parameter specifying the width of the accumulation Component part of the varactor.
accumulation fingers: an integer parameter which modifies the number of fingers in the accumulation Component which is part of the varactor.

## Ports

The following are some examples of valid ports for a varactor:
control_gate_E
control_source_W
control_drain_N
accumulation_gate_E
accumulation_source_W
accumulation_drain_S