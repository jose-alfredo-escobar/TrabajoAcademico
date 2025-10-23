import tkinter as tk


class VistaTareas:
    def __init__(self, root, modelo):
        self.root = root
        self.modelo = modelo
        self.controlador = None  # Se asigna después

        self.root.title("Lista de Tareas")

        self.entrada = tk.Entry(root, width=40)
        self.entrada.pack(pady=5)

        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

    def configurar_botones(self):
        tk.Button(self.root, text="Agregar tarea", command=self.controlador.agregar).pack()
        tk.Button(self.root, text="Marcar como completada", command=self.controlador.completar).pack()
        tk.Button(self.root, text="Eliminar tarea", command=self.controlador.eliminar).pack()

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for descripcion, estado in self.modelo.obtener_tareas():
            self.lista.insert(tk.END, f"{descripcion} [{estado}]")
