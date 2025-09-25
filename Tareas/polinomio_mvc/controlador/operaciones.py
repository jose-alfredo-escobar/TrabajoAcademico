from modelo.polinomio import Polinomio

def sumar(p1, p2):
    max_len = max(len(p1.coeficientes), len(p2.coeficientes))
    resultado = [
        (p1.coeficientes[i] if i < len(p1.coeficientes) else 0) +
        (p2.coeficientes[i] if i < len(p2.coeficientes) else 0)
        for i in range(max_len)
    ]
    return Polinomio(resultado)

def restar(p1, p2):
    max_len = max(len(p1.coeficientes), len(p2.coeficientes))
    resultado = [
        (p1.coeficientes[i] if i < len(p1.coeficientes) else 0) -
        (p2.coeficientes[i] if i < len(p2.coeficientes) else 0)
        for i in range(max_len)
    ]
    return Polinomio(resultado)

def multiplicar(p1, p2):
    resultado = [0] * (len(p1.coeficientes) + len(p2.coeficientes) - 1)
    for i, a in enumerate(p1.coeficientes):
        for j, b in enumerate(p2.coeficientes):
            resultado[i + j] += a * b
    return Polinomio(resultado)

def dividir(p1, p2):
    if not any(p2.coeficientes):
        raise ZeroDivisionError("No se puede dividir por el polinomio cero.")

    dividendo = p1.coeficientes[:]
    divisor = p2.coeficientes[:]
    cociente = [0] * (len(dividendo) - len(divisor) + 1)

    while len(dividendo) >= len(divisor):
        grado_diff = len(dividendo) - len(divisor)
        coef = dividendo[-1] / divisor[-1]
        cociente[grado_diff] = coef

        for i in range(len(divisor)):
            dividendo[grado_diff + i] -= coef * divisor[i]
        dividendo.pop()

    return Polinomio(cociente)
