from services.ServicioAutor import ServicioAutor
import tkinter as tk
from tkinter import messagebox

class GUIActualizarAutor:
    def __init__(self, root):
        self.servicio_autor = ServicioAutor()
        self.autor_encontrado = None
        self.nombre_original = None
        self.root = root
        self.root.title("Actualizar Autor")

        tk.Label(root, text="Nombre a buscar:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_buscado_entry = tk.Entry(root)
        self.nombre_buscado_entry.grid(row=0, column=1, padx=10, pady=5)
        tk.Button(root, text="Buscar", command=self.buscar_autor).grid(row=0, column=2, padx=10, pady=5)

        tk.Label(root, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Edad:").grid(row=2, column=0, padx=10, pady=5)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Nacionalidad:").grid(row=3, column=0, padx=10, pady=5)
        self.nacionalidad_entry = tk.Entry(root)
        self.nacionalidad_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(root, text="Actualizar", command=self.actualizar_autor).grid(row=4, columnspan=2, pady=10)

    def buscar_autor(self):
        nombre = self.nombre_buscado_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
            return
        
        self.autor_encontrado = self.servicio_autor.obtener_autor(nombre) 
        if self.autor_encontrado:
            self.nombre_original = nombre
            self.nombre_entry.insert(0, self.autor_encontrado["nombre"])
            self.edad_entry.insert(0, self.autor_encontrado["edad"])
            self.nacionalidad_entry.insert(0, self.autor_encontrado["nacionalidad"])
            messagebox.showinfo("Éxito", "Autor encontrado. Modifique los campos y presione 'Actualizar'.")
        else:
            self.limpiar_campos()
            messagebox.showinfo("No encontrado", "No se encontró ningún autor con ese nombre.")

    def actualizar_autor(self):
        if not self.autor_encontrado:
            messagebox.showwarning("Advertencia", "Por favor, primero busque un autor.")
            return

        try:
            nombre = self.nombre_entry.get().strip()
            edad = int(self.edad_entry.get().strip())
            nacionalidad = self.nacionalidad_entry.get().strip()

            if self.servicio_autor.actualizar_autor(self.nombre_original, nombre, edad, nacionalidad):
                messagebox.showinfo("Éxito", "El autor ha sido actualizado exitosamente.")
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el autor.")
        except ValueError:
            messagebox.showerror("Error", "Edad debe ser un valor numérico.")

    def limpiar_campos(self):
        self.nombre_buscado_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.nacionalidad_entry.delete(0, tk.END)

