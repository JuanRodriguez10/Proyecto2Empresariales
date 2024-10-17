import json
import requests

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