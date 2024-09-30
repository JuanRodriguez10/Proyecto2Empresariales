using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Cliente.Model
{
    public class Libro
    {
        public int CantidadPaginas { get; set; }
        public double Precio { get; set; }
        public string Titulo { get; set; }
        public DateTime FechaCreacion { get; set; }
        public string Autor { get; set; }

        public Libro(int cantidadPaginas, double precio, string titulo, DateTime fechaCreacion, string autor)
        {
            CantidadPaginas = cantidadPaginas;
            Precio = precio;
            Titulo = titulo;
            FechaCreacion = fechaCreacion;
            Autor = autor;
        }

    }
}
