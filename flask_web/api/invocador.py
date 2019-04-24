import requests

myKey= 'RGAPI-6c6426ef-273b-4d58-a486-189e9377fabf'
class Invocador:
	def __init__(self, nickname, regiao):
		self.nickname = nickname
		regiao = regiao.lower()
		self.region = regiao + str(1) if regiao not in ['kr', 'ru'] else regiao
		self.req = requests.get('https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}'. \
		format(self.region, self.nickname, myKey))
		self.dados = self.req.json()

	def getSoloQueueInformation(self):
		elo = requests.get('https://br1.api.riotgames.com/lol/league/v4/positions/by-summoner/{}?api_key=RGAPI-a351e1cf-d618-489a-9545-df3d85cf521d'. \
			format(self.dados['id']))
		self.elo = elo.json()
		for x in self.elo:
			if x['queueType'].upper() == "RANKED_SOLO_5X5":
				return x
		return -1

	def checarPartidaAtiva(self):
		partidaAtiva = requests.get('https://{}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{}?api_key={}'. \
			format(self.region, self.dados['id'], myKey))
		if partidaAtiva.status_code == 200:
			partidaAtiva = partidaAtiva.json()
			print('(Em partida: encryptionKey: \'{}\', matchId: \'{}\', platformId: \'{}\'.)\n'. \
			format(partidaAtiva['observers']['encryptionKey'], partidaAtiva['gameId'], partidaAtiva['platformId']))

	def getAllQueueInformation(self):
		elo = requests.get('https://{}.api.riotgames.com/lol/league/v4/positions/by-summoner/{}?api_key={}'. \
		format(self.region, self.dados['id'], myKey))
		positions = {}
		self.elo = elo.json()
		ordenedQueues = {}
		for x in sorted(self.elo):
			ordenedQueues[x] = self.elo[x]
		return ordenedQueues