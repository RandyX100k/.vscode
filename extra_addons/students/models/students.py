from odoo import models , fields


class Students(models.Model):
    _name = "students.info"
    _rec_name = "estudiante_id"
    
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
    
    pais_id = fields.Many2one("res.country",string="Pais" , related="estudiante_id.country_id")
   
    
    
    calificaciones_ids = fields.One2many("calificaciones.estudiantes","estudiante_id",string="Calificaciones")
    
    tag_ids = fields.Many2many("res.partner.category",string="Etiquetas")
    
    addrees = fields.Char(string="Direccion link google map")
    