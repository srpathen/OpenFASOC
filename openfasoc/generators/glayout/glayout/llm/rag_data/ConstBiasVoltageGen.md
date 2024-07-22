## Constant Bias Voltage Generator

## Purpose

A constant bias voltage generator is used to generate bias voltage that snures a transistor remains constant in the presence of varying factors (voltage, temperature, etc.). This ensures that transistors in a circuit run consistently which keeps a circuit reliable and efficient in varying conditions.

## Layout Description

A constant bias voltage generator consists of 2 nmos components typically called "source" and "load". Source is moved above load. Route the source of source to the drain of load. Route the gate of load to the drain of load. Route the gate of source to the source of load.

## Parameters

## Parameters

The constant bias voltage generator has the following configurable parameters:

source length: a float parameter specifying the length of the source Component part of the constant bias voltage generator.
source width: a float parameter specifying the width of the source Component part of the constant bias voltage generator.
source fingers: an integer parameter which modifies the number of fingers in the source Component which is part of the constant bias voltage generator.
load length: a float parameter specifying the length of the load Component part of the constant bias voltage generator.
load width: a float parameter specifying the width of the load Component part of the constant bias voltage generator.
load fingers: an integer parameter which modifies the number of fingers in the load Component which is part of the constant bias voltage generator.

## Ports

The following are some examples of valid ports for a constant bias voltage generator:
source_gate_E
source_source_W
source_drain_N
load_gate_E
load_source_W