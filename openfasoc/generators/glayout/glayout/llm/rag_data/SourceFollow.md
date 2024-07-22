## Source Follower

## Purpose

A source follower is made to provide current gain by taking in a high impedance input and producing a low impedance output. This is useful since a source follower can act as a buffer between a high impedance source and a low impedance load which allows it to transfer maximum power from the source to the load while reducing impedance.

## Layout Description

A source follower consists of 2 nmos components typically called "isrc" and "srcfoll". srcfoll is moved above isrc. Route the source of srcfoll to the drain of isrc.

## Parameters

The source follower has the following configurable parameters:

srcfoll length: a float parameter specifying the length of the srcfoll Component part of the source follower.
srcfoll width: a float parameter specifying the width of the srcfoll Component part of the source follower.
srcfoll fingers: an integer parameter which modifies the number of fingers in the srcfoll Component which is part of the source follower.
isrc length: a float parameter specifying the length of the isrc Component part of the source follower.
isrc width: a float parameter specifying the width of the isrc Component part of the source follower.
isrc fingers: an integer parameter which modifies the number of fingers in the isrc Component which is part of the source follower.

## Ports

The following are some examples of valid ports for a source follower:
srcfoll_gate_E
srcfoll_source_W
srcfoll_drain_N
isrc_gate_E
isrc_source_W
isrc_drain_S