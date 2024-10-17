use serde::{Deserialize, Serialize};
use reqwest::Client;
use chrono::NaiveDateTime;

const BASE_URL: &str = "http://localhost:8080";

#[derive(Debug, Serialize, Deserialize)]
pub struct Libro {
    pub titulo: String,
    pub autores: Vec<String>,
    pub cantidad_paginas: i32,
    pub fecha_creacion: NaiveDateTime,
    pub precio: f64,
    pub tapa_dura: bool,
}

pub struct ServicioLibro {
    client: Client,
}

impl ServicioLibro {
    pub fn new() -> Self {
        ServicioLibro {
            client: Client::new(),
        }
    }

    pub async fn obtener_libros(&self) -> Result<Vec<Libro>, reqwest::Error> {
        let response = self.client.get(format!("{}/libros", BASE_URL)).send().await?;
        response.json().await
    }

    pub async fn obtener_libros_autor(&self, autor: &str) -> Result<Vec<Libro>, reqwest::Error> {
        let response = self.client.get(format!("{}/libros/autor/{}", BASE_URL, autor)).send().await?;
        response.json().await
    }

    pub async fn agregar_libro(&self, libro: &Libro) -> Result<bool, reqwest::Error> {
        let response = self.client
            .post(format!("{}/libros/agregar", BASE_URL))
            .json(libro)
            .send()
            .await?;
        Ok(response.status().is_success())
    }

    pub async fn buscar_libro_por_titulo(&self, titulo: &str) -> Result<Option<Libro>, reqwest::Error> {
        let response = self.client
            .get(format!("{}/libros/buscarTitulo/{}", BASE_URL, titulo))
            .send()
            .await?;
        
        if response.status().is_success() {
            Ok(Some(response.json().await?))
        } else {
            Ok(None)
        }
    }

    // Implementa los demás métodos de manera similar...
}