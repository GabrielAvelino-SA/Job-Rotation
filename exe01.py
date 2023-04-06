# 1) Observe o trecho de código abaixo:
# int INDICE = 13, SOMA = 0, K = 0;
#  enquanto K < INDICE faça
# {
# K = K + 1;
# SOMA = SOMA + K;
# }
# imprimir(SOMA);

indice = 13
soma = 0
k = 0

while(k<indice):
    k += 1
    soma += k
print(soma)