from flask_app.config.mysqlconnection import  connectToMySQL
from flask import flash

class Comentario:

    def __init__(self, data):
        #data = {id: 1, content: "Hola", creat.., up.., rec_id.., send_id.., receiver_name: "Pedro", sender_name:"Barack"}
        self.id = data['id']
        self.user_id = data['user_id']
        self.publicacion_id = data['publicacion_id']
        self.contenido = data['contenido']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO `agro`.`comentarios` (`contenido`,`user_id`, `publicacion_id` ) VALUES (%(contenido)s, %(user_id)s, %(publicacion_id)s)"
        result = connectToMySQL('agro').query_db(query, formulario)
        return result

    @classmethod
    def get_user_comentarios(cls, formulario):
        #formulario = {id: 1}
        #2 LEFT JOINS
        query = "SELECT comentarios.contenido, users.first_name AS sender from users LEFT JOIN comentarios on comentarios.user_id = users.id  LEFT JOIN publicaciones ON publicaciones.id = comentarios.publicacion_id"
        results = connectToMySQL('agro').query_db(query, formulario) #Lista de diccionarios
        comentarios = []
        for comentario in results:
            #message = {id: 1, content: "Hola", creat.., up.., rec_id.., send_id.., receiver_name: "Pedro", sender_name:"Barack"}
            comentarios.append(cls(comentario)) #1.- cls(message) me crea instancia de mensaje. 2.- Agregamos la instancia a la lista de mensajes

        return comentarios

    @classmethod
    def eliminar(cls, formulario):
        #formulario = {id: 1}
        query = "DELETE FROM comentarios WHERE id = %(id)s"
        result = connectToMySQL('agro').query_db(query, formulario)
        return result