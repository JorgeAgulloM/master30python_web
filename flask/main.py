from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World with Flask | Jorge Agulló </h1>'

@app.route('/info')
@app.route('/info/<string:name>')
@app.route('/info/<string:name>/<string:surname>')
def info(name:str=None, surname:str=None):

    if not name or not surname:
        return '<h1> Welcome </h1>' 
    if not surname:
        return f'<h1> Welcome, {name}</h1>'
    
    return f'<h1> Welcome, {name} {surname}</h1>'

@app.route('/contact')
@app.route('/contact/<redirection>')
def contact(redirection = None):
    
    if redirection is not None:
        return redirect(url_for('languages'))
    
    return '<h1> Contact page with Jorge Agulló </h1>'

@app.route('/programing_laguages')
def languages():
    return '<h1> Languagues Page </h1>'

if __name__=='__main__':
    app.run(debug=True)