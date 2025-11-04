import tkinter as tk
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Ajuste para formato en español

class VistaTareas:
    def __init__(self, root, modelo):
        self.root = root
        self.modelo = modelo
        self.controlador = None

        self.root.title("Lista de Tareas (Lista Enlazada)")

        # Parte superior: entrada de nueva tarea alineada verticalmente
        self.panel_superior = tk.Frame(root)
        self.panel_superior.pack(pady=10)

        tk.Label(self.panel_superior, text="Título:").pack(anchor='w')
        self.entrada_titulo = tk.Entry(self.panel_superior, width=40)
        self.entrada_titulo.pack(pady=2)

        tk.Label(self.panel_superior, text="Descripción:").pack(anchor='w')
        self.entrada_detalle = tk.Entry(self.panel_superior, width=40)
        self.entrada_detalle.pack(pady=2)

        self.botones = tk.Frame(self.panel_superior)
        self.botones.pack(pady=5)
        tk.Button(self.botones, text="Agregar tarea", command=self.controlador_agregar).pack(side='left', padx=5)
        tk.Button(self.botones, text="Marcar como completada", command=self.controlador_completar).pack(side='left', padx=5)
        tk.Button(self.botones, text="Eliminar tarea", command=self.controlador_eliminar).pack(side='left', padx=5)
        tk.Button(self.botones, text="Buscar tarea", command=self.buscar_tarea).pack(side='left', padx=5)

        # Parte inferior: lista de tareas y detalle seleccionado
        self.panel_inferior = tk.Frame(root)
        self.panel_inferior.pack(padx=10, pady=10)

        # Izquierda: lista de títulos
        self.panel_lista = tk.Frame(self.panel_inferior)
        self.panel_lista.pack(side='left', padx=5)

        self.lista_titulos = tk.Listbox(self.panel_lista, width=40, height=10)
        self.lista_titulos.pack()
        self.lista_titulos.bind('<<ListboxSelect>>', self.mostrar_detalle_tarea)

        self.total_tareas_label = tk.Label(self.panel_lista, text="Total de tareas: 0", fg="black", font=("Arial", 10))
        self.total_tareas_label.pack(anchor='w', pady=5)

        # Derecha: solo contenido sin etiquetas ni bordes
        self.panel_detalle = tk.Frame(self.panel_inferior)
        self.panel_detalle.pack(side='left', padx=10)

        self.mostrar_titulo = tk.Text(
            self.panel_detalle,
            height=1,
            width=40,
            font=("Arial", 14, "bold"),
            wrap='none',
            bd=0,
            bg=self.root.cget('bg'),
            cursor='arrow',
            highlightthickness=0
        )
        self.mostrar_titulo.pack(anchor='w', pady=2)
        self.mostrar_titulo.config(state='disabled')

        self.mostrar_detalle = tk.Text(
            self.panel_detalle,
            height=5,
            width=40,
            wrap='word',
            bd=0,
            bg=self.root.cget('bg'),
            cursor='arrow',
            highlightthickness=0
        )
        self.mostrar_detalle.pack(anchor='w', pady=2)
        self.mostrar_detalle.config(state='disabled')

        self.mostrar_fecha = tk.Text(
            self.panel_detalle,
            height=1,
            width=40,
            font=("Arial", 10),
            fg="#666666",  # gris medio transparente
            wrap='none',
            bd=0,
            bg=self.root.cget('bg'),
            cursor='arrow',
            highlightthickness=0
        )
        self.mostrar_fecha.pack(anchor='w', pady=2)
        self.mostrar_fecha.config(state='disabled')

    def configurar_botones(self):
        pass

    def controlador_agregar(self):
        if self.controlador:
            self.controlador.agregar()

    def controlador_completar(self):
        if self.controlador:
            self.controlador.completar()

    def controlador_eliminar(self):
        if self.controlador:
            self.controlador.eliminar()

    def actualizar_lista(self):
        self.lista_titulos.delete(0, tk.END)
        tareas = self.modelo.obtener_tareas()
        for i, tarea in enumerate(tareas):
            texto = f"{tarea.titulo} [{tarea.estado}]"
            self.lista_titulos.insert(tk.END, texto)
            color = 'green' if tarea.estado == 'pendiente' else 'red'
            self.lista_titulos.itemconfig(i, {'fg': color})
        self.total_tareas_label.config(text=f"Total de tareas: {len(tareas)}")

    def mostrar_detalle_tarea(self, event):
        seleccion = self.lista_titulos.curselection()
        if seleccion:
            self._mostrar_por_indice(seleccion[0])
        else:
            self._limpiar_detalle()

    def buscar_tarea(self):
        texto_busqueda = self.entrada_titulo.get().strip().lower()
        tareas = self.modelo.obtener_tareas()
        for i, tarea in enumerate(tareas):
            if tarea.titulo.lower() == texto_busqueda:
                self.lista_titulos.selection_clear(0, tk.END)
                self.lista_titulos.selection_set(i)
                self.lista_titulos.activate(i)
                self._mostrar_por_indice(i)
                return
        self.mostrar_titulo.config(state='normal', fg='black')
        self.mostrar_titulo.delete('1.0', tk.END)
        self.mostrar_titulo.insert(tk.END, "Tarea no encontrada")
        self.mostrar_titulo.config(state='disabled')

        self.mostrar_detalle.config(state='normal')
        self.mostrar_detalle.delete('1.0', tk.END)
        self.mostrar_detalle.config(state='disabled')

        self.mostrar_fecha.config(state='normal')
        self.mostrar_fecha.delete('1.0', tk.END)
        self.mostrar_fecha.config(state='disabled')

    def _mostrar_por_indice(self, indice):
        tareas = self.modelo.obtener_tareas()
        if 0 <= indice < len(tareas):
            tarea = tareas[indice]
            color = 'green' if tarea.estado == 'pendiente' else 'red'

            fecha_formateada = tarea.fecha_creacion.strftime("%d de %B de %Y")

            self.mostrar_titulo.config(state='normal', fg=color)
            self.mostrar_titulo.delete('1.0', tk.END)
            self.mostrar_titulo.insert(tk.END, tarea.titulo)
            self.mostrar_titulo.config(state='disabled')

            self.mostrar_detalle.config(state='normal')
            self.mostrar_detalle.delete('1.0', tk.END)
            self.mostrar_detalle.insert(tk.END, tarea.detalle)
            self.mostrar_detalle.config(state='disabled')

            self.mostrar_fecha.config(state='normal')
            self.mostrar_fecha.delete('1.0', tk.END)
            self.mostrar_fecha.insert(tk.END, fecha_formateada)
            self.mostrar_fecha.config(state='disabled')

    def _limpiar_detalle(self):
        self.mostrar_titulo.config(state='normal')
        self.mostrar_titulo.delete('1.0', tk.END)
        self.mostrar_titulo.config(state='disabled')

        self.mostrar_detalle.config(state='normal')
        self.mostrar_detalle.delete('1.0', tk.END)
        self.mostrar_detalle.config(state='disabled')

        self.mostrar_fecha.config(state='normal')
        self.mostrar_fecha.delete('1.0', tk.END)
        self.mostrar_fecha.config(state='disabled')
