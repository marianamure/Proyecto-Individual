from flask import render_template, redirect, session, request, flash
from flask_app import app

from flask_app.models.users import User


from flask_app.models.publicaciones import Publicacion

#Importación BCrypt
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrarme')
def registrarme():
    return render_template('registro.html')

@app.route('/registro', methods=['POST'])
def registro():
    #Validar la información ingresada
    if not User.valida_usuario(request.form):
        return redirect('/registrarme')

    pwd = bcrypt.generate_password_hash(request.form['password']) #Encriptamos el password del usuario

    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pwd
    }

    #request.form = FORMULARIO HTML
    id = User.save(formulario) #Recibo el identificador de mi nuevo usuario

    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def login():
    #Verificar que el email EXISTA
    #request.form RECIBIMOS DE HTML
    #request.form = {email: elena@cd.com, password: 123}
    user = User.get_by_email(request.form) #Recibiendo una instancia de usuario o Falso

    if not user:
        flash('E-mail no encontrado', 'login')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password incorrecto', 'login')
        return redirect('/')

    session['user_id'] = user.id

    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inicio sesión

    publicaciones = Publicacion.get_all(formulario) 

    return render_template('dashboard.html', user=user, publicaciones= publicaciones)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Usuario que inicio sesión

    publicaciones = Publicacion.get_all_muro() 

    return render_template('wall.html', user=user, publicaciones= publicaciones)