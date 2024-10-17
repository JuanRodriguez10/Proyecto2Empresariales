from services.ServicioAutor import ServicioAutor
import tkinter as tk
from tkinter import messagebox


class GUIBuscarAutor:
    def __init__(self, root):
        self.servicio_autor = ServicioAutor()
        self.root = root
        self.root.title("Buscar Autor")

        tk.Label(root, text="Nombre a buscar:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_buscado_entry = tk.Entry(root)
        self.nombre_buscado_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(root, text="Buscar", command=self.buscar_autor).grid(row=1, columnspan=2, pady=10)

        tk.Label(root, text="Nombre:").grid(row=2, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Edad:").grid(row=3, column=0, padx=10, pady=5)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Nacionalidad:").grid(row=4, column=0, padx=10, pady=5)
        self.nacionalidad_entry = tk.Entry(root)
        self.nacionalidad_entry.grid(row=4, column=1, padx=10, pady=5)

    def buscar_autor(self):
        nombre = self.nombre_buscado_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
            return
        
        autor = self.servicio_autor.obtener_autor(nombre) 
        if autor:
            self.nombre_entry.insert(0, autor["nombre"])
            self.edad_entry.insert(0, autor["edad"])
            self.nacionalidad_entry.insert(0, autor["nacionalidad"])
        else:
            messagebox.showinfo("No encontrado", "No se encontró ningún autor con ese nombre.")

