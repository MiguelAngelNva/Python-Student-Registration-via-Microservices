from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
import logging

#pip install --upgrade pymongo dnspython


# Configuración de conexión a MongoDB Atlas
MONGO_URI = "mongodb+srv://mnava:12345@cluster0.bwpf0wx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # reemplace aca la cadena de conexion obetenida en mongodb atlas
client = MongoClient(MONGO_URI)
db = client["customer_feedback"]  # Nombre de la base de datos
collection = db["students"]       # Nombre de la colección

# Inicialización de Flask
app = Flask(__name__)
CORS(app) 


# Ruta para crear un estudiante
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    student = {
        "nombre": data.get("nombre"),
        "apellido": data.get("apellido"),
        "programa_academico": data.get("programa_academico"),
        "edad": data.get("edad")
    }
    result = collection.insert_one(student)
    return jsonify({"message": "Estudiante creado", "id": str(result.inserted_id)}), 201

# Ruta para leer todos los estudiatnes
@app.route('/students', methods=['GET'])
def read_student():
    students = collection.find()
    student_list = [{"id": str(student["_id"]), "nombre": student["nombre"], "apellido": student["apellido"], "programa_academico": student["programa_academico"], "edad": student["edad"]} for student in students]
    return jsonify(student_list), 200


# Inicialización de Flask
#app = Flask(__name__)
#CORS(app)  

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
  

