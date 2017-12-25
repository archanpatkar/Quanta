from qiskit import QuantumProgram

Map = QuantumProgram()

mapper = Map.create_quantum_register('mapper', 2)
output = Map.create_classical_register('output', 1)
Mapper = Map.create_circuit('Map', [mapper], [output])

Mapper.h(mapper[0])
Mapper.h(mapper[1])
Mapper.measure(mapper[0], output[0])

def QMap(n1,n2):
    result = Map.execute('Map',shots=1)
    result = result.get_counts('Map')
    print(result)

QMap(20,20)

#Work in Progress