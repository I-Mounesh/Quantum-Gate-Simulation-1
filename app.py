import streamlit as st
import cirq
import numpy as np

def main():
    st.set_page_config(page_title="Quantum Palace Gate", page_icon="🏰")

    # --- UI Header ---
    st.title("🏰 The Quantum Palace Gate")
    st.markdown("""
    **Scenario:** A man stands before a button connected to a palace gate. 
    However, the connection isn't electrical—it's **Quantum Entangled**.
    
    We use a **Bell State** to link the Button and the Gate. 
    Observing the Button instantly determines the state of the Gate.
    """)
    
    st.divider()

    # --- Sidebar: Educational Context ---
    with st.sidebar:
        st.header("⚛️ Behind the Scenes")
        st.write("We are creating a Bell State:")
        st.latex(r"|\psi\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}")
        st.markdown("""
        * **Qubit 0 (The Button):** $H$ Gate puts it in superposition.
        * **Qubit 1 (The Gate):** $CNOT$ entangles it with the Button.
        * **Measurement:** Collapses both to either $|00\rangle$ (Closed) or $|11\rangle$ (Open).
        """)

    # --- Step 1: Initialize Quantum Circuit ---
    st.subheader("1. Setup The Entanglement")
    
    # Define Qubits
    q_button = cirq.NamedQubit("Button")
    q_gate = cirq.NamedQubit("Palace Gate")

    # Create Circuit
    circuit = cirq.Circuit()
    
    # Apply Hadamard to Button (Superposition)
    circuit.append(cirq.H(q_button))
    
    # Apply CNOT (Entangle Button with Gate)
    # Button is Control, Gate is Target
    circuit.append(cirq.CNOT(q_button, q_gate))
    
    # Measure both
    circuit.append(cirq.measure(q_button, key='button_result'))
    circuit.append(cirq.measure(q_gate, key='gate_result'))

    # Display Circuit Diagram
    st.text("Quantum Circuit Diagram:")
    st.code(circuit, language="text")

    st.info("The system is now in Superposition. The button is both 'Pressed' and 'Not Pressed' simultaneously.")

    # --- Step 2: The Interaction ---
    st.subheader("2. The Interaction")
    
    if st.button("Man Presses Button (Observe Quantum State)", type="primary"):
        # Run Simulation
        simulator = cirq.Simulator()
        result = simulator.run(circuit, repetitions=1)
        
        # Extract Results
        button_state = result.measurements['button_result'][0][0]
        gate_state = result.measurements['gate_result'][0][0]

        # --- Step 3: Visualization ---
        st.divider()
        col1, col2 = st.columns(2)

        # Logic: 0 = Off/Closed, 1 = On/Open
        
        with col1:
            st.markdown("### 👨 Man's Action")
            if button_state == 1:
                st.success("**Result: PRESSED (1)**")
                st.markdown("The man chose to press the button.")
                st.markdown("🔴 **Button Down**")
            else:
                st.warning("**Result: NOT PRESSED (0)**")
                st.markdown("The man hesitated and did not press.")
                st.markdown("⚪ **Button Up**")

        with col2:
            st.markdown("### 🏰 Palace Gate")
            if gate_state == 1:
                st.success("**Result: OPEN (1)**")
                st.markdown("Because of entanglement, the gate **opens instantly**.")
                st.image("1769665114636.png", width=150)
            else:
                st.warning("**Result: CLOSED (0)**")
                st.markdown("Because of entanglement, the gate **stays closed**.")
                st.image("1769665119202.png", width=150)

        # Conclusion Text
        st.divider()
        if button_state == gate_state:
             st.markdown(f"""
             > **Verification:** The states matched perfectly ($|{button_state}{gate_state}\\rangle$). 
             > This proves the qubits were entangled. Changing one instantly defined the other. \n
             >Developed by Mounesh C Badiger""")

if __name__ == "__main__":
    main() 