import requests

# URL donde esta almacenada la API, se debe modificar
url = "http://localhost:5000/"

def login(username,password):
    # Json que se envia en la solicitud de login
    payload = {"username":username, "password":password}
    # Se realiza la solicitud a la API
    r = requests.get(url+"login", json=payload)
    # Se obtiene la respuesta en formato JSON
    r_d = r.json()
    #Se evalua respuesta
    if r_d["status"] == 200:
        return True
    else:
        return False

def registro(username,password):
    # Json que se envia en la solicitud de registro
    payload = {"username":username, "password":password}
    # Se realiza la solicitud a la API
    r = requests.post(url+"register", json=payload)
    # Se obtiene la respuesta en formato JSON
    r_d = r.json()
    #Se evalua respuesta
    if r_d["status"] == 200:
        return True
    else:
        return False

def logout(username):
    # Json que se envia en la solicitud de logout
    payload = {"username":username}
    # Se realiza la solicitud a la API
    r = requests.post(url+"logout", json=payload)
    # Se obtiene la respuesta en formato JSON
    r_d = r.json()
    #Se evalua respuesta
    if r_d["status"] == 200:
        return True
    else:
        return False

def crear_cliente(rut,nombre,email,telefono,tipo_cliente,vinternet,varriendo,vstecnico,vventas,descuento,notas,giro,contacto,direccion_fisica,tipo_documento,tipo_plan,precio_plan,precio_instalacion,fecha_instalacion,fecha_desintalacion):
    # Json que se envia en la solicitud de crear cliente
    payload ={
                "rut":rut,
                "nombre":nombre,
                "email":email,
                "telefono":telefono,
                "tipo_cliente":tipo_cliente,
                "vinternet":vinternet,
                "varriendo":varriendo,
                "vstecnico":vstecnico,
                "vventas":vventas,
                "tipo_documento":tipo_documento,
                "tipo_plan":tipo_plan,
                "precio_plan":precio_plan,
                "precio_instalacion":precio_instalacion,
                "descuentos":descuentos,
                "notas":notas,
                "giro":giro,
                "contacto":contacto,
                "direccion_fisica":direccion_fisica,
                "fecha_instalacion":fecha_instalacion,
                "fecha_desintalacion":fecha_desintalacion
            }
    r = requests.post(url+"create_client", json=payload)
    # Se obtiene la respuesta en formato JSON
    r_d = r.json()
    #Se evalua respuesta
    if r_d["status"] == 200:
        return True
    else:
        return False

def guardar_boleta(tipo_servicio,numero_boleta,fecha,monto):
    # Json que se envia en la solicitud de guardar boleta generada
    payload={
            "tipo_servicio":tipo_servicio,
            "numero_boleta":numero_boleta,
            "fecha":fecha,
            "monto":monto
            }
    r = requests.post(url+"guardar_boleta", json=payload)
    # Se obtiene la respuesta en formato JSON
    r_d = r.json()
    #Se evalua respuesta
    if r_d["status"] == 200:
        return True
    else:
        return False


def generar_boleta(rut):
        # Json que se envia en la solicitud de  generar boleta
        payload={
                "rut":rut
                }
        r = requests.get(url+"generar_boleta", json=payload)
        # Se obtiene la respuesta en formato JSON
        r_d = r.json()
        #Se evalua respuesta
        if r_d["status"] == 200:
            return print(r_d)
        else:
            return False
