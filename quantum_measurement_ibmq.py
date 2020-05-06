"""
Program: quantum_measurement_ibmq.py
Author: Jason Drawdy
Date: May 6th, 2020 (05.06.20)
Description:
This program simulates the measurement of a quantum bit called a qubit using the ProjectQ API.
"""

import os
from pathlib import Path

import projectq.setups.ibm # Imports the default compiler to map to IBM QE
from dotenv import load_dotenv
from projectq.backends import IBMBackend
from projectq.ops import All, Entangle, Measure
from projectq import MainEngine

try:
    current_path = Path('.') / '.env'
    load_dotenv(current_path)
    token = os.environ['IBM_QUANTUM_API_KEY']
    device = device='ibmq_rome'
    compiler_engines = projectq.setups.ibm.get_engine_list(token=token,device=device)
    engine = MainEngine(IBMBackend(token=token, use_hardware=True, num_runs=1024, verbose=True, device=device),
                        engine_list=compiler_engines)
    qureg = engine.allocate_qureg(3)
    Entangle | qureg
    All(Measure) | qureg
    engine.flush()
    print([int(q) for q in qureg])
except KeyError:
    print("Please define the environment variables: IBM_QUANTUM_API_KEY")
