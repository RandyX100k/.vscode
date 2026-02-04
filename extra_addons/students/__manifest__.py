{
    "name": "Estudiantes",
    "category": "students",
    "author": "Randy Ciprian",
    
    "depends":[
        "web",
        "website"
    ],
    
    "data":[
        "views/view_list_students.xml",
        "views/view_form.xml",
        "views/view_students.xml",
        "views/view_student_template.xml",
        "wizard/views.xml",
        "security/security.xml",
        "security/ir.model.access.csv"
    ],
    
    
    "assets":{
        "web.assets_frontend":[
            "/students/static/src/xml/**/*.xml",
            "/students/static/src/css/**/*.css",
            "/students/static/src/js/**/*.js"
            
        ]
    }
    

}