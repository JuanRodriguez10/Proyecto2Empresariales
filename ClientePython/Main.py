import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
import json
from datetime import datetime
from tkcalendar import DateEntry

BASE_URL = "http://localhost:8080"
DOMINIO = "/autores"

class ServicioAutor:
    def __init__(self):
        self.base_url = BASE_URL
        self.dominio = DOMINIO

    def agregar_autor(self, nombre, edad, nacionalidad):
        data = {
            "nombre": nombre,
            "edad": edad,
            "nacionalidad": nacionalidad
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{self.base_url}{self.dominio}/agregar", data=json.dumps(data), headers=headers)
        
        if response.status_code in (200, 201):
            return True
        else:
            print(f"Error al agregar autor: {response.status_code} - {response.text}")
            return False

    def listar_autores(self):
        response = requests.get(f"{self.base_url}{self.dominio}")
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al listar autores: {response.status_code} - {response.text}")
            return None

    def obtener_autores_por_nacionalidad(self, nacionalidad):
        response = requests.get(f"{self.base_url}{self.dominio}/nacionalidad/{nacionalidad}")
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener autores por nacionalidad: {response.status_code} - {response.text}")
            return None

    
    def obtener_autor(self, nombre_autor):
        response = requests.get(f"{self.base_url}{self.dominio}/{nombre_autor}")
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener autor: {response.status_code} - {response.text}")
            return None


    def actualizar_autor(self, id_autor, nombre=None, edad=None, nacionalidad=None):
        data = {}
        if nombre:
            data["nombre"] = nombre
        if edad:
            data["edad"] = edad
        if nacionalidad:
            data["nacionalidad"] = nacionalidad

        headers = {"Content-Type": "application/json"}
        response = requests.put(f"{self.base_url}{self.dominio}/actualizar/{id_autor}", data=json.dumps(data), headers=headers)
        
        if response.status_code == 200:
            return True
        else:
            print(f"Error al actualizar autor: {response.status_code} - {response.text}")
            return False

    def eliminar_autor(self, id_autor):
        response = requests.delete(f"{self.base_url}{self.dominio}/borrar/{id_autor}")
        
        if response.status_code == 200:
            return True
        else:
            print(f"Error al eliminar autor: {response.status_code} - {response.text}")
            return False


class ServicioLibroCliente:
    BASE_URL = "http://localhost:8080"

    def obtener_libros(self):
        response = requests.get(f"{self.BASE_URL}/libros")
       
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al listar libros: {response.status_code} - {response.text}")
            return None

    def obtener_libros_autor(self, autor):
        response = requests.get(f"{self.BASE_URL}/libros/autor/{autor}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al listar libros por autor: {response.status_code} - {response.text}")
            return None

        

    def agregar_libro(self, titulo, autores, paginas, fecha, precio, tapa_dura):
        fecha_iso = fecha.strftime("%Y-%m-%dT%H:%M:%S")
        body = {
            "titulo": titulo,
            "autores": autores.split(','),
            "cantidadPaginas": paginas,
            "fechaCreacion": fecha_iso,
            "precio": precio,
            "tapaDura": tapa_dura
        }
        response = requests.post(f"{self.BASE_URL}/libros/agregar", json=body)
        if response.status_code in (200, 201):
            return True
        else:
            print(f"Error al agregar libro: {response.status_code} - {response.text}")
            return False


    def buscar_libro_por_titulo(self, titulo):
        response = requests.get(f"{self.BASE_URL}/libros/buscarTitulo/{titulo}")
        if response.status_code == 200:
            return json.loads(response.content)
        return None

    def buscar_libro_por_autor(self, autor):
        response = requests.get(f"{self.BASE_URL}/libros/buscarAutor/{autor}")
        if response.status_code == 200:
            return json.loads(response.content)
        return None

    def buscar_libro_completo(self, titulo, autor):
        params = {"titulo": titulo, "autor": autor}
        response = requests.get(f"{self.BASE_URL}/libros/buscar", params=params)
        if response.status_code == 200:
            return json.loads(response.content)
        return None

    def dar_autores_disponibles(self):
        response = requests.get(f"{self.BASE_URL}/libros/autoresDisponibles")
        if response.status_code == 200:
            return json.loads(response.content)
        return []

    def eliminar_libro(self, titulo):
        response = requests.delete(f"{self.BASE_URL}/libros/borrar/{titulo}")
        return response.status_code == 200

    def actualizar_libro(self, titulo_antiguo, paginas, precio, nuevo_titulo, fecha, autores, tapa_dura):
        fecha_iso = fecha.strftime("%Y-%m-%dT%H:%M:%S")
        body = {
            "cantidadPaginas": paginas,
            "precio": precio,
            "titulo": nuevo_titulo,
            "fechaCreacion": fecha_iso,
            "autores": autores.split(','),
            "tapaDura": tapa_dura
        }
        response = requests.put(f"{self.BASE_URL}/libros/actualizar/{titulo_antiguo}", json=body)
        return response.status_code == 200

   

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

class GUIBuscarAutor:
    def __init__(self, root):
        self.servicio_autor = ServicioAutor()
        self.root = root
        self.root.title("Buscar Autor")

        tk.Label(root, text="Nombre a buscar:").grid(row=0, column=0, padx=10, pady=5)
        self.nombre_buscado_entry = tk.Entry(root)
        self.nombre_buscado_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Button(root, text="Buscar", command=self.buscar_autor).grid(row=1, columnspan=2, pady=10)

        tk.Label(root, text="Nombre:").grid(row=2, column=0, padx=10, pady=5)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Edad:").grid(row=3, column=0, padx=10, pady=5)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Nacionalidad:").grid(row=4, column=0, padx=10, pady=5)
        self.nacionalidad_entry = tk.Entry(root)
        self.nacionalidad_entry.grid(row=4, column=1, padx=10, pady=5)

    def buscar_autor(self):
        nombre = self.nombre_buscado_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Advertencia", "Por favor ingrese un nombre.")
            return
        
        autor = self.servicio_autor.obtener_autor(nombre) 
        if autor:
            self.nombre_entry.insert(0, autor["nombre"])
            self.edad_entry.insert(0, autor["edad"])
            self.nacionalidad_entry.insert(0, autor["nacionalidad"])
        else:
            messagebox.showinfo("No encontrado", "No se encontró ningún autor con ese nombre.")


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


class GUIPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Autores y Libros")
        
        # Crear la barra de menú
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        # Menú de Autor
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Salir", command=self.salir_aplicacion)

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

        #Menú Acerca de
        acercade_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Acerca de", menu=acercade_menu)
        acercade_menu.add_command(label="Desarrolladores", command=self.mostrar_informacion_desarrolladores)

    def salir_aplicacion(self):
        self.root.quit()
        self.root.destroy() 

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
    
    def mostrar_informacion_desarrolladores(self):
        desarrollo = ("Desarrollado por:\n\n"
                  "Juan Felipe Rodriguez Barbosa\n"
                  "Cod.2220221045\n"
                  "Juan Esteban Rodriguez Castellanos\n"
                  "Cod.2220221063\n\n"
                  "Desarrollo de Aplicaciones Empresariales\n"
                  "Version 1.0")
        messagebox.showinfo("Información", desarrollo)


def main():
    root = tk.Tk()
    app = GUIPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()