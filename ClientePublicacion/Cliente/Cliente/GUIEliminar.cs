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
    public partial class GUIEliminar : Form
    {
        private ServicioLibroCliente servicioLibro;
        Libro libroEncontrado;
        public GUIEliminar()
        {

            InitializeComponent();
            this.ActiveControl = txtBuscar;
            servicioLibro = new ServicioLibroCliente();
            libroEncontrado = null;
        }

        private void lblCantidadPaginas_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void btnBuscar_Click(object sender, EventArgs e)
        {
            string tituloBuscar = txtBuscar.Text.Trim();
            if (!string.IsNullOrEmpty(tituloBuscar))
            {
                libroEncontrado = servicioLibro.BuscarLibroPorTitulo(tituloBuscar);
            }
            else
            {
                MessageBox.Show("Por favor, ingrese un título para buscar.", "Advertencia", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            if (libroEncontrado != null)
            {
                txtTitulo.Text = libroEncontrado.Titulo;
                txtAutor.Text = libroEncontrado.Autor;
                txtPaginas.Text = libroEncontrado.CantidadPaginas.ToString();
                dpFecha.Value = libroEncontrado.FechaCreacion;
                txtPrecio.Text = libroEncontrado.Precio.ToString();
                MessageBox.Show("Libro encontrado.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                LimpiarCampos();
                MessageBox.Show("No se encontró ningún libro con el título especificado.", "No encontrado", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void btnEliminar_Click(object sender, EventArgs e)
        {
            if (libroEncontrado == null)
            {
                MessageBox.Show("Por favor, primero busque un libro para eliminar.", "Advertencia", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            DialogResult confirmResult = MessageBox.Show("¿Está seguro que desea eliminar este libro?", "Confirmar eliminación",
                                     MessageBoxButtons.YesNo, MessageBoxIcon.Question);

            if (confirmResult == DialogResult.Yes)
            {
                try
                {
                    bool eliminado = servicioLibro.EliminarLibro(libroEncontrado.Titulo);

                    if (eliminado)
                    {
                        MessageBox.Show("El libro ha sido eliminado exitosamente.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
                        LimpiarCampos();
                        libroEncontrado = null;
                    }
                    else
                    {
                        MessageBox.Show("No se pudo eliminar el libro. Por favor, inténtelo de nuevo.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Ocurrió un error al eliminar el libro: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        private void LimpiarCampos()
        {
            txtBuscar.Text = "";
            txtTitulo.Text = "";
            txtAutor.Text = "";
            txtPaginas.Text = "";
            dpFecha.Value = DateTime.Now;
            txtPrecio.Text = "";
        }
    }
}
