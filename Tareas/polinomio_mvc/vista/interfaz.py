import tkinter as tk
from tkinter import messagebox

class Polinomio:
    def __init__(self, terminos):
        self.terminos = terminos  # lista de (coeficiente, exponente)

    def __str__(self):
        partes = []
        for coef, exp in sorted(self.terminos, key=lambda x: -x[1]):
            if coef == 0:
                continue
            parte = f"{coef}x^{exp}" if exp != 0 else f"{coef}"
            partes.append(parte)
        return " + ".join(partes) if partes else "0"

    def operar(self, otro, op):
        resultado = {}
        for coef, exp in self.terminos:
            resultado[exp] = resultado.get(exp, 0) + coef
        for coef, exp in otro.terminos:
            if op == '+':
                resultado[exp] = resultado.get(exp, 0) + coef
            elif op == '-':
                resultado[exp] = resultado.get(exp, 0) - coef
        return Polinomio([(c, e) for e, c in resultado.items() if c != 0])

    def multiplicar(self, otro):
        resultado = {}
        for c1, e1 in self.terminos:
            for c2, e2 in otro.terminos:
                exp = e1 + e2
                coef = c1 * c2
                resultado[exp] = resultado.get(exp, 0) + coef
        return Polinomio([(c, e) for e, c in resultado.items() if c != 0])

def parse_entrada(entrada):
    # Formato: coef,exp;coef,exp;...
    terminos = []
    for par in entrada.split(';'):
        try:
            coef, exp = map(int, par.split(','))
            terminos.append((coef, exp))
        except:
            continue
    return Polinomio(terminos)

class PolinomioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones con Polinomios")

        tk.Label(root, text="Polinomio 1 (coef,exp;...):").grid(row=0, column=0)
        self.entrada1 = tk.Entry(root, width=30)
        self.entrada1.grid(row=0, column=1)

        tk.Label(root, text="Polinomio 2 (coef,exp;...):").grid(row=1, column=0)
        self.entrada2 = tk.Entry(root, width=30)
        self.entrada2.grid(row=1, column=1)

        tk.Button(root, text="Sumar", command=self.sumar).grid(row=2, column=0)
        tk.Button(root, text="Restar", command=self.restar).grid(row=2, column=1)
        tk.Button(root, text="Multiplicar", command=self.multiplicar).grid(row=3, column=0)
        tk.Button(root, text="Dividir", command=self.dividir).grid(row=3, column=1)

    def mostrar_resultado(self, resultado):
        messagebox.showinfo("Resultado", str(resultado))

    def sumar(self):
        p1 = parse_entrada(self.entrada1.get())
        p2 = parse_entrada(self.entrada2.get())
        resultado = p1.operar(p2, '+')
        self.mostrar_resultado(resultado)

    def restar(self):
        p1 = parse_entrada(self.entrada1.get())
        p2 = parse_entrada(self.entrada2.get())
        resultado = p1.operar(p2, '-')
        self.mostrar_resultado(resultado)

    def multiplicar(self):
        p1 = parse_entrada(self.entrada1.get())
        p2 = parse_entrada(self.entrada2.get())
        resultado = p1.multiplicar(p2)
        self.mostrar_resultado(resultado)

    def dividir(self):
        messagebox.showinfo("División", "La división de polinomios no está implementada.")