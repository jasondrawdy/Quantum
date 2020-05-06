from projectq.ops import H, Measure
from projectq import MainEngine

def get_random_number(quantum_engine):
    # Initialize a qubit in superposition by applying a Hadamard gate and measure it for 0 or 1.
    qubit = quantum_engine.allocate_qubit()
    H | qubit
    Measure | qubit
    random_number = int(qubit)
    return random_number

sum = 0
random_numbers_list = []
quantum_engine = MainEngine()
for i in range(10):
    # Generate 10 new random number sets.
    random_numbers_list.append(get_random_number(quantum_engine))
quantum_engine.flush()
print('Random Set: ', random_numbers_list)
for i in random_numbers_list:
    sum += i
print("Sum: ", sum)
