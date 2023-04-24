

from flask import Flask, render_template, url_for, request


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'dev'
)


@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')
    

@app.add_template_global  
def repeat(s, n):        
    return s * n



from datetime import datetime

# crear rutas
@app.route('/')
def index():
    print(url_for('index'))
    print(url_for('hello'))
    name = 'Erika'
    tecnicas = ['Plásticas', 'Ilustración', 'Obras Retórica', 'Obras Escultóricas']
    date = datetime.now()
    return render_template('index.html', 
        name = name, 
        tecnicas = tecnicas, 
        date = date,    
    )


@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
@app.route('/hello/<name>/<int:age>/<email>')
def hello(name = None, age = None, email = None):
    
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data = my_data)



# Crear formulario wtform
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario:', validators= [DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password: ', validators= [DataRequired(), Length(min=6, max=40)])
    submit = SubmitField('Registrar: ')



# crear vista y ruta para Registrar usuario
@app.route('/auth/register', methods = ['GET', 'POST'])

def register():
    #print(request.form) # muestra datos de ingreso en la terminal
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"Nombre de usuario: {username}, Contraseña: {password}"

  
    return render_template('auth/register.html', form = form)
