from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from services.ServicioLibroCliente import ServicioLibroCliente

class GUIAgregar(Tk):
    def __init__(self):
        super().__init__()
        self.servicio_libro = ServicioLibroCliente()
        self.autores = []
        self.title("Agregar Libro")

        # Título
        Label(self, text="Título:").grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txt_titulo = Entry(self)
        self.txt_titulo.grid(row=0, column=1, padx=5, pady=5)

        # Número de páginas
        Label(self, text="Páginas:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txt_paginas = Entry(self)
        self.txt_paginas.grid(row=1, column=1, padx=5, pady=5)

        # Precio
        Label(self, text="Precio:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txt_precio = Entry(self)
        self.txt_precio.grid(row=2, column=1, padx=5, pady=5)

        # Fecha de publicación (Date Picker)
        Label(self, text="Fecha:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.dp_fecha = DateEntry(self, date_pattern='yyyy-mm-dd')
        self.dp_fecha.grid(row=3, column=1, padx=5, pady=5)

        # Checkbox para tapa dura
        self.chx_tapa_dura = BooleanVar()
        Checkbutton(self, text="Tapa Dura", variable=self.chx_tapa_dura).grid(row=4, columnspan=2, pady=5)

        # Autores
        Label(self, text="Autores disponibles:").grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.cbx_autores = Listbox(self, selectmode=SINGLE, height=5)
        self.cbx_autores.grid(row=5, column=1, padx=5, pady=5)
        for autor in self.servicio_libro.dar_autores_disponibles():
            self.cbx_autores.insert(END, autor)

        # Lista de autores seleccionados
        Label(self, text="Autores seleccionados:").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        self.txt_autores = Entry(self)
        self.txt_autores.grid(row=6, column=1, padx=5, pady=5)

        # Botón para agregar autor
        Button(self, text="Agregar Autor", command=self.agregar_autor).grid(row=7, columnspan=2, pady=5)

        # Botón para agregar libro
        Button(self, text="Agregar Libro", command=self.agregar_libro).grid(row=8, columnspan=2, pady=10)

    def agregar_autor(self):
        try:
            autor_seleccionado = self.cbx_autores.get(self.cbx_autores.curselection())
            if autor_seleccionado not in self.autores:
                self.autores.append(autor_seleccionado)
                self.txt_autores.delete(0, END)
                self.txt_autores.insert(0, ','.join(self.autores))
            else:
                messagebox.showerror("Error", "No se pueden repetir autores.")
        except IndexError:
            messagebox.showerror("Error", "Debe seleccionar un autor.")

    def agregar_libro(self):
        try:
            titulo = self.txt_titulo.get().strip()
            if not titulo:
                raise ValueError("El título no puede estar vacío.")

            paginas = int(self.txt_paginas.get().strip())
            precio = float(self.txt_precio.get().strip())
            fecha = self.dp_fecha.get_date()  # Obtiene la fecha seleccionada del DatePicker
            tapa_dura = self.chx_tapa_dura.get()

            if self.servicio_libro.agregar_libro(titulo, ','.join(self.autores), paginas, fecha, precio, tapa_dura):
                self.limpiar_campos()
                messagebox.showinfo("Confirmación", "El libro fue agregado exitosamente.")
            else:
                messagebox.showerror("Error", "Hubo un error al agregar el libro.")
        except ValueError as e:
            messagebox.showerror("Error de entrada", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Se produjo un error inesperado: {str(e)}")

    def limpiar_campos(self):
        self.txt_titulo.delete(0, END)
        self.txt_paginas.delete(0, END)
        self.txt_precio.delete(0, END)
        self.dp_fecha.set_date(self.dp_fecha._date.today())  # Reinicia la fecha a hoy
        self.txt_autores.delete(0, END)
        self.chx_tapa_dura.set(False)
        self.autores = []

