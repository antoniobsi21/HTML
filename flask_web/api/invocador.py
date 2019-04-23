import requests

myKey = 'não sei, tem que'
myKey= 'RGAPI-6c6426ef-273b-4d58-a486-189e9377fabf'
class Invocador:
	def __init__(self, nickname, regiao):
		self.nickname = nickname
		self.region = regiao.lower() + str(1) if regiao not in ['kr', 'ru'] else regiao
		self.req = requests.get('https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}'. \
		format(self.region, self.nickname, myKey))
		# if req.status_code == 404:
		# 	print("Invocador não encontrado.")
		# elif req.status_code == 403:
		# 	print("Chave inválida, por favor verifique a válidade de sua chave.")
		# elif req.status_code == 200:
		self.dados = self.req.json()

	def getSoloQueuePosition(self):
		elo = requests.get('https://br1.api.riotgames.com/lol/league/v4/positions/by-summoner/{}?api_key=RGAPI-a351e1cf-d618-489a-9545-df3d85cf521d'. \
			format(self.dados['id']))
		self.elo = elo.json()
		for x in self.elo:
			if x['queueType'].upper() == "RANKED_SOLO_5X5":
				print("\n{}: {} {} ({} PdL).\n".format(self.dados['name'], x['tier'], x['rank'], x['leaguePoints']))
				break
		return -1

	def checarPartidaAtiva(self):
		partidaAtiva = requests.get('https://{}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{}?api_key={}'. \
			format(self.region, self.dados['id'], myKey))
		if partidaAtiva.status_code == 200:
			partidaAtiva = partidaAtiva.json()
			print('(Em partida: encryptionKey: \'{}\', matchId: \'{}\', platformId: \'{}\'.)\n'. \
			format(partidaAtiva['observers']['encryptionKey'], partidaAtiva['gameId'], partidaAtiva['platformId']))

	def printAllQueuePositions(self):
		elo = requests.get('https://{}.api.riotgames.com/lol/league/v4/positions/by-summoner/{}?api_key={}'. \
		format(self.region, self.dados['id'], myKey))
		self.elo = elo.json()
		print("\n{:^20}\n".format(self.dados['name']))
		self.checarPartidaAtiva()
		for x in self.elo:
			if x['queueType'].upper() == "RANKED_SOLO_5X5":
				print("Solo:")
			if x['queueType'].upper() == "RANKED_FLEX_SR":
				print("Flex:")
			if x['queueType'].upper() == "RANKED_FLEX_3X3":
				print("3x3:")
			print("{}: {} {} ({} PdL).\n".format(x['leagueName'], x['tier'], x['rank'], x['leaguePoints']))
		return -1

