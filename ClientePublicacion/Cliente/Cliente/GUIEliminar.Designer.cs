namespace Cliente
{
    partial class GUIEliminar
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
            this.lblEliminarLibro = new System.Windows.Forms.Label();
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
            this.txtBuscar = new System.Windows.Forms.TextBox();
            this.btnEliminar = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.chxTapaDura = new System.Windows.Forms.CheckBox();
            this.SuspendLayout();
            // 
            // lblEliminarLibro
            // 
            this.lblEliminarLibro.AutoSize = true;
            this.lblEliminarLibro.Font = new System.Drawing.Font("Arial Rounded MT Bold", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblEliminarLibro.Location = new System.Drawing.Point(16, 11);
            this.lblEliminarLibro.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblEliminarLibro.Name = "lblEliminarLibro";
            this.lblEliminarLibro.Size = new System.Drawing.Size(219, 34);
            this.lblEliminarLibro.TabIndex = 0;
            this.lblEliminarLibro.Text = "Eliminar Libro";
            // 
            // lblTitulo
            // 
            this.lblTitulo.AutoSize = true;
            this.lblTitulo.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTitulo.Location = new System.Drawing.Point(19, 191);
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
            this.lblAutor.Location = new System.Drawing.Point(19, 226);
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
            this.lblCantidadPaginas.Location = new System.Drawing.Point(19, 267);
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
            this.lblFechaCreacion.Location = new System.Drawing.Point(19, 304);
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
            this.lblPrecio.Location = new System.Drawing.Point(19, 338);
            this.lblPrecio.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblPrecio.Name = "lblPrecio";
            this.lblPrecio.Size = new System.Drawing.Size(73, 23);
            this.lblPrecio.TabIndex = 5;
            this.lblPrecio.Text = "Precio";
            // 
            // txtTitulo
            // 
            this.txtTitulo.Enabled = false;
            this.txtTitulo.Location = new System.Drawing.Point(168, 191);
            this.txtTitulo.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtTitulo.Name = "txtTitulo";
            this.txtTitulo.Size = new System.Drawing.Size(265, 22);
            this.txtTitulo.TabIndex = 6;
            // 
            // txtAutores
            // 
            this.txtAutores.Enabled = false;
            this.txtAutores.Location = new System.Drawing.Point(168, 226);
            this.txtAutores.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtAutores.Name = "txtAutores";
            this.txtAutores.Size = new System.Drawing.Size(265, 22);
            this.txtAutores.TabIndex = 7;
            // 
            // txtPaginas
            // 
            this.txtPaginas.Enabled = false;
            this.txtPaginas.Location = new System.Drawing.Point(168, 267);
            this.txtPaginas.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtPaginas.Name = "txtPaginas";
            this.txtPaginas.Size = new System.Drawing.Size(265, 22);
            this.txtPaginas.TabIndex = 8;
            // 
            // txtPrecio
            // 
            this.txtPrecio.Enabled = false;
            this.txtPrecio.Location = new System.Drawing.Point(168, 338);
            this.txtPrecio.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtPrecio.Name = "txtPrecio";
            this.txtPrecio.Size = new System.Drawing.Size(265, 22);
            this.txtPrecio.TabIndex = 10;
            // 
            // btnBuscar
            // 
            this.btnBuscar.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnBuscar.Location = new System.Drawing.Point(301, 90);
            this.btnBuscar.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.btnBuscar.Name = "btnBuscar";
            this.btnBuscar.Size = new System.Drawing.Size(133, 33);
            this.btnBuscar.TabIndex = 11;
            this.btnBuscar.Text = "Buscar";
            this.btnBuscar.UseVisualStyleBackColor = true;
            this.btnBuscar.Click += new System.EventHandler(this.btnBuscar_Click);
            // 
            // dpFecha
            // 
            this.dpFecha.Enabled = false;
            this.dpFecha.Location = new System.Drawing.Point(168, 306);
            this.dpFecha.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.dpFecha.Name = "dpFecha";
            this.dpFecha.Size = new System.Drawing.Size(265, 22);
            this.dpFecha.TabIndex = 12;
            // 
            // txtBuscar
            // 
            this.txtBuscar.Location = new System.Drawing.Point(23, 96);
            this.txtBuscar.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.txtBuscar.Name = "txtBuscar";
            this.txtBuscar.Size = new System.Drawing.Size(252, 22);
            this.txtBuscar.TabIndex = 13;
            // 
            // btnEliminar
            // 
            this.btnEliminar.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnEliminar.Location = new System.Drawing.Point(301, 397);
            this.btnEliminar.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.btnEliminar.Name = "btnEliminar";
            this.btnEliminar.Size = new System.Drawing.Size(133, 34);
            this.btnEliminar.TabIndex = 14;
            this.btnEliminar.Text = "Eliminar";
            this.btnEliminar.UseVisualStyleBackColor = true;
            this.btnEliminar.Click += new System.EventHandler(this.btnEliminar_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.label1.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(19, 59);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(155, 23);
            this.label1.TabIndex = 15;
            this.label1.Text = "Titulo Buscado";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Arial Rounded MT Bold", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(16, 143);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(270, 34);
            this.label2.TabIndex = 16;
            this.label2.Text = "Libro a eliminar...";
            // 
            // chxTapaDura
            // 
            this.chxTapaDura.AutoSize = true;
            this.chxTapaDura.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.chxTapaDura.Location = new System.Drawing.Point(23, 367);
            this.chxTapaDura.Name = "chxTapaDura";
            this.chxTapaDura.Size = new System.Drawing.Size(186, 27);
            this.chxTapaDura.TabIndex = 17;
            this.chxTapaDura.Text = "Tiene tapa dura";
            this.chxTapaDura.UseVisualStyleBackColor = true;
            // 
            // GUIEliminar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(452, 449);
            this.Controls.Add(this.chxTapaDura);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.btnEliminar);
            this.Controls.Add(this.txtBuscar);
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
            this.Controls.Add(this.lblEliminarLibro);
            this.ForeColor = System.Drawing.SystemColors.ControlText;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "GUIEliminar";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Eliminar";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblEliminarLibro;
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
        private System.Windows.Forms.TextBox txtBuscar;
        private System.Windows.Forms.Button btnEliminar;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.CheckBox chxTapaDura;
    }
}