namespace Cliente
{
    partial class GUIListarAutores
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
            this.txtNacionalidad = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.filtrarNacionalidad = new System.Windows.Forms.Button();
            this.tablaAutores = new System.Windows.Forms.DataGridView();
            this.btnListar = new System.Windows.Forms.Button();
            this.lblBuscarLibro = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.tablaAutores)).BeginInit();
            this.SuspendLayout();
            // 
            // txtNacionalidad
            // 
            this.txtNacionalidad.Location = new System.Drawing.Point(204, 315);
            this.txtNacionalidad.Margin = new System.Windows.Forms.Padding(4);
            this.txtNacionalidad.Name = "txtNacionalidad";
            this.txtNacionalidad.Size = new System.Drawing.Size(147, 22);
            this.txtNacionalidad.TabIndex = 24;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(52, 316);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(144, 23);
            this.label1.TabIndex = 23;
            this.label1.Text = "Nacionalidad:";
            // 
            // filtrarNacionalidad
            // 
            this.filtrarNacionalidad.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.filtrarNacionalidad.Location = new System.Drawing.Point(359, 307);
            this.filtrarNacionalidad.Margin = new System.Windows.Forms.Padding(4);
            this.filtrarNacionalidad.Name = "filtrarNacionalidad";
            this.filtrarNacionalidad.Size = new System.Drawing.Size(253, 33);
            this.filtrarNacionalidad.TabIndex = 22;
            this.filtrarNacionalidad.Text = "Filtrar por Nacionalidad";
            this.filtrarNacionalidad.UseVisualStyleBackColor = true;
            // 
            // tablaAutores
            // 
            this.tablaAutores.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.tablaAutores.Location = new System.Drawing.Point(24, 66);
            this.tablaAutores.Margin = new System.Windows.Forms.Padding(4);
            this.tablaAutores.Name = "tablaAutores";
            this.tablaAutores.RowHeadersWidth = 51;
            this.tablaAutores.Size = new System.Drawing.Size(725, 234);
            this.tablaAutores.TabIndex = 21;
            // 
            // btnListar
            // 
            this.btnListar.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnListar.Location = new System.Drawing.Point(616, 307);
            this.btnListar.Margin = new System.Windows.Forms.Padding(4);
            this.btnListar.Name = "btnListar";
            this.btnListar.Size = new System.Drawing.Size(133, 34);
            this.btnListar.TabIndex = 20;
            this.btnListar.Text = "Listar";
            this.btnListar.UseVisualStyleBackColor = true;
            // 
            // lblBuscarLibro
            // 
            this.lblBuscarLibro.AutoSize = true;
            this.lblBuscarLibro.Font = new System.Drawing.Font("Arial Rounded MT Bold", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblBuscarLibro.Location = new System.Drawing.Point(17, 12);
            this.lblBuscarLibro.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblBuscarLibro.Name = "lblBuscarLibro";
            this.lblBuscarLibro.Size = new System.Drawing.Size(279, 43);
            this.lblBuscarLibro.TabIndex = 19;
            this.lblBuscarLibro.Text = "Listar Autores";
            // 
            // GUIListarAutores
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(767, 355);
            this.Controls.Add(this.txtNacionalidad);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.filtrarNacionalidad);
            this.Controls.Add(this.tablaAutores);
            this.Controls.Add(this.btnListar);
            this.Controls.Add(this.lblBuscarLibro);
            this.Name = "GUIListarAutores";
            this.Text = "Listar Autores";
            ((System.ComponentModel.ISupportInitialize)(this.tablaAutores)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox txtNacionalidad;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button filtrarNacionalidad;
        private System.Windows.Forms.DataGridView tablaAutores;
        private System.Windows.Forms.Button btnListar;
        private System.Windows.Forms.Label lblBuscarLibro;
    }
}