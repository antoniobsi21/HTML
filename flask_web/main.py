from flask import Flask, flash, render_template, request, redirect, url_for, request
from requests import get
from api.invocador import Invocador
#MAHOE

#Deve ser atualizada periodicamente em: 'https://developer.riotgames.com/' >> Login and so on.
#Talvez seja aplicável: keys = ['key1', 'key2']

# myKey = 'não sei, tem que ver'
# Se importar não sera necessário refazer ou criar código aqui, somente criar possíveis mais códigos na classe
# Invocador
app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha dificil de quebrar'
regioes = ['BR', 'NA', 'EUNE', 'EUW', 'JP', 'KR', 'LAS', 'LAN', 'OCE', 'TR', 'RU', 'PBE']
contexto = {"regioes": regioes, "selecionado": 'BR'}
print("-----")

@app.route('/')
def index():
	contexto['titulo'] = 'Página Inicial'
	return render_template('index.html', contexto=contexto)

@app.route('/cadastro')
def cadastro():
	contexto['titulo'] = 'Cadastro'
	return render_template('cadastro.html', contexto=contexto)

@app.route('/contato')
def contato():
	contexto['titulo'] = 'Contato'
	return render_template('contato.html', contexto=contexto)

@app.route('/login')
def login():
	contexto['titulo'] = 'Login'
	return render_template('login.html', contexto=contexto)

@app.route('/invocador', methods=['GET','POST'])
def invocador():
	try:
		error = None
		nome = request.args.get('invocador')
		regiao = request.args.get('regiao')
		
		invocador = Invocador(nome, regiao)
		dados = invocador.dados
		
		statusReq = invocador.req.status_code

		contexto['icone'] = str(dados['profileIconId'])
		contexto['selecionado'] = regiao

		print(contexto['icone'])
		print(invocador.req)
		print('\n\n{}'.format(dados))

		if statusReq == 200:
			nome = dados['name']
			nivel = dados['summonerLevel']
			contexto['titulo'] = 'Invocador - {}'.format(nome)
			contexto['dados'] = dados
			return render_template('invocador.html', contexto=contexto)
		elif statusReq == 403:
			error = 'Chave provavelmente inválida, verifique a validade da mesma'
		elif statusReq == 404:
			error = 'Invocador não encontrado na região informada.'
		elif statusReq == 400:
			error = 'Possíveis caracteres inválidos. (Bad request 400)'
		redirect(url_for('index', error=error))
		flash(error)
		return redirect(url_for('index'))
	except Exception as e:
		print("\n\n")
		print(e)
		print("\n\n")
		flash("Erro desconhecido!")
		return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)