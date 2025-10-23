from modelo import ListaTareas


class ControladorTareas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregar(self):
        descripcion = self.vista.entrada.get()
        if descripcion:
            self.modelo.agregar_tarea(descripcion)
            self.vista.entrada.delete(0, 'end')
            self.vista.actualizar_lista()

    def completar(self):
        seleccion = self.vista.lista.curselection()
        if seleccion:
            descripcion = self.vista.lista.get(seleccion[0]).split(" [")[0]
            self.modelo.marcar_como_completada(descripcion)
            self.vista.actualizar_lista()

    def eliminar(self):
        seleccion = self.vista.lista.curselection()
        if seleccion:
            descripcion = self.vista.lista.get(seleccion[0]).split(" [")[0]
            self.modelo.eliminar_tarea(descripcion)
            self.vista.actualizar_lista()
