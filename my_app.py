from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template( "index.html")

@app.route('/whereami')
def whereami():
	return "Kdua"

@app.route('/hello/<name>')
def foo(name):
    return render_template('index.html', to=name)

