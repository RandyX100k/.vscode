from odoo import models , fields


class Cursos(models.Model):
    
    _name = "cursos.estudiantes"
    _rec_name = "nombre"
    
    nombre = fields.Char(string="Nombre curso")