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

        libros.add(new Libro(1,1,"a",LocalDateTime.of(2023, 9, 26, 10, 30),"a"));
        libros.add(new Libro(1,1,"b",LocalDateTime.of(2023, 9, 26, 10, 30),"b"));
        libros.add(new Libro(1,1,"c",LocalDateTime.of(2023, 9, 26, 10, 30),"c"));
        libros.add(new Libro(1,1,"d",LocalDateTime.of(2023, 9, 26, 10, 30),"d"));



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

    public boolean agregarLibro(int cantidadPaginas, double precio, String titulo, LocalDateTime fechaCreacion, String autor)
    {
        Libro libro = null;

        libro = new Libro(cantidadPaginas, precio, titulo, fechaCreacion, autor);


        if (verificarExistencia(libro.getTitulo())==null)
        {
            libros.add(libro);
            return true;
        }
        return false;
    }

    public Libro verificarExistencia(String titulo)
    {
        for (Libro librito : libros) {
            if (librito.getTitulo().equalsIgnoreCase(titulo)) {
                return librito;
            }
        }

        return null;
    }

    public Libro buscarLibro(String titulo, String autor) {
        Libro libro = null;

        for (Libro librito : libros) {
            if (librito.getTitulo().equalsIgnoreCase(titulo) && librito.getAutor().equalsIgnoreCase(autor)) {
                return librito;
            }
            else if(librito.getTitulo().equalsIgnoreCase(titulo) || librito.getAutor().equalsIgnoreCase(autor))
            {libro = librito;}
        }

        return libro;
    }

    public boolean eliminarLibro(String titulo) {
        boolean eliminado = false;
        Libro librito = verificarExistencia(titulo);
        eliminado = libros.remove(librito);
        return eliminado;
    }

    public boolean actualizarLibro(String tituloAntiguo, int cantidadPaginas, double precio, String titulo, LocalDateTime fechaCreacion, String autor)
    {
        Libro nuevo = null;


        nuevo = new Libro(cantidadPaginas, precio , titulo, fechaCreacion, autor);


        if (verificarExistencia(tituloAntiguo) != null)
        {
            Libro libroAntiguo = verificarExistencia(tituloAntiguo);
            int index = libros.indexOf(libroAntiguo);
            libros.set(index, nuevo);

            return true;
        }

        return false;
    }



}

