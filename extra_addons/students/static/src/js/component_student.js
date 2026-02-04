/**@odoo-module **/

import { Component, useState, onWillStart, onWillRender, onMounted , useRef } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";


export class StudentsComponent extends Component {

    static template = "students.view_calification_student";
    static props = {
        userName: String,
        estudiante_id: Number
    }

    setup() {

        this.ui = useService("ui");
        this.notification = useService("notification");
        this.state = useState({ number: 0, edad: 0, calificaciones: [] });
        this.orm = useService("orm"); //search , searchRead , Read etc'
        this.input_edad = useRef("input_edad");


        onMounted(() => {
            console.log("on mounted");
        })

        onWillStart(async () => {

            const student = await this.orm.searchRead("students.info", [["id", "=", this.props.estudiante_id]], ["edad"]);

            if (!student) {
                this.notification.add("No se encontro el estudiante", { type: "danger" })
                return;
            }


            console.log(student);
            this.state.edad = student[0].edad;


            const califications = await this.orm.searchRead("calificaciones.estudiantes", [["estudiante_id", "=", this.props.estudiante_id]], ["id", "materia_id", "calificacion", "estado_materia"])

            this.state.calificaciones = califications;

        })


        onWillRender(() => {
            this.notification.add("cambio", { type: "success" })
        })


    }

    openAlert() {
        this.ui.block();

        setTimeout(() => {
            this.ui.unblock();
        }, 5000)

    }


    viewInput(ev) {

        console.log(ev.target.value);

    }


    viewNotification() {
        this.notification.add("Mostrando alerta", { type: "danger" })
    }



    changeNumber() {
        this.state.number++;
    }

    validarEdad(){
        const valueAge = parseInt( this.input_edad.el.value );
        if(valueAge < 18 || !valueAge){
            this.notification.add("La edad no cumple los requisitos", {type: "danger"});
            return;
        }

        this.notification.add("La edad es correcta eres apto");
    }

}

registry.category("public_components").add("students.student_component", StudentsComponent)