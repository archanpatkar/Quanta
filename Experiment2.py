from qiskit import QuantumProgram
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


qp = QuantumProgram()

qr = qp.create_quantum_register('qr', 2)
cr = qp.create_classical_register('cr', 2)
qc = qp.create_circuit('Testing_CNOT', [qr], [cr])

qc.h(qr[0])
qc.h(qr[1])
qc.cx(qr[0], qr[1])
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])

result = qp.execute('Testing_CNOT')
permutation = result.get_counts('Testing_CNOT')
 
objects = permutation.keys()
y_pos = np.arange(len(objects))
performance = [permutation.get(value) for value in permutation]
print(result.get_ran_qasm('Testing_CNOT'))

plt.style.use("dark_background")
 
plt.bar(y_pos, performance, align='center', color="#ff0000")
plt.xticks(y_pos, objects)
plt.ylabel('Occurance')
plt.title('Probabilistic Values')
 
plt.show()