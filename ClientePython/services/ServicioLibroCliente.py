import requests

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