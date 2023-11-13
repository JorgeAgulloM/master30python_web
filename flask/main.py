from flask import Flask, flash, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask_de_mierda_de_victor_robles'

# Connection DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskweb'

mysql = MySQL(app)

# Context_processor
@app.context_processor
def date_now():
    return {'now': datetime.now()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info')
@app.route('/info/<string:name>')
@app.route('/info/<string:name>/<string:surname>')
def info(name:str=None, surname:str=None):

    if name is None and surname is None:
        text = ''
    elif surname is None:
        text = name
    else:
        text = f'{name} {surname}'

    return render_template('info.html', text=text)    


@app.route('/contact')
@app.route('/contact/<redirection>')
def contact(redirection = None):
    
    if redirection is not None:
        return redirect(url_for('languages'))
    
    return render_template('contact.html')

@app.route('/languages')
def languages():
    return render_template('languages.html')

root = '/car'

@app.route(f'{root}/create', methods=['GET', 'POST'])
def create_car():
    
    if request.method == 'POST':
        try:       

            brand=request.form['brand']
            model=request.form['model']
            price=request.form['price']
            city=request.form['city']

            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO cars VALUES(NULL, %s, %s, %s, %s)", (brand, model, price, city))
            cursor.connection.commit()
            
            flash('Has creado un nuevo coche')
            return redirect(url_for('index'))
        except Exception as e:
            print(f'Error: {e}')
            return redirect(url_for('index'))
        
    return render_template('create_car.html')
    
if __name__=='__main__':
    app.run(debug=True)