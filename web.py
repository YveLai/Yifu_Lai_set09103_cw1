from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/main.html')
def main():	
	return render_template('main.html')

@app.route('/login.html')
def login():
	return render_template('login.html')

@app.route('/sign_up.html')
def sign_up():
	return render_template('sign_up.html')

@app.route('/cart.html')
def cart():
	return render_template('cart.html')

@app.route('/buy.html')
def buy():
	return render_template('buy.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True) 
