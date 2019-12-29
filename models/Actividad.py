from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Actividad(db.Model):
    __tablename__="actividad"
    id = db.Column(db.Integer,primary_key=True,
    autoincrement=True)
    nombre = db.Column(db.String,nullable=False)
    descripcion = db.Column(db.String,nullable=False)
    def save(self):
        db.session.add(self)
        db.session.commit()