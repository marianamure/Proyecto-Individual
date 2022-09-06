from flask import render_template, redirect, session, request, flash
from flask_app import app


from flask_app.models.users import User
from flask_app.models.publicaciones import Publicacion
from flask_app.models.comentarios import Comentario

@app.route('/send_comentario', methods=['POST'])
def send_comentario():
    if 'user_id' not in session:
        return redirect('/')
    
    #Guardar el mensaje. request.form = Diccionario con todos los campos del formulario
    Comentario.save(request.form)
    return redirect('/view/publicacion/'+request.form["publicacion_id"])

"""@app.route('/post_comentario')
def post_comentario():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    publicacion = Publicacion.get_by_id(formulario) #Usuario que inicio sesión

    comentarios = Comentario.get_user_comentarios(formulario) 

    return render_template('show_publicacion.html', publicacion=publicacion, comentarios= comentarios)"""

@app.route('/eliminar/comentario/<int:id>') #En mi URL voy a obtener ID
def eliminar_mensaje(id):
    formulario = {"id": id}
    Comentario.eliminar(formulario)
    return redirect('/show_publicacion')