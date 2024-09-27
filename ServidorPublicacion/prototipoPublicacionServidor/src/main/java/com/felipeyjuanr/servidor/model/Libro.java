package com.felipeyjuanr.servidor.model;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.RequiredArgsConstructor;
import java.time.LocalDateTime;


/**
 * @author Juan y Felipe R
 */
@Data
@RequiredArgsConstructor
@AllArgsConstructor
@Builder
public class Libro
{
    //Atributos
    private int cantidadPaginas;
    private double precio;
    private String titulo;
    private LocalDateTime fechaCreacion;
    private String autor;
}

