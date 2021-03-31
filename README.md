# Quantum-CoinFlipper
This repository is dedicated to flip coins with true randomness using a real 
quantum computer with help of IBMQ's API and Qiskit's repository.
## Requirements
1. Python3
2. Qiskit Module
3. IBMQ account(Required for API connection)

## Working
The program creates as many quantum and classical bits as the number of coins
to flipped(Limited to 32 due to limitation of current quantum computers) and 
each quantum bit is connect to an hadamard gate and then measured to classical bit
to achieve true randomness.
![alt text](https://github.com/DeathReaper42/Quantum-CoinFlipper/blob/main/images/Quantum_CoinFlipper.png)

## Credits
- IBMQ- https://quantum-computing.ibm.com
- Qiskit Module - https://github.com/Qiskit/qiskit

## References
- Hadamard (H) gate - https://en.wikipedia.org/wiki/Quantum_logic_gate#Hadamard_(H)_gate
- Coin Flipping - https://en.wikipedia.org/wiki/Coin_flipping





