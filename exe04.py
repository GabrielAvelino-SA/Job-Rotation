import json
total = 0
with open("data.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

for i in dados:
    total += i['valores']
for i in dados:
    print (f"{i['estados']} : {((i['valores']/total)*100):,.2f}%")
