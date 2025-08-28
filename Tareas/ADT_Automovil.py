class AutomovilEstatico:
    """
    Representa un automóvil con atributos fijos.
    """

    def __init__(self, marca, modelo, año):
        """
        Inicializa un automóvil con marca, modelo y año.
        """
        self._marca = marca
        self._modelo = modelo
        self._año = año

    def get_marca(self):
        """
        Devuelve la marca del automóvil.
        """
        return self._marca

    def get_modelo(self):
        """
        Devuelve el modelo del automóvil.
        """
        return self._modelo

    def get_año(self):
        """
        Devuelve el año del automóvil.
        """
        return self._año

    def set_marca(self, nueva_marca):
        """
        Actualiza la marca del automóvil.
        """
        self._marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        """
        Actualiza el modelo del automóvil.
        """
        self._modelo = nuevo_modelo

    def set_año(self, nuevo_año):
        """
        Actualiza el año del automóvil.
        """
        self._año = nuevo_año


class AutomovilDinamico:
    """
    Representa un automóvil con atributos dinámicos.
    """

    def __init__(self):
        """
        Inicializa un diccionario vacío de atributos.
        """
        self._atributos = {}

    def set_atributo(self, clave, valor):
        """
        Asigna un valor a un atributo dinámico.
        """
        self._atributos[clave] = valor

    def get_atributo(self, clave):
        """
        Devuelve el valor de un atributo, si existe.
        """
        return self._atributos.get(clave, "Atributo no encontrado")

    def mostrar_atributos(self):
        """
        Muestra todos los atributos del automóvil.
        """
        for clave, valor in self._atributos.items():
            print(f"{clave}: {valor}")


def pruebas_estatico():
    """
    Prueba básica de la clase AutomovilEstatico.
    """
    print("🔧 Prueba AutomovilEstatico")
    auto = AutomovilEstatico("Toyota", "Corolla", 2020)
    print("Marca:", auto.get_marca())
    print("Modelo:", auto.get_modelo())
    print("Año:", auto.get_año())
    auto.set_modelo("Yaris")
    print("Modelo actualizado:", auto.get_modelo())


def pruebas_dinamico():
    """
    Prueba básica de la clase AutomovilDinamico.
    """
    print("\n🔧 Prueba AutomovilDinamico")
    auto = AutomovilDinamico()
    auto.set_atributo("marca", "Honda")
    auto.set_atributo("modelo", "Civic")
    auto.set_atributo("color", "Azul")
    print("Modelo:", auto.get_atributo("modelo"))
    auto.mostrar_atributos()


if __name__ == "__main__":
    pruebas_estatico()
    pruebas_dinamico()
