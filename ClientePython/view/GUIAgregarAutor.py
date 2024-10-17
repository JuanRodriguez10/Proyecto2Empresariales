import tkinter as tk
from tkinter import messagebox
from services.ServicioAutor import ServicioAutor

class GUIAgregarAutor:
    def __init__(self, root):
        self.servicio_autor = ServicioAutor()
        self.root = root
        self.root.title("Agregar Autor")

        # Campos de entrada
        tk.Label(root, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Edad:").grid(row=1, column=0, padx=10, pady=5)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Nacionalidad:").grid(row=2, column=0, padx=10, pady=5)
        self.nacionalidad_entry = tk.Entry(root)
        self.nacionalidad_entry.grid(row=2, column=1, padx=10, pady=5)

        # Botón para agregar autor
        tk.Button(root, text="Agregar Autor", command=self.agregar_autor).grid(row=3, columnspan=2, pady=10)

    def agregar_autor(self):
        nombre = self.nombre_entry.get().strip()
        try:
            edad = int(self.edad_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error de entrada", "La edad debe ser un valor numérico entero.")
            return

        nacionalidad = self.nacionalidad_entry.get().strip()

        # Aquí usamos el booleano que retorna `agregar_autor`
        if self.servicio_autor.agregar_autor(nombre, edad, nacionalidad):
            self.limpiar_campos()
            messagebox.showinfo("Confirmación", "El autor fue agregado exitosamente.")
        else:
            messagebox.showerror("Error", "Hubo un error al agregar el autor.")


    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.nacionalidad_entry.delete(0, tk.END)

