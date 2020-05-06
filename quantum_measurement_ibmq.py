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
