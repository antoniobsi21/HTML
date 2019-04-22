from flask import Flask, render_template

app = Flask(__name__)
regioes = ['BR', 'NA', 'EUNE', 'EUW', 'JP', 'KR', 'LAS', 'LAN', 'OCE', 'TR', 'RU', 'PBE']

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/cadastro')
def cadastro():
	contexto = {'regioes': regioes}
	return render_template('cadastro.html', contexto=contexto)

@app.route('/contato')
def contato():
	return render_template('contato.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/invocador/<nome>')
def invocador(nome):
	return render_template('invocador.html', nome=nome)