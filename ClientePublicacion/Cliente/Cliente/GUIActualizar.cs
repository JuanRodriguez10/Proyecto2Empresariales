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
    public partial class GUIActualizar : Form
    {
        private ServicioLibroCliente servicioLibro;
        private Libro libroEncontrado;
        private string tituloOriginal;
        public GUIActualizar()
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
            if (string.IsNullOrEmpty(tituloBuscar))
            {
                MessageBox.Show("Por favor, ingrese un título para buscar.", "Advertencia", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            libroEncontrado = servicioLibro.BuscarLibroPorTitulo(tituloBuscar);

            if (libroEncontrado != null)
            {
                tituloOriginal = libroEncontrado.Titulo;
                txtTitulo.Text = libroEncontrado.Titulo;
                txtAutor.Text = libroEncontrado.Autor;
                txtPaginas.Text = libroEncontrado.CantidadPaginas.ToString();
                dpFecha.Value = libroEncontrado.FechaCreacion;
                txtPrecio.Text = libroEncontrado.Precio.ToString();
                MessageBox.Show("Libro encontrado. Puede modificar los campos y luego presionar 'Actualizar'.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                LimpiarCampos();
                MessageBox.Show("No se encontró ningún libro con el título especificado.", "No encontrado", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void btnActualizar_Click(object sender, EventArgs e)
        {
            if (libroEncontrado == null)
            {
                MessageBox.Show("Por favor, primero busque un libro para actualizar.", "Advertencia", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            if (!ValidarCampos())
            {
                return;
            }

            try
            {
                int paginas = int.Parse(txtPaginas.Text);
                double precio = double.Parse(txtPrecio.Text);
                string nuevoTitulo = txtTitulo.Text.Trim();
                DateTime fecha = dpFecha.Value;
                string autor = txtAutor.Text.Trim();

                bool actualizado = servicioLibro.ActualizarLibro(tituloOriginal, paginas, precio, nuevoTitulo, fecha, autor);

                if (actualizado)
                {
                    MessageBox.Show("El libro ha sido actualizado exitosamente.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    LimpiarCampos();
                    libroEncontrado = null;
                }
                else
                {
                    MessageBox.Show("No se pudo actualizar el libro. Por favor, inténtelo de nuevo.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (FormatException)
            {
                MessageBox.Show("Por favor, asegúrese de que los campos 'Páginas' y 'Precio' contengan valores numéricos válidos.", "Error de formato", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ocurrió un error al actualizar el libro: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private bool ValidarCampos()
        {
            if (string.IsNullOrWhiteSpace(txtTitulo.Text) ||
                string.IsNullOrWhiteSpace(txtAutor.Text) ||
                string.IsNullOrWhiteSpace(txtPaginas.Text) ||
                string.IsNullOrWhiteSpace(txtPrecio.Text))
            {
                MessageBox.Show("Todos los campos son obligatorios. Por favor, complete todos los campos.", "Campos incompletos", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return false;
            }
            return true;
        }

        private void LimpiarCampos()
        {
            txtBuscar.Text = "";
            txtTitulo.Text = "";
            txtAutor.Text = "";
            txtPaginas.Text = "";
            dpFecha.Value = DateTime.Now;
            txtPrecio.Text = "";
            tituloOriginal = null;
        }
    }
}
