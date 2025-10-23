class Tarea:
    def __init__(self, descripcion):
        self._descripcion = descripcion
        self._estado = 'pendiente'

    def get_descripcion(self):
        return self._descripcion

    def get_estado(self):
        return self._estado

    def set_estado(self, estado):
        self._estado = estado


class ListaTareas:
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, descripcion):
        self._tareas.append(Tarea(descripcion))

    def marcar_como_completada(self, descripcion):
        for tarea in self._tareas:
            if tarea.get_descripcion() == descripcion:
                tarea.set_estado('completada')
                return True
        return False

    def eliminar_tarea(self, descripcion):
        for tarea in self._tareas:
            if tarea.get_descripcion() == descripcion:
                self._tareas.remove(tarea)
                return True
        return False

    def obtener_tareas(self):
        return [(t.get_descripcion(), t.get_estado()) for t in self._tareas]
