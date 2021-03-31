from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
print("\nQuantum-CoinFlipper v1.0.\nMade using Qiskit, IBMQ and Python3.\nLimit to the number of coins is 32.\nThis program doesn't store your IBMQ API Key.")

API_key = input("\nEnter Your IBMQ API Key: ")
while(1):
    n = int(input("Enter Number of coins to flip: "))
    IBMQ.enable_account(API_key)
    provider = IBMQ.get_provider(hub='ibm-q')

    q = QuantumRegister(n,'q')
    c = ClassicalRegister(n,'c')
    circuit = QuantumCircuit(q,c)
    circuit.h(q) # Applies hadamard gate to all qubits
    circuit.measure(q,c) # Measures all qubits 

    backend = provider.get_backend('ibmq_qasm_simulator')
    Flipping = execute(circuit, backend, shots=1)
                               
    print('\nFlipping Coin(s)...\n')                 
    job_monitor(Flipping)
    counts = Flipping.result().get_counts()
    result = list(counts.keys())
    res = ""
    for i in result[0]:
        if(i=="0"):
            res+= "H "
        else:
            res+="T "
    print("\nRESULT: ",res)
    print("Number of Heads = ",res.count("H"))
    print("Number of Tails = ",res.count("T"))
    resp = int(input("\nEnter 0 to Flip again and 1 to Exit: "))
    if(resp==1):
        break

    
