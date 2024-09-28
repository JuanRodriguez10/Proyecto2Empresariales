using RestSharp;
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
    public partial class GUIPrincipal : Form
    {
        public GUIPrincipal()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void agregarToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GUIAgregar guiAgregar = new GUIAgregar();
            guiAgregar.Show();
        }

        private void buscarToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GUIBuscar gUIBuscar = new GUIBuscar();
            gUIBuscar.Show();
        }

        private void actualizarToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GUIActualizar gUIActualizar = new GUIActualizar();
            gUIActualizar.Show();
        }

        private void eliminarToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GUIEliminar gUIEliminar = new GUIEliminar();
            gUIEliminar.Show();
        }

        private void listarToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GUIListar gUIListar = new GUIListar();
            gUIListar.Show();
        }

        private void salirToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("¿Está seguro que desea salir?", "Confirmar salida",
                MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                this.Close();
            }
        }

        private void desarrolladoresToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string desarrollo = "Desarrollado por:\n\n" +
                    "Juan Felipe Rodriguez Barbosa\n" +
                    "Cod.2220221045\n" +
                    "Juan Esteban Rodriguez Castellanos\n" +
                    "Cod.2220221063\n\n" +
                    "Desarrollo de Aplicaciones Empresariales\n" +
                    "Version 2.0";

MessageBox.Show(desarrollo, "Información", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }
    }
}
