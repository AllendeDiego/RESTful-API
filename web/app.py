from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from models import *
import bcrypt
from Funciones import *

app = Flask(__name__)
api = Api(app)


class Register(Resource):
    def post(self):
        #Se obtiene la información otorgada por la app solicitante
        postedData = request.get_json()
        #Se obtiene el usuario, contraseña del JSON
        username = postedData["username"]
        password = postedData["password"]
        #Se consulta si usuario existe en db Users
        if UsuarioExiste(username):
            #Se crea el JSON para devolver la solicitud rechaza
            retJson = {
                "status":301,
                "msg": "Usuario ya existe"
            }
            #Se retorna el JSON a la app solicitante
            return jsonify(retJson)
        #Se encripta la contraseña escrita por el usuario
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        #Se guarda la información en la base de datos Users
        users.insert({
            "Username":username,
            "Password":hashed_pw,
            "Connected":0
        })
        #Se crea el JSON para devolver a la solicitud exitosa
        retJson = {
            "status":200,
            "msg": "Registrado correctamente"
        }
        #Se retorna el JSON a la app solicitante
        return jsonify(retJson)


class Logout(Resource):
    def post(self):
        postedData = request.get_json()
        #Se obtiene el usuario del JSON
        username = postedData["username"]
        #Se actualiza el estado de conexion del usuario
        users.update({
            "Username":username
        }, {
            "$set":{
                "Connected":0
                }
        })
        #Se crea el JSON para devolver a la solicitud exitosa
        retJson = {
            "status":200,
            "msg":"Desconectado con éxito"
        }
        #Se retorna el JSON a la app solicitante
        return jsonify(retJson)

class Login(Resource):
    def get(self):
        #Se obtiene la información otorgada por el usuario
        postedData = request.get_json()
        #Se obtiene el usuario y contraseña del JSON
        username = postedData["username"]
        password = postedData["password"]
        #función para verificar contraseña
        correct_pw = verifyPw(username, password)
        #Se revisa si la contraseña es correcta
        if not correct_pw:
            #Se crea el JSON para devolver solicitud rechazada
            retJson = {
            "status":302,
            "msg":"Usuario y/o Contraseña incorrecta"
            }
            #Se envia JSON
            return jsonify(retJson)
        else:
            #Cambiar a conectado
            users.update({
                "Username":username
            }, {
                "$set":{
                    "Connected":1
                    }
            })
        #Se crea el JSON para devolver a la solicitud exitosa
        retJson = {
            "status":200
        }
        #Se retorna el JSON a la app solicitante
        return jsonify(retJson)

class Create_client(Resource):
    def post(self):
        #Se obtiene la información otorgada por la app solicitante
        postedData = request.get_json()
        #Se obtiene info del JSON
        rut = postedData["rut"]
        nombre = postedData["nombre"]
        email = postedData["email"]
        telefono = postedData["telefono"]
        tipo_cliente = postedData["tipo_cliente"]
        vinternet = postedData["vinternet"]
        varriendo = postedData["varriendo"]
        vstecnico = postedData["vstecnico"]
        vventas = postedData["vventas"]
        descuentos = postedData["descuentos"]
        notas = postedData["notas"]
        giro = postedData["giro"]
        contacto = postedData["contacto"]
        direccion_fisica = postedData["direccion_fisica"]
        tipo_documento = postedData["tipo_documento"]
        tipo_plan = postedData["tipo_plan"]
        precio_plan = postedData["precio_plan"]
        precio_instalacion = postedData["precio_instalacion"]
        fecha_instalacion = postedData["fecha_instalacion"]
        fecha_desintalacion = postedData["fecha_desintalacion"]
        #Se inserta info en db Clients
        clients.insert({
            "Rut":rut,
            "Nombre":nombre,
            "Email":email,
            "Telefono":telefono,
            "Tipo_cliente":tipo_cliente,
            "Vinternet":vinternet,
            "Varriendo":varriendo,
            "Vstecnico":vstecnico,
            "Vventas":vventas,
            "Tipo_documento":tipo_documento,
            "Tipo_plan":tipo_plan,
            "Precio_plan":precio_plan,
            "Precio_instalacion":precio_instalacion,
            "Descuentos":descuentos,
            "Notas":notas,
            "Giro":giro,
            "Contacto":contacto,
            "Direccion_fisica":direccion_fisica,
            "Fecha_instalacion":fecha_instalacion,
            "Fecha_desintalacion":fecha_desintalacion
        })
        #Se crea el JSON para devolver a la solicitud exitosa
        retJson = {
            "status":200,
            "msg": "Registrado correctamente"
        }
        #Se retorna el JSON a la app solicitante
        return jsonify(retJson)

class Guardar_Boleta(Resource):
    def post(self):
        #Se obtiene la información otorgada por la app solicitante
        postedData = request.get_json()
        #Se obtiene info del JSON
        tipo_servicio = postedData["tipo_servicio"]
        numero_boleta = postedData["numero_boleta"]
        fecha = postedData["fecha"]
        monto = postedData["monto"]
        #Se inserta info en db Factura
        factura.insert({
            "Tipo_servicio":tipo_servicio,
            "Numero_boleta":numero_boleta,
            "Fecha":fecha,
            "Monto":monto
        })
        #Se crea el JSON para devolver a la solicitud exitosa
        retJson = {
            "status":200,
            "msg": "Registrado correctamente"
        }
        #Se retorna el JSON a la app solicitante
        return jsonify(retJson)

class Generar_Boleta(Resource):
    def get(self):
        #Se obtiene la información otorgada por el usuario
        postedData = request.get_json()
        #Se obtiene el usuario y contraseña del JSON
        rut = postedData["rut"]
        #Se comprueba si el cliente existe
        if not ClienteExiste(rut):
            #Se crea el JSON para devolver a la solicitud negada
            retJson = {
                "status":301,
                "msg": "Cliente no existe"
            }
            #Se retorna el JSON a la app solicitante
            return jsonify(retJson)
        #Se solicitan los datos del Cliente
        Datos = DatosBoleta(rut)
        #Se obtienen datos del JSON
        nombre = Datos["Nombre"]
        email = Datos["Email"]
        telefono = Datos["Telefono"]
        tipo_cliente = Datos["Tipo_cliente"]
        vinternet = Datos["Vinternet"]
        varriendo = Datos["Varriendo"]
        vstecnico = Datos["Vstecnico"]
        vventas = Datos["Vventas"]
        descuentos = Datos["Descuentos"]
        precio_plan = Datos["Precio_plan"]
        precio_instalacion = Datos["Precio_instalacion"]
        fecha_instalacion = Datos["Fecha_instalacion"]
        fecha_desintalacion = Datos["Fecha_desintalacion"]
        #Se crea el JSON para devolver a la solicitud exitosa
        retJson = {
            "status":200,
            "nombre":nombre,
            "email":email,
            "telefono":telefono,
            "tipo_cliente":tipo_cliente,
            "vinternet":vinternet,
            "varriendo":varriendo,
            "vstecnico":vstecnico,
            "vventas":vventas,
            "descuentos":descuentos,
            "precio_plan":precio_plan,
            "precio_instalacion":precio_instalacion,
            "fecha_instalacion":fecha_instalacion,
            "fecha_desintalacion":fecha_desintalacion
        }
        #Se retorna el JSON a la app solicitante
        return jsonify(retJson)




api.add_resource(Generar_Boleta, '/generar_boleta')
api.add_resource(Guardar_Boleta, '/guardar_boleta')
api.add_resource(Create_client, '/create_client')
api.add_resource(Register, '/register')
api.add_resource(Logout, '/logout')
api.add_resource(Login, '/login')


if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')
