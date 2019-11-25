from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pais(db.Model):
    __tablename__='paises'
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(50), unique = True, nullable = False)

    def __repr__(self):
        return '<Pais %r>' % self.name
            
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name
        }


class Role(db.Model):
    __tablename__='roles'
    id = db.Column(db.Integer, primary_key = True) 
    descripcion = db.Column(db.String(50), unique = True, nullable = False)

    def __repr__(self):
        return '<Role %r>' % self.descripcion
            
    def serialize(self):
        return {
            'id':self.id,
            'descripcion':self.descripcion
        }

class Categoria(db.Model):
    __tablename__='categorias'
    id = db.Column(db.Integer, primary_key = True) 
    descripcion = db.Column(db.String(50), unique = True, nullable = False)

    def __repr__(self):
        return '<Categoria %r>' % self.name
            
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name
        }        