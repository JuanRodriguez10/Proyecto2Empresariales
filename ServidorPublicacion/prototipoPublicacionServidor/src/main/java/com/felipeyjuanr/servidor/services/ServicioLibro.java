package com.felipeyjuanr.servidor.services;

import com.felipeyjuanr.servidor.model.Libro;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.ArrayList;


@Service
public class ServicioLibro {

    private static ServicioLibro servicioLibro;
    private ArrayList<Libro> libros;

    private ServicioLibro(){
        libros = new ArrayList<Libro>();
    }

    public static ServicioLibro getServicioLibro(){
        if(servicioLibro == null){
            servicioLibro = new ServicioLibro();
        }

        return servicioLibro;
    }

    public ArrayList<Libro> getLibros() {
        return libros;
    }

    public ArrayList<Libro> getLibrosAutor(String autor) {
        ArrayList<Libro> autores = new ArrayList<Libro>();
        for(Libro librito : libros){
            if(librito.getAutor().equalsIgnoreCase(autor)){
                autores.add(librito);
            }
        }
        return autores;
    }

    public boolean agregarLibro(int cantidadPaginas, double precio, String titulo, LocalDateTime fechaCreacion, String autor)
    {
        Libro libro = null;

        libro = new Libro(cantidadPaginas, precio, titulo, fechaCreacion, autor);


        if (buscarLibroCompleto(libro.getTitulo(),libro.getAutor())==null)
        {
            libros.add(libro);
            return true;
        }
        return false;
    }

    public Libro buscarLibroCompleto(String titulo, String autor)
    {
        for (Libro librito : libros) {
            if (librito.getTitulo().equalsIgnoreCase(titulo) && librito.getAutor().equalsIgnoreCase(autor)) {
                return librito;
            }
        }

        return null;
    }

    public Libro buscarLibroTitulo(String titulo)
    {
        for (Libro librito : libros) {
            if (librito.getTitulo().equalsIgnoreCase(titulo)) {
                return librito;
            }
        }
        return null;
    }

    public Libro buscarLibroAutor(String autor)
    {
        for (Libro librito : libros) {
            if (librito.getAutor().equalsIgnoreCase(autor)) {
                return librito;
            }
        }
        return null;
    }

    public boolean eliminarLibro(String titulo) {
        boolean eliminado = false;
        Libro librito = buscarLibroTitulo(titulo);
        eliminado = libros.remove(librito);
        return eliminado;
    }

    public boolean actualizarLibro(String tituloAntiguo, int cantidadPaginas, double precio, String titulo, LocalDateTime fechaCreacion, String autor)
    {
        Libro nuevo = null;


        nuevo = new Libro(cantidadPaginas, precio , titulo, fechaCreacion, autor);


        if (buscarLibroTitulo(tituloAntiguo) != null)
        {
            Libro libroAntiguo = buscarLibroTitulo(tituloAntiguo);
            int index = libros.indexOf(libroAntiguo);
            libros.set(index, nuevo);

            return true;
        }

        return false;
    }



}

