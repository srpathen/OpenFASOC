## Bias Voltage Generator

## Purpose

A bias voltage generator is used to generate a bias voltage that is used by transistors and other components for consistent performance. The bias voltage changes depending on external factors which ensures the other components of the circuit perform uniformly and consistently. This stops variations and unpredictably in the performance of a circuit.

## Layout Description

A bias voltage generator consists of a nmos component typically called "load" and a pmos component typically called "src". Src is moved above load. Route the drain of src to the drain of load. Route the gate of load to the drain of load. Route the gate of src to the source of load.

## Parameters

The bias voltage generator has the following configurable parameters:

load length: a float parameter specifying the length of the load Component part of the bias voltage generator.
load width: a float parameter specifying the width of the load Component part of the bias voltage generator.
load fingers: an integer parameter which modifies the number of fingers in the load Component which is part of the bias voltage generator.
src length: a float parameter specifying the length of the src Component part of the bias voltage generator.
src width: a float parameter specifying the width of the src Component part of the bias voltage generator.
src fingers: an integer parameter which modifies the number of fingers in the src Component which is part of the bias voltage generator.

## Ports

The following are some examples of valid ports for a bias voltage generator:
load_gate_E
load_source_W
load_drain_N
src_gate_E
src_source_W
src_drain_S