import streamlit as st

# Constante de los gases ideales en L·atm/mol·K
R = 0.0821

st.title("Calculadora de Gases Ideales")
st.write("Resuelve la ecuación PV = nRT")

# Selección de la variable a resolver
variable = st.selectbox("¿Qué variable deseas calcular?", ["P (Presión)", "V (Volumen)", "n (moles)", "T (Temperatura)"])

# Entradas comunes
P = st.number_input("Presión (atm)", value=1.0) if variable != "P (Presión)" else None
V = st.number_input("Volumen (L)", value=1.0) if variable != "V (Volumen)" else None
n = st.number_input("Cantidad de sustancia (mol)", value=1.0) if variable != "n (moles)" else None
T = st.number_input("Temperatura (K)", value=273.15) if variable != "T (Temperatura)" else None

# Cálculo
if st.button("Calcular"):
    if variable == "P (Presión)":
        resultado = n * R * T / V
        st.success(f"La presión es {resultado:.3f} atm")
    elif variable == "V (Volumen)":
        resultado = n * R * T / P
        st.success(f"El volumen es {resultado:.3f} L")
    elif variable == "n (moles)":
        resultado = P * V / (R * T)
        st.success(f"La cantidad de sustancia es {resultado:.3f} mol")
    elif variable == "T (Temperatura)":
        resultado = P * V / (n * R)
        st.success(f"La temperatura es {resultado:.2f} K")
