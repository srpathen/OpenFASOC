## CTATVGen

## Purpose

A CTATVGen is used to generate a voltage that varies inversely with absolute temperature. This allows circuits to have a refernce temperature that relates to temperature, allowing circuits to accurately work across a range of temperatures. A CTATVGen can also be used to measure and compensate for temperature.

## Layout Description

A CTATVGen consists of 2 nmos components typically called "src" and "load". Move src above load. Route the drain of src to the source of load.

## Parameters

The CTATVGen has the following configurable parameters:

src length: a float parameter specifying the length of the src Component part of the CTATVGen.
src width: a float parameter specifying the width of the src Component part of the CTATVGen.
src fingers: an integer parameter which modifies the number of fingers in the src Component which is part of the CTATVGen.
src rmult: a float parameter specifying the width of metal connections within the src component part of the CTAVGen.
load length: a float parameter specifying the length of the load Component part of the CTATVGen.
load width: a float parameter specifying the width of the load Component part of the CTATVGen.
load fingers: an integer parameter which modifies the number of fingers in the load Component which is part of the CTATVGen.
load rmult: a float parameter specifying the width of metal connections within the load component part of the CTAVGen.

## Ports

The following are some examples of valid ports for a CTATVGen:
src_gate_E
src_source_W
src_drain_N
load_gate_E
load_source_W