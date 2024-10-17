use serde::{Deserialize, Serialize};
use reqwest::Client;

const BASE_URL: &str = "http://localhost:8080";
const DOMINIO: &str = "/autores";

#[derive(Debug, Serialize, Deserialize)]
pub struct Autor {
    pub nombre: String,
    pub edad: i32,
    pub nacionalidad: String,
}

pub struct ServicioAutor {
    client: Client,
}

impl ServicioAutor {
    pub fn new() -> Self {
        ServicioAutor {
            client: Client::new(),
        }
    }

    pub async fn obtener_autores(&self) -> Result<Vec<Autor>, reqwest::Error> {
        let response = self.client.get(format!("{}{}", BASE_URL, DOMINIO)).send().await?;
        response.json().await
    }

    pub async fn obtener_autores_nacionalidad(&self, nacionalidad: &str) -> Result<Vec<Autor>, reqwest::Error> {
        let response = self.client
            .get(format!("{}{}/nacionalidad/{}", BASE_URL, DOMINIO, nacionalidad))
            .send()
            .await?;
        response.json().await
    }

    pub async fn agregar_autor(&self, nombre: &str, edad: i32, nacionalidad: &str) -> Result<bool, reqwest::Error> {
        println!("prueba1");
        let response = self.client
            .post(format!("{}{}/agregar", BASE_URL, DOMINIO))
            .json(&serde_json::json!({
                "nombre": nombre,
                "edad": edad,
                "nacionalidad": nacionalidad
            }))
            .send()
            .await?;
        Ok(response.status().is_success())
    }

    pub async fn buscar_autor(&self, nombre: &str) -> Result<Option<Autor>, reqwest::Error> {
        let response = self.client
            .get(format!("{}{}/{}", BASE_URL, DOMINIO, nombre))
            .send()
            .await?;
        
        if response.status().is_success() {
            Ok(Some(response.json().await?))
        } else {
            Ok(None)
        }
    }

    pub async fn actualizar_autor(&self, nombre_antiguo: &str, nombre: &str, edad: i32, nacionalidad: &str) -> Result<bool, reqwest::Error> {
        let response = self.client
            .put(format!("{}/autores/actualizar/{}", BASE_URL, nombre_antiguo))
            .json(&serde_json::json!({
                "nombre": nombre,
                "edad": edad,
                "nacionalidad": nacionalidad
            }))
            .send()
            .await?;
        Ok(response.status().is_success())
    }

    pub async fn eliminar_autor(&self, nombre: &str) -> Result<bool, reqwest::Error> {
        let response = self.client
            .delete(format!("{}{}/borrar/{}", BASE_URL, DOMINIO, nombre))
            .send()
            .await?;
        Ok(response.status().is_success())
    }
}