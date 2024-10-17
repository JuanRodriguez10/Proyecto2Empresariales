import tkinter as tk
from services.ServicioAutor import ServicioAutor
from services.ServicioLibroCliente import ServicioLibroCliente
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import ttk

class GUIActualizar(Tk):
    def __init__(self):
        super().__init__()
        self.servicio_libro = ServicioLibroCliente()
        self.servicio_autor = ServicioAutor()
        self.title("Buscar Libro")
        self.autores_lista = []  # Para manejar la lista de autores seleccionados
        
        # Campo de búsqueda por título
        Label(self, text="Buscar por Título:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txt_titulo_buscar = Entry(self)
        self.txt_titulo_buscar.grid(row=0, column=1, padx=5, pady=5)

        # Botón de búsqueda
        Button(self, text="Buscar", command=self.buscar_libro).grid(row=1, columnspan=2, pady=10)

        # Campos para mostrar los detalles del libro encontrado
        Label(self, text="Título:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txt_titulo = Entry(self)
        self.txt_titulo.grid(row=2, column=1, padx=5, pady=5)

        Label(self, text="Autores:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txt_autores = Entry(self)
        self.txt_autores.grid(row=3, column=1, padx=5, pady=5)

        # ComboBox para manejar autores
        Label(self, text="Seleccionar Autor:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.combobox_autores = ttk.Combobox(self, values=self.obtener_autores())
        self.combobox_autores.grid(row=4, column=1, padx=5, pady=5)

        # Botones para agregar y eliminar autores
        Button(self, text="Agregar Autor", command=self.agregar_autor).grid(row=5, column=0, padx=5, pady=5)
        Button(self, text="Eliminar Autor", command=self.eliminar_autor).grid(row=5, column=1, padx=5, pady=5)

        Label(self, text="Páginas:").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        self.txt_paginas = Entry(self)
        self.txt_paginas.grid(row=6, column=1, padx=5, pady=5)

        Label(self, text="Fecha:").grid(row=7, column=0, sticky=W, padx=5, pady=5)
        self.dp_fecha = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.dp_fecha.grid(row=7, column=1, padx=5, pady=5)

        Label(self, text="Precio:").grid(row=8, column=0, sticky=W, padx=5, pady=5)
        self.txt_precio = Entry(self)
        self.txt_precio.grid(row=8, column=1, padx=5, pady=5)

        # Checkbox para tapa dura
        self.chx_tapa_dura = BooleanVar()
        Checkbutton(self, text="Tapa Dura", variable=self.chx_tapa_dura).grid(row=9, columnspan=2, pady=5)

        # Botón para actualizar
        Button(self, text="Actualizar", command=self.actualizar_libro).grid(row=10, columnspan=2, pady=10)

    def buscar_libro(self):
        titulo_buscar = self.txt_titulo_buscar.get().strip()
        if not titulo_buscar:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un título para buscar.")
            return

        try:
            libro_encontrado = self.servicio_libro.buscar_libro_por_titulo(titulo_buscar)

            if libro_encontrado:
                self.txt_titulo.delete(0, END)
                self.txt_titulo.insert(0, libro_encontrado["titulo"])

                self.txt_autores.delete(0, END)
                self.autores_lista = libro_encontrado["autores"]
                self.txt_autores.insert(0, ', '.join(self.autores_lista))

                self.txt_paginas.delete(0, END)
                self.txt_paginas.insert(0, libro_encontrado["cantidadPaginas"])

                self.dp_fecha.set_date(datetime.fromisoformat(libro_encontrado["fechaCreacion"]))

                self.txt_precio.delete(0, END)
                self.txt_precio.insert(0, libro_encontrado["precio"])

                self.chx_tapa_dura.set(libro_encontrado["tapaDura"])

                messagebox.showinfo("Éxito", "Libro encontrado.")
            else:
                self.limpiar_campos()
                messagebox.showinfo("No encontrado", "No se encontró ningún libro con el título especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar el libro: {str(e)}")

    def obtener_autores(self):
        nombres_autores = [autor["nombre"] for autor in self.servicio_autor.listar_autores()]
        
        return nombres_autores

    def agregar_autor(self):
        autor_seleccionado = self.combobox_autores.get()
        if autor_seleccionado and autor_seleccionado not in self.autores_lista:
            self.autores_lista.append(autor_seleccionado)
            self.txt_autores.delete(0, END)
            self.txt_autores.insert(0, ', '.join(self.autores_lista))

    def eliminar_autor(self):
        autor_seleccionado = self.combobox_autores.get()
        if autor_seleccionado in self.autores_lista:
            self.autores_lista.remove(autor_seleccionado)
            self.txt_autores.delete(0, END)
            self.txt_autores.insert(0, ', '.join(self.autores_lista))

    def actualizar_libro(self):
        titulo_antiguo = self.txt_titulo_buscar.get().strip()
        paginas = self.txt_paginas.get().strip()
        precio = self.txt_precio.get().strip()
        nuevo_titulo = self.txt_titulo.get().strip()
        fecha = self.dp_fecha.get_date()
        autores = ','.join(self.autores_lista)
        tapa_dura = self.chx_tapa_dura.get()

        try:
            if self.servicio_libro.actualizar_libro(titulo_antiguo, paginas, precio, nuevo_titulo, fecha, autores, tapa_dura):
                messagebox.showinfo("Éxito", "Libro actualizado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el libro.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al actualizar el libro: {str(e)}")

    def limpiar_campos(self):
        self.txt_titulo.delete(0, END)
        self.txt_autores.delete(0, END)
        self.autores_lista = []
        self.txt_paginas.delete(0, END)
        self.dp_fecha.set_date(datetime.now())
        self.txt_precio.delete(0, END)
        self.chx_tapa_dura.set(False)

