from qiskit import QuantumProgram

CoinFlipper = QuantumProgram()

coin = CoinFlipper.create_quantum_register('coin', 1)
output = CoinFlipper.create_classical_register('output', 1)
Flip = CoinFlipper.create_circuit('Flip', [coin], [output])

Flip.h(coin)
Flip.measure(coin, output)

def Coin_Flip():
    result = CoinFlipper.execute('Flip')
    result = result.get_counts('Flip')
    if(result["0"] > result["1"]):
        print("Tails")
        return False
    elif(result["1"] > result["0"]):
        print("Heads")
        return True
    else:
        print("Try Again!")

print("-----------")
print(Coin_Flip())
print("-----------")
print(Coin_Flip())
print("-----------")
print(Coin_Flip())
print("-----------")
print(Coin_Flip())
print("-----------")
print(Coin_Flip())
print("-----------")
print(Coin_Flip())
print("-----------")