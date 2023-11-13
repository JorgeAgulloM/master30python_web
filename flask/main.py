from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World with Flask | Jorge Agulló </h1>'

@app.route('/info')
def info():
    return '<h1> Info Page </h1>'

@app.route('/contact')
def contact():
    return '<h1> Contact page with Jorge Agulló </h1>'

@app.route('/programing_laguages')
def languages():
    return '<h1> Languagues Page </h1>'

if __name__=='__main__':
    app.run(debug=True)