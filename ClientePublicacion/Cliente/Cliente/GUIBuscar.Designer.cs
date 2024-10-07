namespace Cliente
{
    partial class GUIBuscar
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblBuscarLibro = new System.Windows.Forms.Label();
            this.lblTitulo = new System.Windows.Forms.Label();
            this.lblAutor = new System.Windows.Forms.Label();
            this.lblCantidadPaginas = new System.Windows.Forms.Label();
            this.lblFechaCreacion = new System.Windows.Forms.Label();
            this.lblPrecio = new System.Windows.Forms.Label();
            this.txtTitulo = new System.Windows.Forms.TextBox();
            this.txtAutores = new System.Windows.Forms.TextBox();
            this.txtPaginas = new System.Windows.Forms.TextBox();
            this.txtPrecio = new System.Windows.Forms.TextBox();
            this.btnBuscar = new System.Windows.Forms.Button();
            this.dpFecha = new System.Windows.Forms.DateTimePicker();
            this.txtTituloBuscar = new System.Windows.Forms.TextBox();
            this.txtTituloBuscado = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.txtAutorBuscado = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.chxTapaDura = new System.Windows.Forms.CheckBox();
            this.SuspendLayout();
            // 
            // lblBuscarLibro
            // 
            this.lblBuscarLibro.AutoSize = true;
            this.lblBuscarLibro.Font = new System.Drawing.Font("Arial Rounded MT Bold", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblBuscarLibro.Location = new System.Drawing.Point(16, 11);
            this.lblBuscarLibro.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblBuscarLibro.Name = "lblBuscarLibro";
            this.lblBuscarLibro.Size = new System.Drawing.Size(204, 34);
            this.lblBuscarLibro.TabIndex = 0;
            this.lblBuscarLibro.Text = "Buscar Libro";
            // 
            // lblTitulo
            // 
            this.lblTitulo.AutoSize = true;
            this.lblTitulo.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTitulo.Location = new System.Drawing.Point(19, 242);
            this.lblTitulo.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblTitulo.Name = "lblTitulo";
            this.lblTitulo.Size = new System.Drawing.Size(64, 23);
            this.lblTitulo.TabIndex = 1;
            this.lblTitulo.Text = "Título";
            // 
            // lblAutor
            // 
            this.lblAutor.AutoSize = true;
            this.lblAutor.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblAutor.Location = new System.Drawing.Point(19, 278);
            this.lblAutor.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblAutor.Name = "lblAutor";
            this.lblAutor.Size = new System.Drawing.Size(109, 29);
            this.lblAutor.TabIndex = 2;
            this.lblAutor.Text = "Autores";
            // 
            // lblCantidadPaginas
            // 
            this.lblCantidadPaginas.AutoSize = true;
            this.lblCantidadPaginas.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblCantidadPaginas.Location = new System.Drawing.Point(19, 316);
            this.lblCantidadPaginas.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblCantidadPaginas.Name = "lblCantidadPaginas";
            this.lblCantidadPaginas.Size = new System.Drawing.Size(126, 23);
            this.lblCantidadPaginas.TabIndex = 3;
            this.lblCantidadPaginas.Text = "No. páginas";
            this.lblCantidadPaginas.Click += new System.EventHandler(this.lblCantidadPaginas_Click);
            // 
            // lblFechaCreacion
            // 
            this.lblFechaCreacion.AutoSize = true;
            this.lblFechaCreacion.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblFechaCreacion.Location = new System.Drawing.Point(19, 357);
            this.lblFechaCreacion.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblFechaCreacion.Name = "lblFechaCreacion";
            this.lblFechaCreacion.Size = new System.Drawing.Size(70, 23);
            this.lblFechaCreacion.TabIndex = 4;
            this.lblFechaCreacion.Text = "Fecha";
            // 
            // lblPrecio
            // 
            this.lblPrecio.AutoSize = true;
            this.lblPrecio.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblPrecio.Location = new System.Drawing.Point(19, 391);
            this.lblPrecio.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblPrecio.Name = "lblPrecio";
            this.lblPrecio.Size = new System.Drawing.Size(73, 23);
            this.lblPrecio.TabIndex = 5;
            this.lblPrecio.Text = "Precio";
            // 
            // txtTitulo
            // 
            this.txtTitulo.Enabled = false;
            this.txtTitulo.Location = new System.Drawing.Point(168, 242);
            this.txtTitulo.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtTitulo.Name = "txtTitulo";
            this.txtTitulo.Size = new System.Drawing.Size(265, 22);
            this.txtTitulo.TabIndex = 6;
            // 
            // txtAutores
            // 
            this.txtAutores.Enabled = false;
            this.txtAutores.Location = new System.Drawing.Point(168, 278);
            this.txtAutores.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtAutores.Name = "txtAutores";
            this.txtAutores.Size = new System.Drawing.Size(265, 22);
            this.txtAutores.TabIndex = 7;
            // 
            // txtPaginas
            // 
            this.txtPaginas.Enabled = false;
            this.txtPaginas.Location = new System.Drawing.Point(168, 319);
            this.txtPaginas.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtPaginas.Name = "txtPaginas";
            this.txtPaginas.Size = new System.Drawing.Size(265, 22);
            this.txtPaginas.TabIndex = 8;
            // 
            // txtPrecio
            // 
            this.txtPrecio.Enabled = false;
            this.txtPrecio.Location = new System.Drawing.Point(168, 391);
            this.txtPrecio.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtPrecio.Name = "txtPrecio";
            this.txtPrecio.Size = new System.Drawing.Size(265, 22);
            this.txtPrecio.TabIndex = 10;
            // 
            // btnBuscar
            // 
            this.btnBuscar.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnBuscar.Location = new System.Drawing.Point(303, 86);
            this.btnBuscar.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.btnBuscar.Name = "btnBuscar";
            this.btnBuscar.Size = new System.Drawing.Size(133, 58);
            this.btnBuscar.TabIndex = 11;
            this.btnBuscar.Text = "Buscar";
            this.btnBuscar.UseVisualStyleBackColor = true;
            this.btnBuscar.Click += new System.EventHandler(this.btnBuscar_Click);
            // 
            // dpFecha
            // 
            this.dpFecha.Enabled = false;
            this.dpFecha.Location = new System.Drawing.Point(168, 358);
            this.dpFecha.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.dpFecha.Name = "dpFecha";
            this.dpFecha.Size = new System.Drawing.Size(265, 22);
            this.dpFecha.TabIndex = 12;
            // 
            // txtTituloBuscar
            // 
            this.txtTituloBuscar.Location = new System.Drawing.Point(23, 86);
            this.txtTituloBuscar.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtTituloBuscar.Name = "txtTituloBuscar";
            this.txtTituloBuscar.Size = new System.Drawing.Size(252, 22);
            this.txtTituloBuscar.TabIndex = 13;
            // 
            // txtTituloBuscado
            // 
            this.txtTituloBuscado.AutoSize = true;
            this.txtTituloBuscado.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.txtTituloBuscado.Location = new System.Drawing.Point(19, 60);
            this.txtTituloBuscado.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.txtTituloBuscado.Name = "txtTituloBuscado";
            this.txtTituloBuscado.Size = new System.Drawing.Size(155, 23);
            this.txtTituloBuscado.TabIndex = 14;
            this.txtTituloBuscado.Text = "Titulo Buscado";
            this.txtTituloBuscado.Click += new System.EventHandler(this.label1_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(19, 122);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(155, 23);
            this.label1.TabIndex = 15;
            this.label1.Text = "Autor Buscado";
            // 
            // txtAutorBuscado
            // 
            this.txtAutorBuscado.Location = new System.Drawing.Point(20, 148);
            this.txtAutorBuscado.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtAutorBuscado.Name = "txtAutorBuscado";
            this.txtAutorBuscado.Size = new System.Drawing.Size(252, 22);
            this.txtAutorBuscado.TabIndex = 16;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Arial Rounded MT Bold", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(13, 196);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(118, 34);
            this.label2.TabIndex = 17;
            this.label2.Text = "Libro...";
            // 
            // chxTapaDura
            // 
            this.chxTapaDura.AutoSize = true;
            this.chxTapaDura.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.chxTapaDura.Location = new System.Drawing.Point(22, 420);
            this.chxTapaDura.Name = "chxTapaDura";
            this.chxTapaDura.Size = new System.Drawing.Size(186, 27);
            this.chxTapaDura.TabIndex = 18;
            this.chxTapaDura.Text = "Tiene tapa dura";
            this.chxTapaDura.UseVisualStyleBackColor = true;
            // 
            // GUIBuscar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(452, 460);
            this.Controls.Add(this.chxTapaDura);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.txtAutorBuscado);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.txtTituloBuscado);
            this.Controls.Add(this.txtTituloBuscar);
            this.Controls.Add(this.dpFecha);
            this.Controls.Add(this.btnBuscar);
            this.Controls.Add(this.txtPrecio);
            this.Controls.Add(this.txtPaginas);
            this.Controls.Add(this.txtAutores);
            this.Controls.Add(this.txtTitulo);
            this.Controls.Add(this.lblPrecio);
            this.Controls.Add(this.lblFechaCreacion);
            this.Controls.Add(this.lblCantidadPaginas);
            this.Controls.Add(this.lblAutor);
            this.Controls.Add(this.lblTitulo);
            this.Controls.Add(this.lblBuscarLibro);
            this.ForeColor = System.Drawing.SystemColors.ControlText;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "GUIBuscar";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Buscar";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblBuscarLibro;
        private System.Windows.Forms.Label lblTitulo;
        private System.Windows.Forms.Label lblAutor;
        private System.Windows.Forms.Label lblCantidadPaginas;
        private System.Windows.Forms.Label lblFechaCreacion;
        private System.Windows.Forms.Label lblPrecio;
        private System.Windows.Forms.TextBox txtTitulo;
        private System.Windows.Forms.TextBox txtAutores;
        private System.Windows.Forms.TextBox txtPaginas;
        private System.Windows.Forms.TextBox txtPrecio;
        private System.Windows.Forms.Button btnBuscar;
        private System.Windows.Forms.DateTimePicker dpFecha;
        private System.Windows.Forms.TextBox txtTituloBuscar;
        private System.Windows.Forms.Label txtTituloBuscado;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtAutorBuscado;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.CheckBox chxTapaDura;
    }
}