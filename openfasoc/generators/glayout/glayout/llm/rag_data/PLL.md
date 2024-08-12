# Phase Locked Latch
## Purpose

A phase locked latch is a specialized circuit used in digital systems to synchronize data with a clock signal, ensuring that the output data is stable and aligned with the clock phase. This is essential in applications where timing precision is critical, such as in high-speed data transfer and clock distribution networks.

## Layout Description

A phase locked latch typically consists of the following components:

    Input Stage: Includes data input (D) and clock input (CLK).
    Phase Detector: Compares the phase of the input clock signal with a reference clock signal and generates a control signal based on the phase difference.
    Charge Pump: Converts the control signal from the phase detector into a voltage signal.
    Voltage-Controlled Oscillator (VCO): Generates a clock signal whose frequency is controlled by the voltage signal from the charge pump.
    Feedback Loop: Provides feedback to the phase detector to adjust the phase of the VCO clock signal, locking it to the phase of the input clock signal.
    Latch Mechanism: Captures and holds the data input (D) on the edges of the phase-locked clock signal.

The general connections are as follows:

    The data input (D) is connected to the input stage.
    The clock input (CLK) is connected to the phase detector.
    The output of the phase detector is connected to the charge pump, which in turn controls the VCO.
    The output of the VCO provides the phase-locked clock signal, which is used to control the latch mechanism.
    The feedback loop ensures that the VCO clock signal remains in phase with the input clock signal.