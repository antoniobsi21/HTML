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
regioes = ['BR', 'NA', 'EUNE', 'EUW', 'JP', 'KR', 'LAS', 'LAN', 'OCE', 'TR', 'RU', 'PBE']

@app.route('/')
def index():
	contexto = {'titulo': 'Página Inicial', 'regioes': regioes}
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
	try:
		error = None
		nome = request.args.get('invocador')
		regiao = request.args.get('regiao')
		
		invocador = Invocador(nome, regiao)
		dados = invocador.dados
		
		statusReq = invocador.req.status_code
		if statusReq == 200:
			nome = dados['name']
			nivel = dados['summonerLevel']
			contexto = {'titulo': 'invocador - {}'.format(nome), 'invocador': nome, 'nivel': nivel}
			return render_template('invocador.html', contexto=contexto)
		# elif statusReq == 403:
		# 	error = 'Chave provavelmente inválida, verifique a validade da mesma'
		# elif statusReq == 404:
		# 	error = 'Invocador não existe na região informada.'
		# redirect(url_for('index', error=error))

		return redirect(url_for('index'))
		# NÃO SEI
	except:
		return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(debug=True)