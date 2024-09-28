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
        public GUIBuscar()
        {
            InitializeComponent();
            this.ActiveControl = txtBuscar;
        }

        private void lblCantidadPaginas_Click(object sender, EventArgs e)
        {

        }
    }
}
