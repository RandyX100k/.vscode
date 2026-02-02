from odoo import models , fields
from odoo.exceptions import ValidationError


class WizardCalification(models.TransientModel):
    _name = "wizard.calification"
    
    estudiante_id = fields.Many2one("students.info",string="Estudiante")
    nota = fields.Char(string="Nota")
    
    
    
    def reprobar(self):
        
        if not self.estudiante_id:
            raise ValidationError("No mandaste el estudiante")
        
        
        estudent = self.env["students.info"].browse(self.estudiante_id.id)
        
        
        if estudent:
            estudent.esta_reprobado = True
            estudent.note = self.nota