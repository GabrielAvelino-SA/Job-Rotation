import json

acumulador = []

class JSON_FILE():
    def __init__(self,json_array):
        self.menor = 0
        self.maior = 0
        self.totalMes = 0
        self.media = 0

        for i  in json_array:
            if (i['valor'] >= self.maior):
                self.maior = i['valor']
            if (i['valor'] <= self.menor):
                self.menor = i['valor']
            self.totalMes += i['valor']
        self.media = self.totalMes/len(json_array)
    def getMenor(self):
        return self.menor
    def getMaior(self):
        return self.maior
    def getTotalMes(self):
        return self.totalMes
    def getMedia(self):
        return self.media

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

faturameto = JSON_FILE(dados)

for i in dados:

    if i['valor'] >= faturameto.getMedia():
        acumulador.insert(len(acumulador),i['dia'])

print(f"Media: {faturameto.getMedia()}, Dias acima da media: {acumulador}")
print(f"Maior faturamento do Mês: {faturameto.getMaior()}")
print(f"Menor faturamento do Mês: {faturameto.getMenor()}")
