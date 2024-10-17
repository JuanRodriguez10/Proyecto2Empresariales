// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

mod services;

use services::autor_service::{ServicioAutor, Autor};
use tauri::Manager;

#[tauri::command]
async fn obtener_autores(estado: tauri::State<'_, ServicioAutor>) -> Result<Vec<Autor>, String> {
    estado.obtener_autores().await.map_err(|e| e.to_string())
}

#[tauri::command]
async fn obtener_autores_nacionalidad(estado: tauri::State<'_, ServicioAutor>, nacionalidad: String) -> Result<Vec<Autor>, String> {
    estado.obtener_autores_nacionalidad(&nacionalidad).await.map_err(|e| e.to_string())
}

#[tauri::command]
async fn agregar_autor(
    estado: tauri::State<'_, ServicioAutor>,
    nombre: String,
    edad: i32,
    nacionalidad: String,
) -> Result<bool, String> {
    estado.agregar_autor(&nombre, edad, &nacionalidad).await.map_err(|e| e.to_string())
}

#[tauri::command]
async fn buscar_autor(estado: tauri::State<'_, ServicioAutor>, nombre: String) -> Result<Option<Autor>, String> {
    estado.buscar_autor(&nombre).await.map_err(|e| e.to_string())
}

#[tauri::command]
async fn actualizar_autor(
    estado: tauri::State<'_, ServicioAutor>,
    nombre_antiguo: String,
    nombre: String,
    edad: i32,
    nacionalidad: String,
) -> Result<bool, String> {
    estado.actualizar_autor(&nombre_antiguo, &nombre, edad, &nacionalidad)
        .await
        .map_err(|e| e.to_string())
}

#[tauri::command]
async fn eliminar_autor(estado: tauri::State<'_, ServicioAutor>, nombre: String) -> Result<bool, String> {
    estado.eliminar_autor(&nombre).await.map_err(|e| e.to_string())
}

fn main() {
    tauri::Builder::default()
        .setup(|app| {
            let servicio_autor = ServicioAutor::new();
            app.manage(servicio_autor);
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            obtener_autores,
            obtener_autores_nacionalidad,
            agregar_autor,
            buscar_autor,
            actualizar_autor,
            eliminar_autor,
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}