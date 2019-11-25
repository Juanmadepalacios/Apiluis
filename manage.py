from flask import Flask, render_template, request, jsonify
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_cors import CORS
from models import db, Pais
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html', name="home")

@app.route('/paises', methods=['GET', 'POST'])
@app.route('/paises/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def paises(id=None):
    if request.method == 'GET':
        if id is not None:
            pais = Pais.query.get(id)
            if pais:
                return jsonify(pais.serialize()), 200
            else:
                return jsonify({"error":"Not found"}), 404
        else:
            paises = Pais.query.all()
            paises = list(map(lambda pais: pais.serialize(), paises))
            return jsonify(paises), 200

    if request.method == 'POST':

        if not request.json.get('nombre'):
            return jsonify({"nombre":"es requerido"}), 422

        data = request.get_json()
        pais = Pais.query.filter_by(name=data['nombre'].upper()).first()
        print(pais)
        if pais:
            return jsonify({"pais": data['nombre'].upper() + " ya existe"}), 200
        else:
            pais = Pais()
            pais.name = data['nombre'].upper() 
            db.session.add(pais)
            db.session.commit()
        
        return jsonify(pais.serialize()), 201

    if request.method == 'PUT':
        data = request.get_json()
        if not request.json.get('nombre'):
            return jsonify({"nombre":"es requerido"}), 422

        pais = Pais.query.get(id)

        if not pais:
            return jsonify({"error":"not found"}), 404
        else:
            pais = Pais.query.filter_by(name=data['nombre'].upper()).first()
            if pais:
                return jsonify({"pais": data['nombre'].upper() + " ya existe"}), 200
            else:
                pais = Pais.query.get(id)
                pais.name = data['nombre'].upper()
                db.session.commit()

                return jsonify(pais.serialize()), 201

    if request.method == 'DELETE':
        pais = Pais.query.get(id)
        if not pais:
            return jsonify({"error":"not found"}), 404
        else:
            db.session.delete(pais)
            db.session.commit()
            return jsonify({"message":"delete"}), 200
        
        
if __name__ =='__main__':
    manager.run()

