import tkinter as tk


class Nodo:
    """Nodo que representa un término de un polinomio con encapsulamiento."""

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
    """Lista enlazada para representar un polinomio."""

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

    def copiar(self):
        copia = Polinomio()
        actual = self.inicio
        while actual:
            copia.agregar_termino(actual.get_coeficiente(), actual.get_grado())
            actual = actual.get_siguiente()
        return copia

    def grado_maximo(self):
        return self.inicio.get_grado() if self.inicio else -1

    def coeficiente_grado(self, grado):
        actual = self.inicio
        while actual:
            if actual.get_grado() == grado:
                return actual.get_coeficiente()
            actual = actual.get_siguiente()
        return 0

    def evaluar(self, x):
        resultado = 0
        actual = self.inicio
        while actual:
            resultado += actual.get_coeficiente() * (x ** actual.get_grado())
            actual = actual.get_siguiente()
        return resultado

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

    def sumar(self, otro):
        resultado = self.copiar()
        actual = otro.inicio
        while actual:
            resultado.agregar_termino(actual.get_coeficiente(), actual.get_grado())
            actual = actual.get_siguiente()
        return resultado

    def restar(self, otro):
        resultado = self.copiar()
        actual = otro.inicio
        while actual:
            resultado.agregar_termino(-actual.get_coeficiente(), actual.get_grado())
            actual = actual.get_siguiente()
        return resultado

    def multiplicar(self, otro):
        resultado = Polinomio()
        actual1 = self.inicio
        while actual1:
            actual2 = otro.inicio
            while actual2:
                coef = actual1.get_coeficiente() * actual2.get_coeficiente()
                grado = actual1.get_grado() + actual2.get_grado()
                resultado.agregar_termino(coef, grado)
                actual2 = actual2.get_siguiente()
            actual1 = actual1.get_siguiente()
        return resultado

    def multiplicar_por_termino(self, coef, grado):
        resultado = Polinomio()
        actual = self.inicio
        while actual:
            nuevo_coef = actual.get_coeficiente() * coef
            nuevo_grado = actual.get_grado() + grado
            resultado.agregar_termino(nuevo_coef, nuevo_grado)
            actual = actual.get_siguiente()
        return resultado

    def dividir(self, divisor):
        dividendo = self.copiar()
        cociente = Polinomio()

        while dividendo.inicio and dividendo.grado_maximo() >= divisor.grado_maximo():
            grado_d = dividendo.grado_maximo()
            grado_v = divisor.grado_maximo()
            coef_d = dividendo.coeficiente_grado(grado_d)
            coef_v = divisor.coeficiente_grado(grado_v)

            nuevo_coef = coef_d / coef_v
            nuevo_grado = grado_d - grado_v

            cociente.agregar_termino(nuevo_coef, nuevo_grado)
            producto = divisor.multiplicar_por_termino(nuevo_coef, nuevo_grado)
            dividendo = dividendo.restar(producto)

        return cociente, dividendo


def mostrar_polinomio_canvas(polinomio):
    ventana = tk.Tk()
    ventana.title("Visualización de Polinomio")
    canvas = tk.Canvas(ventana, width=800, height=400, bg="white")
    canvas.pack()

    # Dibujar nodos
    x = 50
    y = 100
    radio = 40
    terminos = polinomio.obtener_terminos()

    for i, (coef, grado) in enumerate(terminos):
        texto = f"{int(coef)}x^{grado}" if grado != 0 else f"{int(coef)}"
        canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="#add8e6")
        canvas.create_text(x, y, text=texto, font=("Arial", 12, "bold"))
        if i < len(terminos) - 1:
            canvas.create_line(x + radio, y, x + 2 * radio, y, arrow=tk.LAST)
        x += 100

    # Ejes cartesianos
    canvas.create_line(50, 300, 750, 300, arrow=tk.LAST)
    canvas.create_line(400, 50, 400, 350, arrow=tk.LAST)
    canvas.create_text(760, 300, text="x", font=("Arial", 10))
    canvas.create_text(400, 40, text="y", font=("Arial", 10))

    # Graficar curva
    puntos = []
    for px in range(-100, 100):
        x_canvas = 400 + px * 2
        y_valor = polinomio.evaluar(px)
        y_canvas = 300 - y_valor * 0.5
        puntos.append((x_canvas, y_canvas))

    for i in range(len(puntos) - 1):
        x1, y1 = puntos[i]
        x2, y2 = puntos[i + 1]
        canvas.create_line(x1, y1, x2, y2, fill="red")

    ventana.mainloop()


# Ejemplo de uso
if __name__ == "__main__":
    p1 = Polinomio()
    p1.agregar_termino(3, 2)
    p1.agregar_termino(2, 0)

    p2 = Polinomio()
    p2.agregar_termino(1, 1)
    p2.agregar_termino(1, 0)

    print("Polinomio 1:")
    p1.imprimir()

    print("Polinomio 2:")
    p2.imprimir()

    print("Suma:")
    p1.sumar(p2).imprimir()

    print("Resta:")
    p1.restar(p2).imprimir()

    print("Multiplicación:")
    p1.multiplicar(p2).imprimir()

    print("División:")
    cociente, residuo = p1.dividir(p2)
    print("Cociente:")
    cociente.imprimir()
    print("Residuo:")
    residuo.imprimir()

    mostrar_polinomio_canvas(p1)
