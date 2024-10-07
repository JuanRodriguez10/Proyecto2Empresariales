using Cliente.Model;
using Cliente.Service;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Cliente
{
    public partial class GUIBuscar : Form
    {
        private ServicioLibroCliente servicioLibro;

        public GUIBuscar()
        {
            InitializeComponent();
            this.ActiveControl = txtTituloBuscar;
            servicioLibro = new ServicioLibroCliente();

        }

        private void lblCantidadPaginas_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btnBuscar_Click(object sender, EventArgs e)
        {
            string tituloBuscar = txtTituloBuscar.Text.Trim();
            string autorBuscar = txtAutorBuscado.Text.Trim();
            Libro libroEncontrado = null;

            try
            {
                if (!string.IsNullOrEmpty(tituloBuscar) && !string.IsNullOrEmpty(autorBuscar))
                {
                    libroEncontrado = servicioLibro.BuscarLibroCompleto(tituloBuscar, autorBuscar);
                }
                else if (!string.IsNullOrEmpty(tituloBuscar))
                {
                    libroEncontrado = servicioLibro.BuscarLibroPorTitulo(tituloBuscar);
                }
                else if (!string.IsNullOrEmpty(autorBuscar))
                {
                    libroEncontrado = servicioLibro.BuscarLibroPorAutor(autorBuscar);
                }
                else
                {
                    MessageBox.Show("Por favor, ingrese un título o un autor para buscar.", "Advertencia", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                if (libroEncontrado != null)
                {
                    txtTitulo.Text = libroEncontrado.Titulo;
                    txtAutores.Text = libroEncontrado.Autor;
                    txtPaginas.Text = libroEncontrado.CantidadPaginas.ToString();
                    dpFecha.Value = libroEncontrado.FechaCreacion;
                    txtPrecio.Text = libroEncontrado.Precio.ToString();

                    MessageBox.Show("Libro encontrado.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    txtTitulo.Text = "";
                    txtAutores.Text = "";
                    txtPaginas.Text = "";
                    dpFecha.Value = DateTime.Now;
                    txtPrecio.Text = "";
                    MessageBox.Show("No se encontró ningún libro con los criterios especificados.", "No encontrado", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ocurrió un error al buscar el libro: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

    }
}
