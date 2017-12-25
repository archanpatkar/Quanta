from qiskit import *
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

qp = qiskit.QuantumProgram()

qr = qp.create_quantum_register('qr', 2)
cr = qp.create_classical_register('cr', 8)
qc = qp.create_circuit('Testing_Quantum_Entanglement', [qr], [cr])

qc.h(qr[0])
qc.h(qr[1])
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])
qc.cx(qr[0],qr[1])
qc.measure(qr[0], cr[2])
qc.measure(qr[1], cr[3])
qc.x(qr[0])
qc.cx(qr[0],qr[1])
qc.measure(qr[0], cr[4])
qc.measure(qr[1], cr[5])
qc.x(qr[0])
qc.cx(qr[0],qr[1])
qc.measure(qr[0], cr[6])
qc.measure(qr[1], cr[7])

result = qp.execute('Testing_Quantum_Entanglement',shots=1)
permutation = result.get_counts('Testing_Quantum_Entanglement')

# states = [key for key in permutation.keys()][0]

print(permutation)

# # Initial State of Qubits Measured and Stored in Bits of Register
# initialstate = states[0:2]

# # State After Entaglement of Qbits
# afterentanglement = states[2:4]

# # After flipping a Qubit and Observing the Behaviour
# afterupdate = states[4:6]

# print("Initial State of QBits")
# print(initialstate)

# print("State of QBits after Entanglement")
# print(afterentanglement) 

# print("After Changing State of a QBit")
# print(afterupdate)
 
# objects = permutation.keys()
# y_pos = np.arange(len(objects))
# performance = [permutation.get(value) for value in permutation]
# print(result.get_ran_qasm('Testing_Quantum_Entanglement'))

# plt.style.use("dark_background")
 
# plt.bar(y_pos, performance, align='center', color="#ff0000")
# plt.xticks(y_pos, objects)
# plt.ylabel('Occurance')
# plt.title('Probabilistic Values')
 
# plt.show()