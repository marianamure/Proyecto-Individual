from flask import render_template, redirect, session, request, flash
from flask_app import app


from flask_app.models.users import User
from flask_app.models.publicaciones import Publicacion
from werkzeug.utils import secure_filename
import os

@app.route('/new_datos')
def datos():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inicio sesión

    return render_template('datos.html', user=user)

@app.route('/create/datos', methods=['POST'])
def create_datos():
    if 'user_id' not in session: 
        return redirect('/')

    if not Publicacion.valida_publicacion(request.form):  
        return redirect('/new_datos')

    if 'imagen' not in request.files:
        flash('Imagen no encontrada', 'publicacion')
        return redirect('/new_datos')

    imagen = request.files['imagen']

    if imagen.filename == "":
        flash ('Nombre de imagen vacía', 'publicacion')
        return redirect ('/new_datos')   

    nombre_imagen = secure_filename(imagen.filename) 
    imagen.save(os.path.join(app.config ['UPLOAD_FOLDER'],nombre_imagen)) 
    
    formulario = {
        'finca' : request.form['finca'],
        'municipio' : request.form['municipio'],
        'nombre_fertilizante' : request.form['nombre_fertilizante'],
        'cantidad_fertilizante' : request.form['cantidad_fertilizante'],
        'fecha_cosecha' : request.form['fecha_cosecha'],
        'enfermedades' : request.form['enfermedades'],
        'produccion' : request.form['produccion'],
        'descripcion' : request.form['descripcion'],
        'user_id' : request.form['user_id'],
        'imagen' : nombre_imagen
    }
    Publicacion.save(formulario)

    return redirect('/dashboard')

@app.route('/editar/publicacion/<int:id>') 
def editar_publicacion(id):
    if 'user_id' not in session: 
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) 

    
    formulario_publicacion = {"id": id}
    publicacion = Publicacion.get_by_id(formulario_publicacion)

    return render_template('editadatos.html', user=user, publicacion=publicacion)

@app.route('/update/publicacion', methods=['POST'])
def update_publicacion():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    
    if not Publicacion.valida_publicacion(request.form): #llama a la función de valida_receta enviándole el formulario, comprueba que sea valido 
        return redirect('/editar/publicacion/'+request.form['id'])

    nombre_imagen = ''
    
    if 'imagen' in request.files:
        imagen = request.files['imagen']

        if imagen.filename != "":
            nombre_imagen = secure_filename(imagen.filename)    
            imagen.save(os.path.join(app.config ['UPLOAD_FOLDER'],nombre_imagen)) 

    formulario = {
        'finca' : request.form['finca'], 
        'municipio' : request.form['municipio'],
        'nombre_fertilizante' : request.form['nombre_fertilizante'],
        'cantidad_fertilizante' : request.form['cantidad_fertilizante'],
        'fecha_cosecha' : request.form['fecha_cosecha'],
        'enfermedades' : request.form['enfermedades'],
        'produccion' : request.form['produccion'],
        'descripcion' : request.form['descripcion'],
        'user_id' : request.form['user_id'],
        'imagen' : nombre_imagen,
        'id': request.form['id']
    }

    Publicacion.update(formulario)
    return redirect('/dashboard')


@app.route('/eliminar/publicacion/<int:id>') #En mi URL voy a obtener ID
def eliminar_publicacion(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    print("eliminando")
    formulario = {"id": id}
    Publicacion.eliminar(formulario)
    
    return redirect('/dashboard')

@app.route('/view/publicacion/<int:id>') #A través de la URL recibimos el ID de la receta
def show_publicacion(id):
    if 'user_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inicio sesión

    formulario_publicacion={
        'id':id
    }

    publicaciones = Publicacion.get_by_id(formulario_publicacion) 


    return render_template('show_publicacion.html', user=user, publicaciones= publicaciones)
