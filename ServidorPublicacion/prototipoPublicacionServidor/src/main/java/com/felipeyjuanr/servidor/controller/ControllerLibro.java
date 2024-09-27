package com.felipeyjuanr.servidor.controller;

import com.felipeyjuanr.servidor.model.Libro;
import com.felipeyjuanr.servidor.services.ServicioLibro;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;

@RestController
@RequestMapping(value = "/libros")
public class ControllerLibro {

    private ServicioLibro servicioLibro = ServicioLibro.getServicioLibro();


    @GetMapping(value = "/")
    public ResponseEntity<ArrayList<Libro>> getLibros(){
        ArrayList<Libro> libros = servicioLibro.getLibros();
        if (libros.isEmpty()) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(libros);
    }




}
