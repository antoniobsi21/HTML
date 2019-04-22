from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
regioes = ['BR', 'NA', 'EUNE', 'EUW', 'JP', 'KR', 'LAS', 'LAN', 'OCE', 'TR', 'RU', 'PBE']

@app.route('/')
def index():
	contexto = {'titulo': 'Página Inicial'}
	return render_template('index.html', contexto=contexto)

@app.route('/cadastro')
def cadastro():
	contexto = {'regioes': regioes, 'titulo': 'Cadastro'}
	return render_template('cadastro.html', contexto=contexto)

@app.route('/contato')
def contato():
	contexto = {'titulo': 'Contato'}
	return render_template('contato.html', contexto=contexto)

@app.route('/login')
def login():
	contexto = {'titulo': 'Login'}
	return render_template('login.html', contexto=contexto)

@app.route('/invocador', methods=['GET','POST'])
def invocador():
	if request.form.get("invocador"):
		nome = request.form["invocador"]
	else:
		nome = ""
		print("@@@@")
		print(request.form)
		# return redirect(url_for("index"))
	contexto = {'nome': nome, 'titulo': 'Invocador - {}'.format(nome)}
	return render_template('invocador.html', contexto=contexto)