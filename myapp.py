from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template( "index1.html")

@app.route('/whereami')
def whereami():
	return "Kdua"

@app.route('/hello/<name>')
def foo(name):
	return render_template('index1.html', to=name)

if __name__ == '__main__':
        app.run(host="0.0.0.0")

#@app.router('/WEEK1/>')
def Week1():
#        return render_template( "index.html")
#if __WEEK1__ =='__WEEK1__')

@app.route('/')
def index():
        return render_template( "index1.html")


