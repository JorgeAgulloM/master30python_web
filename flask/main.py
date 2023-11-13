from flask import Flask, redirect, url_for, render_template
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

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

if __name__=='__main__':
    app.run(debug=True)