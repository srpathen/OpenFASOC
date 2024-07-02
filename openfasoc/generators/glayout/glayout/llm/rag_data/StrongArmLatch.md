# Strong Arm Latch
## Purpose
A strong arm latch is a type of flip-flop circuit used in digital electronics for storing binary data.
## Layout Description
A strong arm latch consists of several components arranged as follows:

    Cross Coupled Inverters: Positioned at the top to form the feedback loop essential for latching functionality.
    Bridge NFET: Located above the diffpair and below the cross coupled inverters, facilitating connections between different parts of the circuit.
    Clkgnd NFET: Positioned at the bottom to provide grounding connections.
    ClkpwrL and ClkpwrR PFETs: Positioned to the left and right of the cross coupled inverters respectively, controlling the power supply to the latch.
## Routing details:

    Connect the drain of transistor A of the diffpair with the drain of the bridge.
    Connect the drain of transistor B of the diffpair with the source of the bridge.
    Connect the source of transistor A in the diffpair with the source of clkgnd.

This layout configuration ensures proper operation and stability of the strong arm latch, facilitating reliable data storage and retrieval in digital circuits.