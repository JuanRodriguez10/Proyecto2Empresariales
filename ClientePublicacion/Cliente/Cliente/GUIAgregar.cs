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
            var paginasTexto = txtPaginas.Text.Trim();
            int paginas = int.Parse(paginasTexto);

            var precioTexto = txtPrecio.Text.Trim();
            double precio = double.Parse(precioTexto);

            var titulo = txtTitulo.Text.Trim();

            DateTime fecha = dpFecha.Value;

            var autor = txtAutor.Text.Trim();

            bool agregado = servicioLibro.AgregarLibro(paginas, precio, titulo, fecha, autor);

            if (agregado)
            {
                txtPaginas.Text = "";
                txtPrecio.Text = "";
                txtTitulo.Text = "";
                dpFecha.Value = DateTime.Now;
                txtAutor.Text = "";

                MessageBox.Show("El libro fue agregado exitosamente.", "Confirmación", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("Hubo un error al agregar el libro.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }


        }
    }
}
