class ControladorTareas:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def agregar(self):
        titulo = self.vista.entrada_titulo.get()
        detalle = self.vista.entrada_detalle.get()
        if titulo:
            self.modelo.agregar_tarea(titulo, detalle)
            self.vista.entrada_titulo.delete(0, 'end')
            self.vista.entrada_detalle.delete(0, 'end')
            self.vista.actualizar_lista()

    def completar(self):
        seleccion = self.vista.lista_titulos.curselection()
        if seleccion:
            titulo = self.vista.lista_titulos.get(seleccion[0]).split(" [")[0]
            self.modelo.marcar_como_completada(titulo)
            self.vista.actualizar_lista()

    def eliminar(self):
        seleccion = self.vista.lista_titulos.curselection()
        if seleccion:
            titulo = self.vista.lista_titulos.get(seleccion[0]).split(" [")[0]
            self.modelo.eliminar_tarea(titulo)
            self.vista.actualizar_lista()
