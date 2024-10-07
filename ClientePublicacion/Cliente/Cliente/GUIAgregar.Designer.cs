namespace Cliente
{
    partial class GUIAgregar
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
            this.lblAgregarLibro = new System.Windows.Forms.Label();
            this.lblTitulo = new System.Windows.Forms.Label();
            this.lblAutor = new System.Windows.Forms.Label();
            this.lblCantidadPaginas = new System.Windows.Forms.Label();
            this.lblFechaCreacion = new System.Windows.Forms.Label();
            this.lblPrecio = new System.Windows.Forms.Label();
            this.txtTitulo = new System.Windows.Forms.TextBox();
            this.txtAutores = new System.Windows.Forms.TextBox();
            this.txtPaginas = new System.Windows.Forms.TextBox();
            this.txtPrecio = new System.Windows.Forms.TextBox();
            this.btnAgregar = new System.Windows.Forms.Button();
            this.dpFecha = new System.Windows.Forms.DateTimePicker();
            this.cbxAutores = new System.Windows.Forms.ComboBox();
            this.btnAgregarAutor = new System.Windows.Forms.Button();
            this.chxTapaDura = new System.Windows.Forms.CheckBox();
            this.SuspendLayout();
            // 
            // lblAgregarLibro
            // 
            this.lblAgregarLibro.AutoSize = true;
            this.lblAgregarLibro.Font = new System.Drawing.Font("Arial Rounded MT Bold", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblAgregarLibro.Location = new System.Drawing.Point(16, 11);
            this.lblAgregarLibro.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblAgregarLibro.Name = "lblAgregarLibro";
            this.lblAgregarLibro.Size = new System.Drawing.Size(221, 34);
            this.lblAgregarLibro.TabIndex = 0;
            this.lblAgregarLibro.Text = "Agregar Libro";
            // 
            // lblTitulo
            // 
            this.lblTitulo.AutoSize = true;
            this.lblTitulo.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTitulo.Location = new System.Drawing.Point(19, 64);
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
            this.lblAutor.Location = new System.Drawing.Point(19, 100);
            this.lblAutor.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblAutor.Name = "lblAutor";
            this.lblAutor.Size = new System.Drawing.Size(87, 23);
            this.lblAutor.TabIndex = 2;
            this.lblAutor.Text = "Autores";
            this.lblAutor.Click += new System.EventHandler(this.lblAutor_Click);
            // 
            // lblCantidadPaginas
            // 
            this.lblCantidadPaginas.AutoSize = true;
            this.lblCantidadPaginas.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblCantidadPaginas.Location = new System.Drawing.Point(19, 184);
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
            this.lblFechaCreacion.Location = new System.Drawing.Point(19, 221);
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
            this.lblPrecio.Location = new System.Drawing.Point(19, 256);
            this.lblPrecio.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblPrecio.Name = "lblPrecio";
            this.lblPrecio.Size = new System.Drawing.Size(73, 23);
            this.lblPrecio.TabIndex = 5;
            this.lblPrecio.Text = "Precio";
            // 
            // txtTitulo
            // 
            this.txtTitulo.Location = new System.Drawing.Point(168, 64);
            this.txtTitulo.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtTitulo.Name = "txtTitulo";
            this.txtTitulo.Size = new System.Drawing.Size(265, 22);
            this.txtTitulo.TabIndex = 6;
            this.txtTitulo.TextChanged += new System.EventHandler(this.txtTitulo_TextChanged);
            // 
            // txtAutores
            // 
            this.txtAutores.Enabled = false;
            this.txtAutores.Location = new System.Drawing.Point(168, 100);
            this.txtAutores.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtAutores.Name = "txtAutores";
            this.txtAutores.Size = new System.Drawing.Size(265, 22);
            this.txtAutores.TabIndex = 7;
            // 
            // txtPaginas
            // 
            this.txtPaginas.Location = new System.Drawing.Point(168, 184);
            this.txtPaginas.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtPaginas.Name = "txtPaginas";
            this.txtPaginas.Size = new System.Drawing.Size(265, 22);
            this.txtPaginas.TabIndex = 8;
            // 
            // txtPrecio
            // 
            this.txtPrecio.Location = new System.Drawing.Point(168, 257);
            this.txtPrecio.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtPrecio.Name = "txtPrecio";
            this.txtPrecio.Size = new System.Drawing.Size(265, 22);
            this.txtPrecio.TabIndex = 10;
            // 
            // btnAgregar
            // 
            this.btnAgregar.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnAgregar.Location = new System.Drawing.Point(300, 317);
            this.btnAgregar.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.btnAgregar.Name = "btnAgregar";
            this.btnAgregar.Size = new System.Drawing.Size(133, 34);
            this.btnAgregar.TabIndex = 11;
            this.btnAgregar.Text = "Agregar";
            this.btnAgregar.UseVisualStyleBackColor = true;
            this.btnAgregar.Click += new System.EventHandler(this.btnAgregar_Click);
            // 
            // dpFecha
            // 
            this.dpFecha.Location = new System.Drawing.Point(168, 222);
            this.dpFecha.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.dpFecha.Name = "dpFecha";
            this.dpFecha.Size = new System.Drawing.Size(265, 22);
            this.dpFecha.TabIndex = 12;
            // 
            // cbxAutores
            // 
            this.cbxAutores.FormattingEnabled = true;
            this.cbxAutores.Location = new System.Drawing.Point(23, 140);
            this.cbxAutores.Name = "cbxAutores";
            this.cbxAutores.Size = new System.Drawing.Size(262, 24);
            this.cbxAutores.TabIndex = 13;
            // 
            // btnAgregarAutor
            // 
            this.btnAgregarAutor.Font = new System.Drawing.Font("Arial Rounded MT Bold", 7.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnAgregarAutor.Location = new System.Drawing.Point(300, 140);
            this.btnAgregarAutor.Name = "btnAgregarAutor";
            this.btnAgregarAutor.Size = new System.Drawing.Size(133, 24);
            this.btnAgregarAutor.TabIndex = 14;
            this.btnAgregarAutor.Text = "Agregar autor";
            this.btnAgregarAutor.UseVisualStyleBackColor = true;
            // 
            // chxTapaDura
            // 
            this.chxTapaDura.AutoSize = true;
            this.chxTapaDura.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.chxTapaDura.Location = new System.Drawing.Point(23, 286);
            this.chxTapaDura.Name = "chxTapaDura";
            this.chxTapaDura.Size = new System.Drawing.Size(186, 27);
            this.chxTapaDura.TabIndex = 16;
            this.chxTapaDura.Text = "Tiene tapa dura";
            this.chxTapaDura.UseVisualStyleBackColor = true;
            this.chxTapaDura.CheckedChanged += new System.EventHandler(this.checkBox1_CheckedChanged);
            // 
            // GUIAgregar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(448, 364);
            this.Controls.Add(this.chxTapaDura);
            this.Controls.Add(this.btnAgregarAutor);
            this.Controls.Add(this.cbxAutores);
            this.Controls.Add(this.dpFecha);
            this.Controls.Add(this.btnAgregar);
            this.Controls.Add(this.txtPrecio);
            this.Controls.Add(this.txtPaginas);
            this.Controls.Add(this.txtAutores);
            this.Controls.Add(this.txtTitulo);
            this.Controls.Add(this.lblPrecio);
            this.Controls.Add(this.lblFechaCreacion);
            this.Controls.Add(this.lblCantidadPaginas);
            this.Controls.Add(this.lblAutor);
            this.Controls.Add(this.lblTitulo);
            this.Controls.Add(this.lblAgregarLibro);
            this.ForeColor = System.Drawing.SystemColors.ControlText;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "GUIAgregar";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Agregar";
            this.Load += new System.EventHandler(this.GUIAgregar_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblAgregarLibro;
        private System.Windows.Forms.Label lblTitulo;
        private System.Windows.Forms.Label lblAutor;
        private System.Windows.Forms.Label lblCantidadPaginas;
        private System.Windows.Forms.Label lblFechaCreacion;
        private System.Windows.Forms.Label lblPrecio;
        private System.Windows.Forms.TextBox txtTitulo;
        private System.Windows.Forms.TextBox txtAutores;
        private System.Windows.Forms.TextBox txtPaginas;
        private System.Windows.Forms.TextBox txtPrecio;
        private System.Windows.Forms.Button btnAgregar;
        private System.Windows.Forms.DateTimePicker dpFecha;
        private System.Windows.Forms.ComboBox cbxAutores;
        private System.Windows.Forms.Button btnAgregarAutor;
        private System.Windows.Forms.CheckBox chxTapaDura;
    }
}