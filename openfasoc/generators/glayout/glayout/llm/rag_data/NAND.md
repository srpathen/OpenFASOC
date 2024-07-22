## NAND

# Purpose

A NAND logic gate is a combination of AND and NOT logic gates. It is used to perform logic operations in circuits. The NAND takes in inputs and outputs the opposite of what is outputed by an AND logic gate. If one of the inputs was low (false) the NAND would output high (true). If all inputs were high (true) the output would be low (false).

## Layout Description

A NAND consists of 2 nmos components typically called "pulldown1" and "pulldown2" and 2 pmos components typically called "pullup1" and "pullup2". Pullup1 is moved above pulldown1. Pullup2 is moved above pulldown1 and to the right of pullup1. Pulldown2 is moved right of pulldown1. Route the drain of pulldown1 to the source of pulldown2. Route the drain of pulldown2 to the drain of pullup1. Route the source of pullup1 to the source of pullup2. Route the drain of pullup1 to the drain of pullup2.

## Parameters

The NAND has the following configurable parameters:

pullup length: a float parameter specifying the length of the pullup transistor Component part of the NAND.
pullup width: a float parameter specifying the width of the pullup transistor Component part of the NAND.
pullup fingers: an integer parameter which modifies the number of fingers in the pullup transistor Component part of the NAND.
pulldown length: a float parameter specifying the length of the pulldown transistor Component part of the NAND.
pulldown width: a float parameter specifying the width of the pulldown transistor Component part of the NAND.
pulldown fingers: an integer parameter which modifies the number of fingers in the pulldown transistor Component part of the NAND.

## Ports

The following are some examples of valid ports for a ultra-low-power diode:
pullup_gate_S
pullup_source_W
pullup_drain_W
pulldown_gate_N
pulldown_source_E
pulldown_drain_E