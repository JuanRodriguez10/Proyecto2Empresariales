from services.ServicioLibroCliente import ServicioLibroCliente
import tkinter as tk
from tkinter import messagebox

class GUIListarLibros:
    def __init__(self, root):
        self.servicio_libro = ServicioLibroCliente()  # Instancia del servicio
        self.root = root
        self.root.title("Listar libros")

        # Crear frame para tabla y scrollbars
        frame = tk.Frame(root)
        frame.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

        # Scrollbar vertical
        self.scrollbar_vertical = tk.Scrollbar(frame, orient=tk.VERTICAL)
        self.scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)

        # Scrollbar horizontal
        self.scrollbar_horizontal = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        self.scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

        # Crear tabla (Listbox) más alta y ancha con scrollbars
        self.tabla = tk.Listbox(frame, height=15, width=80, 
                                yscrollcommand=self.scrollbar_vertical.set,
                                xscrollcommand=self.scrollbar_horizontal.set)
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH)

        # Conectar los scrollbars con la tabla
        self.scrollbar_vertical.config(command=self.tabla.yview)
        self.scrollbar_horizontal.config(command=self.tabla.xview)

        # Botones y campos de entrada
        tk.Button(root, text="Listar Libros", command=self.listar_libros).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(root, text="Filtrar por Autor", command=self.filtrar_por_autor).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Autor:").grid(row=2, column=0, padx=10, pady=5)
        self.autor_entry = tk.Entry(root)
        self.autor_entry.grid(row=2, column=1, padx=10, pady=5)

    def listar_libros(self):
        libros = self.servicio_libro.obtener_libros()  
        self.mostrar_en_tabla(libros)

    def filtrar_por_autor(self):
        autor = self.autor_entry.get().strip()
        if not autor:
            messagebox.showwarning("Advertencia", "Por favor ingrese un autor.")
            return

        libros_filtrados = self.servicio_libro.obtener_libros_autor(autor)
        if libros_filtrados:
            self.mostrar_en_tabla(libros_filtrados)
        else:
            messagebox.showinfo("No encontrado", "No se encontraron libros con ese autor.")
            self.tabla.delete(0, tk.END)

    def mostrar_en_tabla(self, libros):
        self.tabla.delete(0, tk.END)  # Limpiar la tabla antes de mostrar nuevos resultados
        for libro in libros:
            # Crear una cadena con todos los datos del libro
            libro_info = (f"Título: {libro['titulo']}, Autor(es): {', '.join(libro['autores'])}, "
                          f"Páginas: {libro['cantidadPaginas']}, Fecha: {libro['fechaCreacion']}, "
                          f"Precio: {libro['precio']}, Tapa Dura: {'Sí' if libro['tapaDura'] else 'No'}")
            self.tabla.insert(tk.END, libro_info)

        # Ajustar automáticamente el scroll horizontal si el contenido es largo
        self.tabla.config(width=max([len(item) for item in self.tabla.get(0, tk.END)]) + 5)

