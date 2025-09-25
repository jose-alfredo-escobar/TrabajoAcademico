class Polinomio:
    def __init__(self, coeficientes):
        """
        Inicializa un polinomio con una lista de coeficientes.
        Ejemplo: [3, 0, 2] representa 3 + 0x + 2x²
        """
        self.coeficientes = coeficientes

    def __str__(self):
        partes = []
        for i, coef in enumerate(self.coeficientes):
            if coef != 0:
                termino = f"{coef}x^{i}" if i > 0 else str(coef)
                partes.append(termino)
        return " + ".join(partes[::-1]) if partes else "0"
