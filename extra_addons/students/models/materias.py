from odoo import models , fields


class Materias(models.Model):
    _name = "materias.students"
    
    name = fields.Char(string="Materia nombre",required=True)
    profesor_id = fields.Many2one("res.partner",string="Profesor" , required=True , domain=[("is_teacher","=",True)])
    