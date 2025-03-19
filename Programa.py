import tkinter as tk
from tkinter import ttk, messagebox

class AplicacionContable:
    def __init__(self, root):  # Corregido: __init__
        self.root = root
        self.root.title("Aplicación Contable")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.saldo_caja = 30000
        self.saldo_mercancias = 10000
        self.saldo_mobiliario = 20000
        self.saldo_terreno = 2800000
        self.saldo_edificio = 1500000
        self.saldo_capital_social = 4980000
        self.saldo_proveedores = 0
        self.saldo_iva_trasladado = 0
        self.saldo_iva_acreditable = 0
        self.saldo_bancos = 100000
        self.equipo_computo = 20000
        self.equipo_reparto = 400000
        self.muebles_enseyeres = 100000
        self.papeleria = 0
        self.rentas_pagadas = 0

        self.diario = []

        self._crear_interfaz()
        
    def _crear_interfaz(self):
        tk.Label(self.root, text="Seleccione una operación:", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=20)

        btn_asiento_apertura = ttk.Button(self.root, text="Asiento de Apertura", command=self.mostrar_asiento_apertura)
        btn_asiento_apertura.pack(pady=10)

        btn_compra_efectivo = ttk.Button(self.root, text="Compra en Efectivo", command=self.mostrar_compra_efectivo)
        btn_compra_efectivo.pack(pady=10)

        btn_balance = ttk.Button(self.root, text="Mostrar Balance General", command=self.mostrar_balance_general)
        btn_balance.pack(pady=20)
        
    def mostrar_asiento_apertura(self):
        messagebox.showinfo("Info", "Función Asiento de Apertura aún no implementada.")

    def mostrar_compra_efectivo(self):
        messagebox.showinfo("Info", "Función Compra en Efectivo aún no implementada.")

    def mostrar_balance_general(self):
        messagebox.showinfo("Info", "Función Balance General aún no implementada.")

if __name__ == "__main__":  # Corregido: __name__
    root = tk.Tk()
    app = AplicacionContable(root)
    root.mainloop()
