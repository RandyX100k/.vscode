from odoo import models , fields , api


class Calificaciones(models.Model):
    _name = "calificaciones.estudiantes"
    
    
    estudiante_id = fields.Many2one("students.info",string="Estudiante")
    materia_id = fields.Many2one("materias.students",string="Materias")
    calificacion = fields.Float(string="Calificacion")
    estado_materia = fields.Selection(
        [
            ("aprobado","Aprobado"),
            ("reprobado","Reprobado")
        ],
        
        compute="_check_calificacion",
        store=True
    )
    
    
    
    @api.depends("calificacion")
    def _check_calificacion(self):
        
        for record in self:
            
            if record.calificacion <= 69:
                record.estado_materia = "reprobado"
            
            else:
                record.estado_materia = "aprobado"
            
    
    