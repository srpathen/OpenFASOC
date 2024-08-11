## ULPD

## Purpose

Ultra-low-power diodes are diodes designed to use minimal power making it extremely useful for minimal energy consumption. Thye have mininmal energy loss and can operate at very low power levels improving efficiency and function of low power circuits.

## Layout Description

A ultra-low-power diode consists of 2 nmos components typically called "A" and "B". A is moved above B. Route gate of A to source of B. Route source of A to gate of B.

## Parameters

The ultra-low-power diode has the following configurable parameters:

length: a float parameter specifying the length of all transistor Components part of the ultra-low-power diode.
width: a float parameter specifying the width of all transistor Components part of the ultra-low-power diode.
fingers: an integer parameter which modifies the number of fingers in all transistor Components which are part of the ultra-low-power diode.

## Ports

The following are some examples of valid ports for a ultra-low-power diode:
A_gate_E
A_source_W
A_drain_N
B_gate_E
B_source_W
B_drain_S