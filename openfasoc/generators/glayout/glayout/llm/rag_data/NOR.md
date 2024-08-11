## NOR

# Purpose

A NOR logic gate is a combination of OR and NOT logic gates. It is used to perform logic operations in circuits. The NOR takes in inputs and outputs the opposite of what is outputed by an OR logic gate. If both of the inputs was low (false) the NOR would output high (true). If one of the inputs was high (true) the output would be low (false).

## Layout Description

A NOR consists of 2 nmos components typically called "pulldown1" and "pulldown2" and 2 pmos components typically called "pullup1" and "pullup2". Pullup1 is moved above pulldown1. Pullup2 is moved above pulldown1 and to the right of pullup1. Pulldown2 is moved right of pulldown1. Route the source of pulldown1 to the drain of pulldown2. Route the drain of pulldown1 to the drain of pullup2. Route the source of pullup1 to the source of pullup2. Route the drain of pullup1 to the drain of pullup2.

## Parameters

The NOR has the following configurable parameters:

pullup length: a float parameter specifying the length of the pullup transistor Component part of the NOR.
pullup width: a float parameter specifying the width of the pullup transistor Component part of the NOR.
pullup fingers: an integer parameter which modifies the number of fingers in the pullup transistor Component part of the NOR.
pulldown length: a float parameter specifying the length of the pulldown transistor Component part of the NOR.
pulldown width: a float parameter specifying the width of the pulldown transistor Component part of the NOR.
pulldown fingers: an integer parameter which modifies the number of fingers in the pulldown transistor Component part of the NOR.

## Ports

The following are some examples of valid ports for a ultra-low-power diode:
pullup_gate_S
pullup_source_W
pullup_drain_W
pulldown_gate_N
pulldown_source_E
pulldown_drain_E