"""
Program: quantum_measurement_simulation.py
Author: Jason Drawdy
Date: May 6th, 2020 (05.06.20)
Description:
This program simulates the measurement of a quantum bit called a qubit using the ProjectQ API.
"""

from projectq import MainEngine
from projectq.ops import H, Measure

engine = MainEngine()
qubit = engine.allocate_qubit()

H | qubit
Measure | qubit

engine.flush()
print("Measured {}".format(int(qubit)))
