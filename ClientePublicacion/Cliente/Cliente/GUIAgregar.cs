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
    public partial class GUIAgregar : Form
    {
        private ServicioLibroCliente servicioLibro;
        public GUIAgregar()
        {
            servicioLibro = new ServicioLibroCliente();
            InitializeComponent();
        }

        private void lblCantidadPaginas_Click(object sender, EventArgs e)
        {

        }

        private void GUIAgregar_Load(object sender, EventArgs e)
        {

        }

        private void txtTitulo_TextChanged(object sender, EventArgs e)
        {

        }

        private void btnAgregar_Click(object sender, EventArgs e)
        {
            try
            {
                var paginasTexto = txtPaginas.Text.Trim();
                if (!int.TryParse(paginasTexto, out int paginas))
                {
                    MessageBox.Show("El número de páginas debe ser un valor numérico entero.", "Error de entrada", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                var precioTexto = txtPrecio.Text.Trim();
                if (!double.TryParse(precioTexto, out double precio))
                {
                    MessageBox.Show("El precio debe ser un valor numérico válido.", "Error de entrada", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                var titulo = txtTitulo.Text.Trim();
                if (string.IsNullOrEmpty(titulo))
                {
                    MessageBox.Show("El título no puede estar vacío.", "Error de entrada", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                DateTime fecha = dpFecha.Value;

                var autor = txtAutores.Text.Trim();
                if (string.IsNullOrEmpty(autor))
                {
                    MessageBox.Show("El autor no puede estar vacío.", "Error de entrada", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                bool agregado = servicioLibro.AgregarLibro(paginas, precio, titulo, fecha, autor);
                if (agregado)
                {
                    LimpiarCampos();
                    MessageBox.Show("El libro fue agregado exitosamente.", "Confirmación", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                else
                {
                    MessageBox.Show("Hubo un error al agregar el libro.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Se produjo un error inesperado: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void LimpiarCampos()
        {
            txtPaginas.Text = "";
            txtPrecio.Text = "";
            txtTitulo.Text = "";
            dpFecha.Value = DateTime.Now;
            txtAutores.Text = "";
        }

        private void lblAutor_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {

        }
    }
}
