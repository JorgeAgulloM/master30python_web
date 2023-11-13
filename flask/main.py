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
            mysql.connection.commit()
            cursor.close()
            
            flash('Has creado un nuevo coche')
            return redirect(url_for('index'))
        except Exception as e:
            print(f'Error: {e}')
            return redirect(url_for('index'))
        
    return render_template('create_car.html')

@app.route(f'{root}/cars')
def cars():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()
    cursor.close()
    
    return render_template('cars.html', cars=cars)

@app.route(f'{root}/car/<car_id>')
def car(car_id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM cars WHERE id = %s', (car_id))
    car = cursor.fetchone()
    cursor.close()
    
    return render_template('car.html', car=car)

@app.route(f'{root}/delete/<car_id>')
def delete(car_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM cars WHERE id = %s', (car_id))
    mysql.connection.commit()
    cursor.close()
    
    flash('Coche eliminado')
    return redirect(url_for('cars'))
    
if __name__=='__main__':
    app.run(debug=True)