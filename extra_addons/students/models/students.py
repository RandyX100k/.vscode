from odoo import models , fields


class Students(models.Model):
    _name = "students.info"
    
    estado_calificacion = fields.Selection(
        [
            ("reprobado","Reprobado"),
            ("aprobado","Aprobado")
        ]
    )
    # nombre = fields.Char(string="Nombre del estudiante")
    # apellido = fields.Char(string="Apellido del estudiante")
    # edad = fields.Integer(string="Edad" , default=0)
    
    estudiante_id = fields.Many2one("res.partner",String="Estudiante" , required=True )
    curso_id = fields.Many2one("cursos.estudiantes", String="Cursos")

    esta_reprobado = fields.Boolean(string="Esta reprobado?",default=True)
    
    
    nota = fields.Html(string="Nota")
    