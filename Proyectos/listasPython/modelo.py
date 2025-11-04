from datetime import datetime

class NodoTarea:
    def __init__(self, titulo, detalle, estado='pendiente'):
        self.titulo = titulo
        self.detalle = detalle
        self.estado = estado
        self.fecha_creacion = datetime.now()
        self.siguiente = None  # ← clave para lista enlazada

    def alternar_estado(self):
        self.estado = 'completada' if self.estado == 'pendiente' else 'pendiente'

#gestiona la lista enlazada de tareas
#permite hacer operaciones como agregar, completar, eliminar y obtener tareas
class ListaTareas:
    def __init__(self):
        self.inicio = None

    def agregar_tarea(self, titulo, detalle):
        nuevo = NodoTarea(titulo, detalle)
        if not self.inicio:
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def marcar_como_completada(self, titulo):
        actual = self.inicio
        while actual:
            if actual.titulo == titulo:
                actual.alternar_estado()
                return True
            actual = actual.siguiente
        return False

    def eliminar_tarea(self, titulo):
        actual = self.inicio
        anterior = None
        while actual:
            if actual.titulo == titulo:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def obtener_tareas(self):
        tareas = []
        actual = self.inicio
        while actual:
            tareas.append(actual)
            actual = actual.siguiente
        return tareas


