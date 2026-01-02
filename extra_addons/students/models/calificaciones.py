from odoo import models , fields 


class Calificaciones(models.Model):
    _name = "calificaciones.estudiantes"
    
    
    estudiante_id = fields.Many2one("res.partner",string="Estudiante")
    materia_id = fields.Many2one("materias.students",string="Materias")
    calificacion = fields.Float(string="Calificacion")
    
    
    