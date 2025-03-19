import streamlit as st

# Configuración inicial de la aplicación
st.set_page_config(page_title="Aplicación Contable", layout="wide")

# Variables para almacenar los saldos de las cuentas
if 'saldo_caja' not in st.session_state:
    st.session_state.saldo_caja = 30000
if 'saldo_mercancias' not in st.session_state:
    st.session_state.saldo_mercancias = 10000
if 'saldo_mobiliario' not in st.session_state:
    st.session_state.saldo_mobiliario = 20000
if 'saldo_terreno' not in st.session_state:
    st.session_state.saldo_terreno = 2800000
if 'saldo_edificio' not in st.session_state:
    st.session_state.saldo_edificio = 1500000
if 'saldo_capital_social' not in st.session_state:
    st.session_state.saldo_capital_social = 4980000
if 'saldo_proveedores' not in st.session_state:
    st.session_state.saldo_proveedores = 0
if 'saldo_iva_trasladado' not in st.session_state:
    st.session_state.saldo_iva_trasladado = 0
if 'saldo_iva_acreditable' not in st.session_state:
    st.session_state.saldo_iva_acreditable = 0
if 'saldo_bancos' not in st.session_state:
    st.session_state.saldo_bancos = 100000
if 'equipo_computo' not in st.session_state:
    st.session_state.equipo_computo = 20000
if 'equipo_reparto' not in st.session_state:
    st.session_state.equipo_reparto = 400000
if 'muebles_enseyeres' not in st.session_state:
    st.session_state.muebles_enseyeres = 100000
if 'papeleria' not in st.session_state:
    st.session_state.papeleria = 0
if 'rentas_pagadas' not in st.session_state:
    st.session_state.rentas_pagadas = 0

# Diario general
if 'diario' not in st.session_state:
    st.session_state.diario = []

# Función para mostrar el Diario Mayor en forma de "T"
def mostrar_diario_mayor():
    st.header("Diario Mayor en Forma de T")

    # Inicializar el diccionario de cuentas dinámicamente
    cuentas = {}
    for cuenta, monto, tipo in st.session_state.diario:
        if cuenta not in cuentas:
            cuentas[cuenta] = {"Debe": [], "Haber": []}
        if tipo == "Debe":
            cuentas[cuenta]["Debe"].append(monto)
        elif tipo == "Haber":
            cuentas[cuenta]["Haber"].append(monto)

    # Mostrar cada cuenta en forma de "T"
    for cuenta, movimientos in cuentas.items():
        st.write(f"### Cuenta: {cuenta}")
        
        # Crear dos columnas para Debe y Haber
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Debe**")
            for monto in movimientos["Debe"]:
                st.markdown(f"<span style='color: green;'>{monto:,.2f}</span>", unsafe_allow_html=True)
        
        with col2:
            st.write("**Haber**")
            for monto in movimientos["Haber"]:
                st.markdown(f"<span style='color: red;'>{monto:,.2f}</span>", unsafe_allow_html=True)
        
        # Calcular y mostrar el saldo
        saldo = sum(movimientos["Debe"]) - sum(movimientos["Haber"])
        st.write(f"**Saldo**: {saldo:,.2f}")
        
        st.write("---")  # Separador entre cuentas

# Función para mostrar el balance general
def mostrar_balance_general():
    st.header("Balance General")
    
    # Calcular total de activos
    activos = (
        st.session_state.saldo_caja
        + st.session_state.saldo_mercancias
        + st.session_state.saldo_mobiliario
        + st.session_state.saldo_terreno
        + st.session_state.saldo_edificio
        + st.session_state.saldo_bancos
        + st.session_state.equipo_computo
        + st.session_state.equipo_reparto
        + st.session_state.muebles_enseyeres
        + st.session_state.papeleria
        + st.session_state.rentas_pagadas
    )
    
    # Calcular total de pasivos
    pasivos = st.session_state.saldo_proveedores + st.session_state.saldo_iva_trasladado
    
    # Calcular capital contable
    capital_contable = st.session_state.saldo_capital_social - st.session_state.saldo_iva_acreditable
    
    # Mostrar activos
    st.subheader("Activos")
    st.write(f"Caja: ${st.session_state.saldo_caja:,.2f}")
    st.write(f"Mercancías: ${st.session_state.saldo_mercancias:,.2f}")
    st.write(f"Terreno: ${st.session_state.saldo_terreno:,.2f}")
    st.write(f"Edificio: ${st.session_state.saldo_edificio:,.2f}")
    st.write(f"Total Activos: ${activos:,.2f}")
    
    # Mostrar pasivos
    st.subheader("Pasivos")
    st.write(f"Proveedores: ${st.session_state.saldo_proveedores:,.2f}")
    st.write(f"IVA Trasladado: ${st.session_state.saldo_iva_trasladado:,.2f}")
    st.write(f"Total Pasivos: ${pasivos:,.2f}")
    
    # Mostrar capital contable
    st.subheader("Capital Contable")
    st.write(f"Capital Social: ${st.session_state.saldo_capital_social:,.2f}")
    st.write(f"Total Capital Contable: ${capital_contable:,.2f}")

# Función para mostrar el diario general
def mostrar_diario():
    st.header("Diario General")
    for cuenta, monto, tipo in st.session_state.diario:
        st.write(f"{cuenta}: ${monto:,.2f} ({tipo})")

# Interfaz principal
st.title("Aplicación Contable")

# Menú de opciones
opcion = st.sidebar.selectbox(
    "Seleccione una operación:",
    [
        "Asiento de Apertura",
        "Compra en Efectivo",
        "Compra a Crédito",
        "Compra Combinada",
        "Anticipo de Clientes",
        "Compra de Papelería",
        "Pago de Rentas Anticipadas",
        "Mostrar Balance General",
        "Mostrar Diario",
        "Mostrar Diario Mayor",
    ],
)

if opcion == "Asiento de Apertura":
    st.header("Asiento de Apertura")
    capital = st.number_input("Capital Social:", value=0.0)
    if st.button("Registrar"):
        st.session_state.saldo_capital_social = capital
        st.session_state.diario.append(("Capital Social", capital, "Haber"))
        st.session_state.diario.append(("Caja", capital, "Debe"))
        st.success("Asiento de apertura registrado correctamente.")

elif opcion == "Compra en Efectivo":
    st.header("Compra en Efectivo")
    monto = st.number_input("Monto de la compra:", value=0.0)
    if st.button("Registrar"):
        if st.session_state.saldo_caja >= monto:
            st.session_state.saldo_caja -= monto
            st.session_state.saldo_mercancias += monto
            st.session_state.diario.append(("Mercancías", monto, "Debe"))
            st.session_state.diario.append(("Caja", monto, "Haber"))
            st.success("Compra en efectivo registrada correctamente.")
        else:
            st.error("Saldo insuficiente en caja.")

elif opcion == "Compra a Crédito":
    st.header("Compra a Crédito")
    monto = st.number_input("Monto de la compra:", value=0.0)
    if st.button("Registrar"):
        st.session_state.saldo_mercancias += monto
        st.session_state.saldo_proveedores += monto
        st.session_state.diario.append(("Mercancías", monto, "Debe"))
        st.session_state.diario.append(("Proveedores", monto, "Haber"))
        st.success("Compra a crédito registrada correctamente.")

elif opcion == "Compra Combinada":
    st.header("Compra Combinada")
    monto = st.number_input("Monto de la compra:", value=0.0)
    efectivo = st.number_input("Monto en efectivo:", value=0.0)
    credito = st.number_input("Monto a crédito:", value=0.0)
    if st.button("Registrar"):
        if efectivo + credito != monto:
            st.error("La suma de efectivo y crédito debe ser igual al monto total.")
        else:
            iva = monto * 0.16
            total_pago = monto + iva
            if st.session_state.saldo_caja >= efectivo:
                st.session_state.saldo_caja -= efectivo
                st.session_state.saldo_mercancias += monto
                st.session_state.saldo_proveedores += credito + iva
                st.session_state.saldo_iva_acreditable += iva
                st.session_state.diario.append(("Mercancías", monto, "Debe"))
                st.session_state.diario.append(("IVA Acreditable", iva, "Debe"))
                st.session_state.diario.append(("Caja", efectivo, "Haber"))
                st.session_state.diario.append(("Proveedores", credito + iva, "Haber"))
                st.success("Compra combinada registrada correctamente.")
            else:
                st.error("Saldo insuficiente en caja.")

elif opcion == "Anticipo de Clientes":
    st.header("Anticipo de Clientes")
    monto = st.number_input("Monto del anticipo:", value=0.0)
    if st.button("Registrar"):
        st.session_state.saldo_caja += monto
        st.session_state.diario.append(("Caja", monto, "Debe"))
        st.session_state.diario.append(("Anticipo de Clientes", monto, "Haber"))
        st.success("Anticipo de clientes registrado correctamente.")

elif opcion == "Compra de Papelería":
    st.header("Compra de Papelería")
    monto = st.number_input("Monto de la compra:", value=0.0)
    if st.button("Registrar"):
        st.session_state.saldo_caja -= monto
        st.session_state.papeleria += monto
        st.session_state.diario.append(("Papelería", monto, "Debe"))
        st.session_state.diario.append(("Caja", monto, "Haber"))
        st.success("Compra de papelería registrada correctamente.")

elif opcion == "Pago de Rentas Anticipadas":
    st.header("Pago de Rentas Anticipadas")
    monto = st.number_input("Monto del pago:", value=0.0)
    if st.button("Registrar"):
        st.session_state.saldo_caja -= monto
        st.session_state.rentas_pagadas += monto
        st.session_state.diario.append(("Rentas Pagadas por Anticipado", monto, "Debe"))
        st.session_state.diario.append(("Caja", monto, "Haber"))
        st.success("Pago de rentas registrado correctamente.")

elif opcion == "Mostrar Balance General":
    mostrar_balance_general()

elif opcion == "Mostrar Diario":
    mostrar_diario()

elif opcion == "Mostrar Diario Mayor":
    mostrar_diario_mayor()