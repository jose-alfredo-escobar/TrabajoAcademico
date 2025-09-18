import tkinter as tk
import json


class Nodo:
    def __init__(self, coeficiente, grado):
        self.__coeficiente = coeficiente
        self.__grado = grado
        self.__siguiente = None

    def get_coeficiente(self):
        return self.__coeficiente

    def set_coeficiente(self, valor):
        self.__coeficiente = valor

    def get_grado(self):
        return self.__grado

    def set_grado(self, valor):
        self.__grado = valor

    def get_siguiente(self):
        return self.__siguiente

    def set_siguiente(self, nodo):
        self.__siguiente = nodo


class Polinomio:
    def __init__(self):
        self.inicio = None

    def agregar_termino(self, coeficiente, grado):
        if coeficiente == 0:
            return
        nuevo = Nodo(coeficiente, grado)
        if not self.inicio or grado > self.inicio.get_grado():
            nuevo.set_siguiente(self.inicio)
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.get_siguiente() and actual.get_siguiente().get_grado() > grado:
                actual = actual.get_siguiente()
            if actual.get_grado() == grado:
                actual.set_coeficiente(actual.get_coeficiente() + coeficiente)
            elif actual.get_siguiente() and actual.get_siguiente().get_grado() == grado:
                siguiente = actual.get_siguiente()
                siguiente.set_coeficiente(siguiente.get_coeficiente() + coeficiente)
            else:
                nuevo.set_siguiente(actual.get_siguiente())
                actual.set_siguiente(nuevo)

    def obtener_terminos(self):
        actual = self.inicio
        lista = []
        while actual:
            lista.append((actual.get_coeficiente(), actual.get_grado()))
            actual = actual.get_siguiente()
        return lista

    def imprimir(self):
        partes = []
        actual = self.inicio
        while actual:
            coef = int(round(actual.get_coeficiente()))
            grado = actual.get_grado()
            if coef != 0:
                if grado == 0:
                    partes.append(f"{coef}")
                elif grado == 1:
                    partes.append(f"{coef}x")
                else:
                    partes.append(f"{coef}x^{grado}")
            actual = actual.get_siguiente()
        print(" + ".join(partes) if partes else "0")

    def evaluar(self, x):
        resultado = 0
        actual = self.inicio
        while actual:
            resultado += actual.get_coeficiente() * (x ** actual.get_grado())
            actual = actual.get_siguiente()
        return resultado

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            json.dump(self.obtener_terminos(), archivo)
        print(f"Polinomio guardado en '{nombre_archivo}'")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                terminos = json.load(archivo)
            for coef, grado in terminos:
                self.agregar_termino(coef, grado)
            print(f"Polinomio cargado desde '{nombre_archivo}'")
        except Exception as e:
            print(f"Error al cargar: {e}")

    def copiar(self):
        copia = Polinomio()
        for coef, grado in self.obtener_terminos():
            copia.agregar_termino(coef, grado)
        return copia

    def sumar(self, otro):
        resultado = self.copiar()
        for coef, grado in otro.obtener_terminos():
            resultado.agregar_termino(coef, grado)
        return resultado

    def restar(self, otro):
        resultado = self.copiar()
        for coef, grado in otro.obtener_terminos():
            resultado.agregar_termino(-coef, grado)
        return resultado

    def multiplicar(self, otro):
        resultado = Polinomio()
        for coef1, grado1 in self.obtener_terminos():
            for coef2, grado2 in otro.obtener_terminos():
                resultado.agregar_termino(coef1 * coef2, grado1 + grado2)
        return resultado

    def dividir(self, divisor):
        dividendo = self.copiar()
        cociente = Polinomio()

        while dividendo.inicio and dividendo.inicio.get_grado() >= divisor.inicio.get_grado():
            grado_d = dividendo.inicio.get_grado()
            grado_v = divisor.inicio.get_grado()
            coef_d = dividendo.inicio.get_coeficiente()
            coef_v = divisor.inicio.get_coeficiente()

            nuevo_coef = coef_d / coef_v
            nuevo_grado = grado_d - grado_v

            temp = Polinomio()
            temp.agregar_termino(nuevo_coef, nuevo_grado)
            cociente.agregar_termino(nuevo_coef, nuevo_grado)
            producto = divisor.multiplicar(temp)
            dividendo = dividendo.restar(producto)

        return cociente, dividendo


def mostrar_polinomio_canvas(polinomio, titulo="Polinomio"):
    ventana = tk.Tk()
    ventana.title(titulo)
    canvas = tk.Canvas(ventana, width=800, height=400, bg="white")
    canvas.pack()

    x = 50
    y = 100
    radio = 40
    for coef, grado in polinomio.obtener_terminos():
        texto = f"{int(coef)}x^{grado}" if grado != 0 else f"{int(coef)}"
        canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="#add8e6")
        canvas.create_text(x, y, text=texto, font=("Arial", 12, "bold"))
        x += 100

    canvas.create_line(50, 300, 750, 300, arrow=tk.LAST)
    canvas.create_line(400, 50, 400, 350, arrow=tk.LAST)

    puntos = []
    for px in range(-100, 100):
        x_canvas = 400 + px * 2
        y_valor = polinomio.evaluar(px)
        y_canvas = 300 - y_valor * 0.5
        puntos.append((x_canvas, y_canvas))

    for i in range(len(puntos) - 1):
        canvas.create_line(*puntos[i], *puntos[i + 1], fill="red")

    ventana.mainloop()


def construir_polinomio(nombre):
    print(f"\n Construye el polinomio {nombre}:")
    p = Polinomio()
    while True:
        entrada = input("→ coef,grado (o 'fin'): ")
        if entrada.lower() == "fin":
            break
        try:
            coef, grado = map(int, entrada.split(","))
            p.agregar_termino(coef, grado)
        except ValueError:
            print(" Formato inválido. Usa: coeficiente,grado")
    return p


if __name__ == "__main__":
    print("=== Proyecto ADT Persistente de Polinomios ===")
    print("1. Crear dos polinomios")
    print("2. Cargar polinomio desde archivo")
    opcion = input("Selecciona opción (1 o 2): ")

    if opcion == "1":
        p1 = construir_polinomio("P1")
        p2 = construir_polinomio("P2")

        print("\n P1:")
        p1.imprimir()
        print(" P2:")
        p2.imprimir()

        suma = p1.sumar(p2)
        resta = p1.restar(p2)
        producto = p1.multiplicar(p2)
        cociente, residuo = p1.dividir(p2)

        print("\n Suma:")
        suma.imprimir()
        print(" Resta:")
        resta.imprimir()
        print(" Multiplicación:")
        producto.imprimir()
        print(" División - Cociente:")
        cociente.imprimir()
        print(" División - Residuo:")
        residuo.imprimir()

        guardar = input("\n¿Guardar P1? (s/n): ")
        if guardar.lower() == "s":
            nombre = input("Nombre del archivo (ej: p1.json): ")
            p1.guardar_en_archivo(nombre)

        mostrar_polinomio_canvas(suma, "Suma P1 + P2")

    elif opcion == "2":
        nombre = input("Nombre del archivo a cargar: ")
        p = Polinomio()
        p.cargar_desde_archivo(nombre)
        print("\n Polinomio cargado:")
        p.imprimir()
        mostrar_polinomio_canvas(p, "Visualización del Polinomio")

