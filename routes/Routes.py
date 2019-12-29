from models.Actividad import Actividad
from flask import request
from flask import render_template
def routes(app):
    @app.route('/')
    def main():
        actividades = Actividad.query.all()
        return render_template("actividades.html",actividades=actividades)
    @app.route("/actividad/<int:id>")
    def actividad(id):
        actividad = Actividad.query.filter_by(id=id)[0];
        return render_template("verActividad.html",actividad=actividad)
    @app.route("/actividad/edit/<int:id>")
    def editar(id):
        actividad = Actividad.query.filter_by(id=id)[0];
        return render_template("modificarActividad.html",actividad=actividad)
    @app.route('/actividad/<int:id>/update',methods=['POST'])
    def update(id):
        actividad = Actividad.query.filter_by(id=id)[0];
        actividad.nombre = request.form['nombre']
        actividad.descripcion = request.form['descripcion']
        actividad.save()
        return render_template("success.html",operacion="Actualizado",id=actividad.id)
    @app.route('/registrar')
    def registrar():
        return render_template('registro.html')
    @app.route('/store',methods=['POST'])
    def store():
        actividad = Actividad()
        actividad.nombre=request.form['nombre']
        actividad.descripcion=request.form['descripcion']
        actividad.save()
        return render_template('savesuccess.html')
