import tkinter as tk
from view.GUIAgregar import GUIAgregar
from view.GUIBuscar import GUIBuscar
from view.GUIActualizar import GUIActualizar
from view.GUIEliminar import GUIEliminar
from view.GUIListarLibros import GUIListarLibros
from view.GUIAgregarAutor import GUIAgregarAutor
from view.GUIActualizarAutor import GUIActualizarAutor
from view.GUIBuscarAutor import GUIBuscarAutor
from view.GUIEliminarAutor import GUIEliminarAutor
from view.GUIListarAutores import GUIListarAutores

class GUIPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Autores y Libros")
        
        # Crear la barra de menú
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # Menú de Autor
        autor_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Autor", menu=autor_menu)
        autor_menu.add_command(label="Agregar Autor", command=self.abrir_agregar_autor)
        autor_menu.add_command(label="Actualizar Autor", command=self.abrir_actualizar_autor)
        autor_menu.add_command(label="Buscar Autor", command=self.abrir_buscar_autor)
        autor_menu.add_command(label="Eliminar Autor", command=self.abrir_eliminar_autor)
        autor_menu.add_command(label="Listar Autores", command=self.abrir_listar_autores)
        
        # Menú de Libro
        libro_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Libro", menu=libro_menu)
        libro_menu.add_command(label="Agregar Libro", command=self.abrir_agregar_libro)
        libro_menu.add_command(label="Actualizar Libro", command=self.abrir_actualizar_libro)
        libro_menu.add_command(label="Buscar Libro", command=self.abrir_buscar_libro)
        libro_menu.add_command(label="Eliminar Libro", command=self.abrir_eliminar_libro)
        libro_menu.add_command(label="Listar Libros", command=self.abrir_listar_libros)

    def abrir_agregar_libro(self):
        GUIAgregar()
    
    def abrir_buscar_libro(self):
        GUIBuscar()

    def abrir_actualizar_libro(self):
        GUIActualizar()

    def abrir_eliminar_libro(self):
        GUIEliminar()

    def abrir_listar_libros(self):
        nueva_ventana = tk.Toplevel(self.root)
        GUIListarLibros(nueva_ventana)

    def abrir_agregar_autor(self):
        nueva_ventana = tk.Toplevel(self.root)
        GUIAgregarAutor(nueva_ventana)

    def abrir_actualizar_autor(self):
        nueva_ventana = tk.Toplevel(self.root)
        GUIActualizarAutor(nueva_ventana)

    def abrir_buscar_autor(self):
        nueva_ventana = tk.Toplevel(self.root)
        GUIBuscarAutor(nueva_ventana)

    def abrir_eliminar_autor(self):
        nueva_ventana = tk.Toplevel(self.root)
        GUIEliminarAutor(nueva_ventana)

    def abrir_listar_autores(self):
        nueva_ventana = tk.Toplevel(self.root)
        GUIListarAutores(nueva_ventana)

