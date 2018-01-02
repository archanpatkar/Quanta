from qiskit import QuantumProgram
from enum import Enum
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

PrisonerDilemma = QuantumProgram()

Prisoners = PrisonerDilemma.create_quantum_register('prisoners', 2)
Outcome = PrisonerDilemma.create_classical_register('outcome', 2)
Game = PrisonerDilemma.create_circuit('Game', [Prisoners], [Outcome])

Game.h(Prisoners[0])
Game.h(Prisoners[1])
Game.measure(Prisoners[0], Outcome[0])
Game.measure(Prisoners[1], Outcome[1])

def QPrisonerDilemma(iterations):
    result = PrisonerDilemma.execute('Game',shots=iterations)
    result = result.get_counts('Game')
    output = {}
    for played in result:
        if(played == "00"):
            output["Prisoner 1 - Cooperates \n Prisoner 2 - Cooperates"] = result.get(played)
        elif(played == "01"):
            output["Prisoner 1 - Cooperates \n Prisoner 2 - Defects"] = result.get(played)
        elif(played == "11"):
            output["Prisoner 1 - Defects \n Prisoner 2 - Defects"] = result.get(played)
        elif(played == "10"):
            output["Prisoner 1 - Defects \n Prisoner 2 - Cooperates"] = result.get(played)
    return output

def Graph(input):
    objects = input.keys()
    y_pos = np.arange(len(objects))
    performance = [input.get(value) for value in input]
    plt.style.use("dark_background")
    plt.figure(num="Prisoner's dilemma")
    plt.bar(y_pos, performance, align='center', color="#ff0000")
    plt.xticks(y_pos, objects)
    plt.ylabel('Occurance')
    plt.title('Game Possibilities')
    plt.show()


output = QPrisonerDilemma(1024)
Graph(output)