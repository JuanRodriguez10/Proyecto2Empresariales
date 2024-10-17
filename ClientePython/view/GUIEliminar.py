from services.ServicioLibroCliente import ServicioLibroCliente
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry

class GUIEliminar(Tk):
    def __init__(self):
        super().__init__()
        self.servicio_libro = ServicioLibroCliente()
        self.title("Buscar Libro")

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

        Label(self, text="Páginas:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txt_paginas = Entry(self)
        self.txt_paginas.grid(row=4, column=1, padx=5, pady=5)

        Label(self, text="Fecha:").grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.dp_fecha = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.dp_fecha.grid(row=5, column=1, padx=5, pady=5)

        Label(self, text="Precio:").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        self.txt_precio = Entry(self)
        self.txt_precio.grid(row=6, column=1, padx=5, pady=5)

        # Checkbox para tapa dura
        self.chx_tapa_dura = BooleanVar()
        Checkbutton(self, text="Tapa Dura", variable=self.chx_tapa_dura).grid(row=7, columnspan=2, pady=5)

        # Botón para eliminar el libro
        Button(self, text="Eliminar", command=self.confirmar_eliminar_libro).grid(row=8, columnspan=2, pady=10)

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
                self.txt_autores.insert(0, ', '.join(libro_encontrado["autores"]))

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

    def confirmar_eliminar_libro(self):
        titulo = self.txt_titulo.get().strip()

        if not titulo:
            messagebox.showwarning("Advertencia", "No hay un libro seleccionado para eliminar.")
            return

        respuesta = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro de que desea eliminar el libro '{titulo}'?")
        
        if respuesta:
            self.eliminar_libro(titulo)

    def eliminar_libro(self, titulo):
        try:
            eliminado = self.servicio_libro.eliminar_libro(titulo)
            if eliminado:
                messagebox.showinfo("Éxito", f"El libro '{titulo}' ha sido eliminado correctamente.")
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", f"No se pudo eliminar el libro '{titulo}'.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar el libro: {str(e)}")

    def limpiar_campos(self):
        self.txt_titulo.delete(0, END)
        self.txt_autores.delete(0, END)
        self.txt_paginas.delete(0, END)
        self.dp_fecha.set_date(datetime.now())
        self.txt_precio.delete(0, END)
        self.chx_tapa_dura.set(False)

