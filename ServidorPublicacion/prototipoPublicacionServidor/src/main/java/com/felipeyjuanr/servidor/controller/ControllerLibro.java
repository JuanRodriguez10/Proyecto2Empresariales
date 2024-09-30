package com.felipeyjuanr.servidor.controller;

import com.felipeyjuanr.servidor.model.Libro;
import com.felipeyjuanr.servidor.services.ServicioLibro;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(value = "/libros")
public class ControllerLibro {

    private ServicioLibro servicioLibro = ServicioLibro.getServicioLibro();

    @GetMapping
    public ResponseEntity<List<Libro>> getLibros() {
        List<Libro> libros = servicioLibro.getLibros();
        if (libros.isEmpty()) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(libros);
    }

    @GetMapping("/autor/{autor}")
    public ResponseEntity<List<Libro>> getLibrosAutor(@PathVariable String autor) {
        List<Libro> libros = servicioLibro.getLibrosAutor(autor);
        if (libros.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(libros);
    }

    @PostMapping("/agregar")
    public ResponseEntity<String> agregarLibro(@RequestBody Libro libro) {
        boolean agregado = servicioLibro.agregarLibro(
                libro.getCantidadPaginas(),
                libro.getPrecio(),
                libro.getTitulo(),
                libro.getFechaCreacion(),
                libro.getAutor()
        );
        if (agregado) {
            return ResponseEntity.status(HttpStatus.CREATED).body("Libro agregado exitosamente");
        } else {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("No se pudo agregar el libro");
        }
    }

    @GetMapping("/buscarTitulo/{titulo}")
    public ResponseEntity<Libro> buscarLibroPorTitulo(@PathVariable String titulo) {
        Libro libro = servicioLibro.buscarLibroTitulo(titulo);
        if (libro != null) {
            return ResponseEntity.ok(libro);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @GetMapping("/buscarAutor/{autor}")
    public ResponseEntity<Libro> buscarLibroPorAutor(@PathVariable String autor) {
        Libro libro = servicioLibro.buscarLibroAutor(autor);
        if (libro != null) {
            return ResponseEntity.ok(libro);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @GetMapping("/buscar")
    public ResponseEntity<Libro> buscarLibro(
            @RequestParam String titulo,
            @RequestParam String autor) {
        Libro libro = servicioLibro.buscarLibroCompleto(titulo, autor);
        if (libro != null) {
            return ResponseEntity.ok(libro);
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping("/borrar/{titulo}")
    public ResponseEntity<String> eliminarLibro(@PathVariable String titulo) {
        boolean eliminado = servicioLibro.eliminarLibro(titulo);
        if (eliminado) {
            return ResponseEntity.ok("Libro eliminado exitosamente");
        } else {
            return ResponseEntity.notFound().build();
        }
    }

    @PutMapping("/actualizar/{tituloAntiguo}")
    public ResponseEntity<String> actualizarLibro(
            @PathVariable String tituloAntiguo,
            @RequestBody Libro libroActualizado) {
        boolean actualizado = servicioLibro.actualizarLibro(
                tituloAntiguo,
                libroActualizado.getCantidadPaginas(),
                libroActualizado.getPrecio(),
                libroActualizado.getTitulo(),
                libroActualizado.getFechaCreacion(),
                libroActualizado.getAutor()
        );
        if (actualizado) {
            return ResponseEntity.ok("Libro actualizado exitosamente");
        } else {
            return ResponseEntity.notFound().build();
        }
    }
}
