## Regulated Cascode

## Purpose

A regulated cascode significantly increases output resistance compared to simple cascodes or amplififers. This improves the performance of a circuit by increasing voltage gain, increasing bandwith, and improving linearity.

## Layout Description

A regulated cascode consists of 2 nmos components typically called "A" and "B". A is moved above B. Route the gate of A to the drain of B. Route the gate of B to the source of B.

## Parameters

The regulated cascode has the following configurable parameters:

length: a float parameter specifying the length of all transistor Components part of the regulated cascode.
width: a float parameter specifying the width of all transistor Components part of the regulated cascode.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the regulated cascode.

## Ports

The following are some examples of valid ports for a regulated cascode:
A_gate_E
A_source_W
A_drain_N
B_gate_E
B_source_W
B_drain_S