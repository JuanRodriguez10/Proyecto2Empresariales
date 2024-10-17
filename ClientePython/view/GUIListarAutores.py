from tkinter import ttk
from services.ServicioAutor import ServicioAutor
from tkinter import messagebox
import tkinter as tk

class GUIListarAutores:
    def __init__(self, root):
        self.servicio_autor = ServicioAutor()
        self.root = root
        self.root.title("Listar Autores")

        self.tabla = tk.Listbox(root)
        self.tabla.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

        tk.Button(root, text="Listar Autores", command=self.listar_autores).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(root, text="Filtrar por Nacionalidad", command=self.filtrar_por_nacionalidad).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Nacionalidad:").grid(row=2, column=0, padx=10, pady=5)
        self.nacionalidad_entry = tk.Entry(root)
        self.nacionalidad_entry.grid(row=2, column=1, padx=10, pady=5)

    def listar_autores(self):
        autores = self.servicio_autor.listar_autores()  
        self.mostrar_en_tabla(autores)

    def filtrar_por_nacionalidad(self):
        nacionalidad = self.nacionalidad_entry.get().strip()
        if not nacionalidad:
            messagebox.showwarning("Advertencia", "Por favor ingrese una nacionalidad.")
            return

        autores_filtrados = self.servicio_autor.obtener_autores_por_nacionalidad(nacionalidad)
        if autores_filtrados:
            self.mostrar_en_tabla(autores_filtrados)
        else:
            messagebox.showinfo("No encontrado", "No se encontraron autores con esa nacionalidad.")
            self.tabla.delete(0, tk.END)

    def mostrar_en_tabla(self, autores):
        self.tabla.delete(0, tk.END)  # Limpiar la tabla antes de mostrar nuevos resultados
        for autor in autores:
            autor_info = f"Nombre: {autor['nombre']}, Edad: {autor['edad']}, Nacionalidad: {autor['nacionalidad']}"
            self.tabla.insert(tk.END, autor_info)

