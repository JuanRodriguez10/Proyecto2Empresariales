namespace Cliente
{
    partial class GUIAgregarAutor
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
            this.lblAgregarAutor = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.txtNombre = new System.Windows.Forms.TextBox();
            this.lblEdad = new System.Windows.Forms.Label();
            this.lblNacionalidad = new System.Windows.Forms.Label();
            this.txtEdad = new System.Windows.Forms.TextBox();
            this.txtNacionalidad = new System.Windows.Forms.TextBox();
            this.btnAgregarAutor = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblAgregarAutor
            // 
            this.lblAgregarAutor.AutoSize = true;
            this.lblAgregarAutor.Font = new System.Drawing.Font("Arial Rounded MT Bold", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblAgregarAutor.Location = new System.Drawing.Point(13, 9);
            this.lblAgregarAutor.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblAgregarAutor.Name = "lblAgregarAutor";
            this.lblAgregarAutor.Size = new System.Drawing.Size(284, 43);
            this.lblAgregarAutor.TabIndex = 1;
            this.lblAgregarAutor.Text = "Agregar Autor";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(15, 55);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(89, 23);
            this.label1.TabIndex = 2;
            this.label1.Text = "Nombre";
            // 
            // txtNombre
            // 
            this.txtNombre.Location = new System.Drawing.Point(167, 55);
            this.txtNombre.Name = "txtNombre";
            this.txtNombre.Size = new System.Drawing.Size(232, 22);
            this.txtNombre.TabIndex = 3;
            // 
            // lblEdad
            // 
            this.lblEdad.AutoSize = true;
            this.lblEdad.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblEdad.Location = new System.Drawing.Point(15, 92);
            this.lblEdad.Name = "lblEdad";
            this.lblEdad.Size = new System.Drawing.Size(61, 23);
            this.lblEdad.TabIndex = 4;
            this.lblEdad.Text = "Edad";
            // 
            // lblNacionalidad
            // 
            this.lblNacionalidad.AutoSize = true;
            this.lblNacionalidad.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblNacionalidad.Location = new System.Drawing.Point(12, 129);
            this.lblNacionalidad.Name = "lblNacionalidad";
            this.lblNacionalidad.Size = new System.Drawing.Size(138, 23);
            this.lblNacionalidad.TabIndex = 5;
            this.lblNacionalidad.Text = "Nacionalidad";
            // 
            // txtEdad
            // 
            this.txtEdad.Location = new System.Drawing.Point(167, 92);
            this.txtEdad.Name = "txtEdad";
            this.txtEdad.Size = new System.Drawing.Size(232, 22);
            this.txtEdad.TabIndex = 6;
            // 
            // txtNacionalidad
            // 
            this.txtNacionalidad.Location = new System.Drawing.Point(167, 132);
            this.txtNacionalidad.Name = "txtNacionalidad";
            this.txtNacionalidad.Size = new System.Drawing.Size(232, 22);
            this.txtNacionalidad.TabIndex = 7;
            // 
            // btnAgregarAutor
            // 
            this.btnAgregarAutor.Font = new System.Drawing.Font("Arial Rounded MT Bold", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnAgregarAutor.Location = new System.Drawing.Point(258, 172);
            this.btnAgregarAutor.Name = "btnAgregarAutor";
            this.btnAgregarAutor.Size = new System.Drawing.Size(141, 39);
            this.btnAgregarAutor.TabIndex = 8;
            this.btnAgregarAutor.Text = "Agregar";
            this.btnAgregarAutor.UseVisualStyleBackColor = true;
            // 
            // GUIAgregarAutor
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(424, 232);
            this.Controls.Add(this.btnAgregarAutor);
            this.Controls.Add(this.txtNacionalidad);
            this.Controls.Add(this.txtEdad);
            this.Controls.Add(this.lblNacionalidad);
            this.Controls.Add(this.lblEdad);
            this.Controls.Add(this.txtNombre);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.lblAgregarAutor);
            this.Name = "GUIAgregarAutor";
            this.Text = "Agregar autor";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblAgregarAutor;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox txtNombre;
        private System.Windows.Forms.Label lblEdad;
        private System.Windows.Forms.Label lblNacionalidad;
        private System.Windows.Forms.TextBox txtEdad;
        private System.Windows.Forms.TextBox txtNacionalidad;
        private System.Windows.Forms.Button btnAgregarAutor;
    }
}