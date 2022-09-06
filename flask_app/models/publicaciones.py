from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

class Publicacion:

    def __init__(self, data):
        #data = {id: 1, content: "Hola", creat.., up.., rec_id.., send_id.., receiver_name: "Pedro", sender_name:"Barack"}
        self.id = data['id']
        self.finca = data['finca']
        self.municipio = data['municipio']
        self.nombre_fertilizante = data['nombre_fertilizante']
        self.cantidad_fertilizante = data['cantidad_fertilizante']
        self.fecha_cosecha = data['fecha_cosecha']
        self.enfermedades = data['enfermedades']
        self.produccion = data['produccion']
        self.descripcion = data ['descripcion']
        self.imagen = data ['imagen']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        if "first_name" in data:
            self.first_name = data['first_name']

# Falta la descripcion y la imagen, tampoco se han agregado al erd 
# Ojo, se debe hacer left join  con         #LEFT JOIN    self.first_name = data['first_name']    ?   

    @staticmethod
    def valida_publicacion(formulario):
        es_valido = True

        if formulario['finca'] == "":
            flash('El campo debe tener informacion', 'publicacion')
            es_valido = False
        
        if formulario['municipio'] == "":
            flash('El campo debe tener informacion', 'publicacion')
            es_valido = False

        if formulario['nombre_fertilizante'] == "":
            flash('El campo debe tener informacion', 'publicacion')
            es_valido = False

        if formulario['cantidad_fertilizante'] == "":
            flash('El campo debe tener informacion', 'publicacion')
            es_valido = False

        if formulario['fecha_cosecha'] == "":
            flash('El campo debe tener informacion', 'publicacion')
            es_valido = False

        if formulario['enfermedades'] == "":
            flash('El campo debe tener informacion', 'publicacion')
            es_valido = False

        if formulario['produccion'] == "":
            flash('El campo debe tener informacion', 'publicacion')
            es_valido = False
        
        return es_valido

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO publicaciones (finca, municipio, nombre_fertilizante, cantidad_fertilizante, fecha_cosecha, enfermedades, produccion, descripcion, imagen, user_id) VALUES (%(finca)s, %(municipio)s, %(nombre_fertilizante)s,%(cantidad_fertilizante)s, %(fecha_cosecha)s, %(enfermedades)s, %(produccion)s, %(descripcion)s, %(imagen)s, %(user_id)s)"
        result = connectToMySQL('agro').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls,formulario):
        query = "SELECT publicaciones.*, finca FROM publicaciones LEFT JOIN users ON users.id = publicaciones.user_id WHERE users.id=%(id)s;"
        results = connectToMySQL('agro').query_db(query,formulario) 
        publicaciones = []
        for publicacion in results:
            
            publicaciones.append(cls(publicacion)) 

        return publicaciones

    @classmethod
    def get_by_id(cls, formulario): #formulario = {id: 1}
        query = "SELECT publicaciones.*, first_name FROM publicaciones LEFT JOIN users ON users.id = publicaciones.user_id WHERE publicaciones.id = %(id)s"
        result = connectToMySQL('agro').query_db(query, formulario) #Lista de diccionarios
        publicacion = cls(result[0])
        return publicacion

    @classmethod
    def update(cls, formulario):
        if(formulario['imagen'] != ''):
            query = "UPDATE publicaciones SET finca=%(finca)s, municipio=%(municipio)s, nombre_fertilizante=%(nombre_fertilizante)s, cantidad_fertilizante=%(cantidad_fertilizante)s, fecha_cosecha=%(fecha_cosecha)s, enfermedades=%(enfermedades)s, produccion=%(produccion)s, descripcion=%(descripcion)s, imagen=%(imagen)s WHERE id = %(id)s"
        else:
            query = "UPDATE publicaciones SET finca=%(finca)s, municipio=%(municipio)s, nombre_fertilizante=%(nombre_fertilizante)s, cantidad_fertilizante=%(cantidad_fertilizante)s, fecha_cosecha=%(fecha_cosecha)s, enfermedades=%(enfermedades)s, produccion=%(produccion)s, descripcion=%(descripcion)s WHERE id = %(id)s"
        result = connectToMySQL('agro').query_db(query, formulario)
        return result

    @classmethod
    def eliminar(cls, formulario):
        query = "DELETE FROM publicaciones WHERE id = %(id)s"
        result = connectToMySQL('agro').query_db(query, formulario)
        return result

    @classmethod
    def get_all_muro(cls):
        query = "SELECT publicaciones.*, users.first_name FROM publicaciones LEFT JOIN users ON users.id = publicaciones.user_id;"
        results = connectToMySQL('agro').query_db(query) 
        publicaciones = []
        for publicacion in results:
            
            publicaciones.append(cls(publicacion)) 

        return publicaciones