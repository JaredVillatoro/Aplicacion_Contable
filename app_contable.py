import streamlit as st
from datetime import datetime

# ========== CONFIGURACIÓN INICIAL ==========
st.set_page_config(page_title="Sistema Contable Completo", layout="wide")
st.title("📊 Sistema Contable - Tío Frank")

# ========== VARIABLES DE ESTADO (TU CÓDIGO ORIGINAL + MEJORAS) ==========
if 'diario' not in st.session_state:
    st.session_state.diario = []

if 'cuentas' not in st.session_state:
    st.session_state.cuentas = {
        # Activos (valores iniciales de tu código + imágenes)
        'Caja': {'saldo': 30000, 'tipo': 'Activo Circulante'},
        'Bancos': {'saldo': 100000, 'tipo': 'Activo Circulante'},
        'Mercancías': {'saldo': 10000, 'tipo': 'Activo Circulante'},
        'Terrenos': {'saldo': 2800000, 'tipo': 'Activo No Circulante', 'dep_acum': 0},
        'Edificios': {'saldo': 1500000, 'tipo': 'Activo No Circulante', 'dep_acum': 0},
        'Equipo de Cómputo': {'saldo': 20000, 'tipo': 'Activo No Circulante', 'dep_acum': 0},
        'Equipo de Reparto': {'saldo': 400000, 'tipo': 'Activo No Circulante', 'dep_acum': 0},
        'Muebles y Enseres': {'saldo': 100000, 'tipo': 'Activo No Circulante', 'dep_acum': 0},
        'Papelería': {'saldo': 0, 'tipo': 'Activo Circulante'},
        'Rentas Pagadas': {'saldo': 0, 'tipo': 'Activo Circulante'},
        
        # Pasivos y Capital (de tus imágenes)
        'Proveedores': {'saldo': 0, 'tipo': 'Pasivo'},
        'Documentos por Pagar': {'saldo': 0, 'tipo': 'Pasivo'},
        'IVA Trasladado': {'saldo': 0, 'tipo': 'Pasivo'},
        'Anticipo de Clientes': {'saldo': 0, 'tipo': 'Pasivo'},
        'Capital Social': {'saldo': 4980000, 'tipo': 'Capital'},
        'Utilidad del Ejercicio': {'saldo': 0, 'tipo': 'Capital'}
    }

# ========== FUNCIONES DE OPERACIONES (TU CÓDIGO ORIGINAL) ==========
def registrar_asiento_apertura():
    capital = st.number_input("Capital Social:", value=0.0)
    if st.button("Registrar Asiento de Apertura"):
        st.session_state.cuentas['Capital Social']['saldo'] = capital
        st.session_state.cuentas['Caja']['saldo'] += capital
        st.session_state.diario.append(("Capital Social", capital, "Haber"))
        st.session_state.diario.append(("Caja", capital, "Debe"))
        st.success("¡Asiento registrado!")

def registrar_compra_efectivo():
    monto = st.number_input("Monto de compra:", value=0.0)
    if st.button("Registrar Compra en Efectivo"):
        st.session_state.cuentas['Caja']['saldo'] -= monto
        st.session_state.cuentas['Mercancías']['saldo'] += monto
        st.session_state.diario.append(("Mercancías", monto, "Debe"))
        st.session_state.diario.append(("Caja", monto, "Haber"))
        st.success("¡Compra registrada!")

# ... (Aquí irían TODAS tus funciones originales: compra a crédito, anticipos, etc.)

# ========== FUNCIONES DE REPORTES PROFESIONALES (DE TUS IMÁGENES) ==========
def mostrar_balance_profesional():
    st.header(f"Balance General al {datetime.now().strftime('%d/%m/%Y')}")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Activo")
        st.write("**Circulante**")
        st.write(f"Caja: ${st.session_state.cuentas['Caja']['saldo']:,.2f}")
        st.write(f"Bancos: ${st.session_state.cuentas['Bancos']['saldo']:,.2f}")
        # ... (lista completa de activos circulantes)
        
        st.write("**No Circulante**")
        st.write(f"Terrenos: ${st.session_state.cuentas['Terrenos']['saldo']:,.2f}")
        # ... (lista completa de activos no circulantes)

    with col2:
        st.subheader("Pasivo")
        st.write(f"Proveedores: ${st.session_state.cuentas['Proveedores']['saldo']:,.2f}")
        # ... (lista completa de pasivos)

    with col3:
        st.subheader("Capital")
        st.write(f"Capital Social: ${st.session_state.cuentas['Capital Social']['saldo']:,.2f}")
        # ... (lista completa de capital)

def mostrar_estado_resultados():
    st.header("Estado de Resultados")
    utilidad_bruta = 105000 - 50000  # Ejemplo basado en tus imágenes
    st.table({
        "Concepto": ["Ventas", "Costo de Ventas", "Utilidad Bruta", "Gastos Generales", "Utilidad del Ejercicio"],
        "Monto": ["$105,000", "$50,000", "$55,000", "$13,292", "$41,708"]
    })

# ========== INTERFAZ PRINCIPAL ==========
menu_principal = st.sidebar.radio(
    "Menú Principal",
    ["Operaciones Contables", "Reportes Financieros"]
)

if menu_principal == "Operaciones Contables":
    st.header("📝 Registrar Operaciones")
    opcion = st.selectbox(
        "Seleccione una operación:",
        ["Asiento de Apertura", "Compra en Efectivo", "Compra a Crédito", "..."]  # Todas tus opciones originales
    )
    
    if opcion == "Asiento de Apertura":
        registrar_asiento_apertura()
    elif opcion == "Compra en Efectivo":
        registrar_compra_efectivo()
    # ... (todas las demás operaciones)

elif menu_principal == "Reportes Financieros":
    st.header("📊 Reportes Profesionales")
    reporte = st.selectbox(
        "Seleccione un reporte:",
        ["Balance General", "Estado de Resultados", "Flujo de Efectivo"]
    )
    
    if reporte == "Balance General":
        mostrar_balance_profesional()
    elif reporte == "Estado de Resultados":
        mostrar_estado_resultados()
    # ... (otros reportes)