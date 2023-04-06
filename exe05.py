text = str(input("Digite a String: "))
tamanho = len (text)
text_invert = []

for celula in text:
    contador = 0
    text_invert.insert(tamanho*(-1),celula)
    contador+=1

print(''.join(text_invert))