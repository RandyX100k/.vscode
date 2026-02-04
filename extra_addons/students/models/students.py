from odoo import models , fields , api
from odoo.exceptions  import ValidationError

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
    
    estudiante_id = fields.Many2one("res.partner",String="Estudiante" , required=True, domain=[ ("is_teacher", "=", False) ] )
    curso_id = fields.Many2one("cursos.estudiantes", String="Cursos")

    esta_reprobado = fields.Boolean(string="Esta reprobado?",default=True)
    
    pais_id = fields.Many2one("res.country",string="Pais" , related="estudiante_id.country_id")
   
    
    
    calificaciones_ids = fields.One2many("calificaciones.estudiantes","estudiante_id",string="Calificaciones")
    
    tag_ids = fields.Many2many("res.partner.category",string="Etiquetas")
    
    addrees = fields.Char(string="Direccion link google map")
    
    note = fields.Char(string="Nota")
    
    edad = fields.Integer(string="Edad")
    
    
    def unlink(self):
        
        for record in self:
            if record.curso_id:
                raise ValidationError("Este estudiante no se puede eliminar tiene un curso")
        
        
        return super().unlink()                
    
    
    
    def copy(self,default=None):
        
        raise ValidationError("No puedes duplicar esos registros")
    
    
    
    
    def reprobar(self):
        
        return{
            "name": "Reprobar",
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.calification",
            "target": "new",
            "context":{
                "default_estudiante_id": self.id
            }
        }
        
        
    
    @api.constrains("estudiante_id")
    def _check_estudiante_id(self):
        
        for record in self:
            
            if record.estudiante_id and self.search_count(
                [("estudiante_id","=",record.estudiante_id),("id","!=", record.id)]
                
                ):
                
                raise ValidationError("El estudiante ya existe")
            
    
    @api.onchange("edad")
    def _check_edad(self):
        for record in self:
            if record.edad:
            
                if record.edad <=14:
                    raise ValidationError("La edad del estudiante debe ser mayor a 14 años")