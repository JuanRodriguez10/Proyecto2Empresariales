from tkinter import *
from tkinter import messagebox
from datetime import datetime
from services.ServicioLibroCliente import ServicioLibroCliente
from tkcalendar import DateEntry

class GUIBuscar(Tk):
    def __init__(self):
        super().__init__()
        self.servicio_libro = ServicioLibroCliente()
        self.title("Buscar Libro")

        # Campo de búsqueda por título
        Label(self, text="Buscar por Título:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txt_titulo_buscar = Entry(self)
        self.txt_titulo_buscar.grid(row=0, column=1, padx=5, pady=5)

        # Campo de búsqueda por autor
        Label(self, text="Buscar por Autor:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txt_autor_buscado = Entry(self)
        self.txt_autor_buscado.grid(row=1, column=1, padx=5, pady=5)

        # Botón de búsqueda
        Button(self, text="Buscar", command=self.buscar_libro).grid(row=2, columnspan=2, pady=10)

        # Campos para mostrar los detalles del libro encontrado
        Label(self, text="Título:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.txt_titulo = Entry(self)
        self.txt_titulo.grid(row=3, column=1, padx=5, pady=5)

        Label(self, text="Autores:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txt_autores = Entry(self)
        self.txt_autores.grid(row=4, column=1, padx=5, pady=5)

        Label(self, text="Páginas:").grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txt_paginas = Entry(self)
        self.txt_paginas.grid(row=5, column=1, padx=5, pady=5)

        Label(self, text="Fecha:").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        self.dp_fecha = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.dp_fecha.grid(row=6, column=1, padx=5, pady=5)

        Label(self, text="Precio:").grid(row=7, column=0, sticky=W, padx=5, pady=5)
        self.txt_precio = Entry(self)
        self.txt_precio.grid(row=7, column=1, padx=5, pady=5)

        # Checkbox para tapa dura
        self.chx_tapa_dura = BooleanVar()
        Checkbutton(self, text="Tapa Dura", variable=self.chx_tapa_dura).grid(row=8, columnspan=2, pady=5)

    def buscar_libro(self):
        titulo_buscar = self.txt_titulo_buscar.get().strip()
        autor_buscado = self.txt_autor_buscado.get().strip()
        libro_encontrado = None

        try:
            # Determinar el método de búsqueda
            if titulo_buscar and autor_buscado:
                libro_encontrado = self.servicio_libro.buscar_libro_completo(titulo_buscar, autor_buscado)
            elif titulo_buscar:
                libro_encontrado = self.servicio_libro.buscar_libro_por_titulo(titulo_buscar)
            elif autor_buscado:
                libro_encontrado = self.servicio_libro.buscar_libro_por_autor(autor_buscado)
            else:
                messagebox.showwarning("Advertencia", "Por favor, ingrese un título o un autor para buscar.")
                return

            # Mostrar los datos si se encuentra un libro
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
                messagebox.showinfo("No encontrado", "No se encontró ningún libro con los criterios especificados.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar el libro: {str(e)}")

    def limpiar_campos(self):
        self.txt_titulo.delete(0, END)
        self.txt_autores.delete(0, END)
        self.txt_paginas.delete(0, END)
        self.dp_fecha.set_date(datetime.now())
        self.txt_precio.delete(0, END)
        self.chx_tapa_dura.set(False)

