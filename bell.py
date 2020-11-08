# Mariana Hernandez
# Tarea 6 - computo cuantico

"""Script for preparing the Bell state |\Phi^{+}> in Cirq. """

# Import the Cirq library
import cirq

# Get qubits and circuit
# qreg crea un arreglo de dos qubits
qreg = [cirq.LineQubit(x) for x in range(2)]
circ = cirq.Circuit()

# Add the Bell state preparation circuit
# primer compuerta en el circuito es H aplicada al primer qubit
# siguiente compuerta en el circuito es CNOT aplicada del
# primer qubit al segundo
circ.append([cirq.H(qreg[0]),cirq.CNOT(qreg[0], qreg[1])])

# Display the circuit
print("Circuit")
print(circ)

# inicializar simulacion
sim = cirq.Simulator()
print('Simulate the circuit:')

# initial_state = (0,0): (1/sqrt(2))(|00> + |11>)
# initial_state = (1,0): (1/sqrt(2))(|00> - |11>)
# initial_state = (0,1): (1/sqrt(2))(|01> + |10>)
results=sim.simulate(circ, initial_state= (0,1))
print(results)

# Add measurements
# *qreg: The qubits that the measurement gate should measure.
# key: The string key of the measurement. If this is None, 
# it defaults to a comma-separated list of the target qubits’ str values
circ.append(cirq.measure(*qreg, key="z"))

# Simulate the circuit
res = sim.run(circ, repetitions=100)

# Display the outcomes
print("\nMeasurements:")
print(res.histogram(key="z"))










