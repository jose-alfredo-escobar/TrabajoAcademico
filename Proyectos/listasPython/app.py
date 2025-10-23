import tkinter as tk
from modelo import ListaTareas
from vista import VistaTareas
from controlador import ControladorTareas


def main():
    root = tk.Tk()
    modelo = ListaTareas()
    vista = VistaTareas(root, modelo)
    controlador = ControladorTareas(modelo, vista)
    vista.controlador = controlador
    vista.configurar_botones()
    root.mainloop()


if __name__ == "__main__":
    main()
