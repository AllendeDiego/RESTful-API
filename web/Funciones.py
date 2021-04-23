from models import *
import bcrypt

def verifyPw(username, password):
    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def verifyConnected(username):
    #Busca el usuario y luego entrega una lista, pero como solo hay 1
    #usuario con ese nombre, se selecciona el primer usuario [0] y
    # se lee si el usuario esta conectado
    connected = users.find({
        "Username":username
    })[0]["Connected"]

    if connected == 0:
        return False
    else:
        return True

def DatosBoleta(rut):
    #Busca los fatos del cliente en la db Clients
    Datos = clients.find({"Rut":rut})[0]
    #Returna todos los datos del cliente
    return Datos

def ClienteExiste(rut):
    #Busca en la db Clients si el rut del cliente ya existe
    Cliente = clients.find({"Rut":rut}).count()
    if Cliente == 0:
        return False
    else:
        return True

def UsuarioExiste(username):
    #Busca en la db Users si el rut del usuario ya existe
    Usuario = users.find({"Username":username}).count()
    if Usuario == 0:
        return False
    else:
        return True
