from odoo.http import Controller , route , request
import json


class UserController(Controller):
    
    @route("/students" , auth="user", type="http")
    def students(self):
        
        return request.make_response(
            json.dumps(
                {
                    "name": "jose"
                }
            )
        )

    
    
    @route("/new/students",auth="public", type="http",methods=["POST"] , csrf=False)
    def new_students(self,**kwargs):
        
        name = kwargs.get("name")
        
        if name:
        
        
            new_contact = request.env["res.partner"].sudo().create({
                "name": name
            })
            
            
            new_students = request.env["students.info"].sudo().create({
                "estudiante_id": int(new_contact.id)
            })
            
            
            
            return request.make_response(
                json.dumps(
                    {
                        "name": name,
                        "parnert_id": new_contact.id,
                        "estudiante_id": new_students.id
                    }
                )
            )
        
        return request.make_response(
                json.dumps(
                    {
                        "status": "no se puede crear falta el name"
                    }
                )
            )
    
    
    @route("/view/calification",type="http", auth="public", csrf=False , website=True)
    def view_calification(self):
        
        userNow = request.env.user
        
        partner_id = userNow.partner_id.id
        
        student = request.env["students.info"].sudo().search([("estudiante_id","=",partner_id)])
        
        userInfo = {
            "userName": userNow.partner_id.name,
            "estudiante_id": student.id or None
        }

        
        return request.render("students.students_template_students",userInfo)
    