import tkinter as tk
from tkinter import messagebox
from services.ServicioAutor import ServicioAutor

class GUIEliminarAutor:
    def __init__(self, root):
        self.servicio_autor = ServicioAutor()
        self.autor = None
        self.root = root
        self.root.title("Eliminar Autor")

        # Campos de búsqueda
        tk.Label(root, text="Nombre a buscar:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_buscado_entry = tk.Entry(root)
        self.nombre_buscado_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(root, text="Buscar", command=self.buscar_autor).grid(row=1, columnspan=2, pady=10)

        # Campos para mostrar los datos del autor
        tk.Label(root, text="Nombre:").grid(row=2, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Edad:").grid(row=3, column=0, padx=10, pady=5)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Nacionalidad:").grid(row=4, column=0, padx=10, pady=5)
        self.nacionalidad_entry = tk.Entry(root)
        self.nacionalidad_entry.grid(row=4, column=1, padx=10, pady=5)

        # Botón para eliminar autor
        tk.Button(root, text="Eliminar", command=self.eliminar_autor).grid(row=5, columnspan=2, pady=10)

    def buscar_autor(self):
        nombre = self.nombre_buscado_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
            return
        
        self.autor = self.servicio_autor.obtener_autor(nombre)
        if self.autor:
            # Mostrar los datos del autor en las casillas
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, self.autor["nombre"])
            self.edad_entry.delete(0, tk.END)
            self.edad_entry.insert(0, self.autor["edad"])
            self.nacionalidad_entry.delete(0, tk.END)
            self.nacionalidad_entry.insert(0, self.autor["nacionalidad"])
            messagebox.showinfo("Éxito", "Autor encontrado. Presione 'Eliminar' para borrarlo.")
        else:
            self.limpiar_campos()
            messagebox.showinfo("No encontrado", "No se encontró ningún autor con ese nombre.")

    def eliminar_autor(self):
        if self.autor:
            if messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar este autor?"):
                if self.servicio_autor.eliminar_autor(self.nombre_buscado_entry.get().strip()):  # Usamos el id del autor para eliminar
                    messagebox.showinfo("Éxito", "El autor ha sido eliminado.")
                    self.limpiar_campos()
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el autor.")
        else:
            messagebox.showwarning("Advertencia", "Primero busque un autor.")

    def limpiar_campos(self):
        self.nombre_buscado_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.nacionalidad_entry.delete(0, tk.END)


