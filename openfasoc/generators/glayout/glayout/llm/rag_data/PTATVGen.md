

## Purpose

Proportional to absolute temperature voltage generators are used to generate voltage that linearily varies with absolute temperature. This is done by creating a reference voltage that depends on absolute temperature. This is useful to compensate for a range of temperatures and ensure a circuit has a reliable reference for a wide range of absolute temperatures. This reference voltage also allows different components of a circuit to be accurately calibrated in different temperatures by comparing against the reference voltage.

## Layout Description

A proportional to absolute temperature voltage generator consists of 2 nmos components typically called "A" and "B". A is moved above B. Route source of A to frain of B. Route gate of A to gate of B. Route gate of A to drain of A.

## Parameters

The proportional to absolute temperature voltage generator has the following configurable parameters:

length: a float parameter specifying the length of all transistor Components part of the proportional to absolute temperature voltage generator.
width: a float parameter specifying the width of all transistor Components part of the proportional to absolute temperature voltage generator.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the proportional to absolute temperature voltage generator.

## Ports

The following are some examples of valid ports for a proportional to absolute temperature voltage generator:
A_gate_E
A_source_W
A_drain_N
B_gate_E
B_source_W
B_drain_S