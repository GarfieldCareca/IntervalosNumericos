#input  de quantas proposições deverão ser simuladas e criação da lista de letras
quan = int(input("Quantas proposições você deseja simular?"))
letras = []
i = 0

#laço para input das letras e armazenamento das proposições
while i < quan:
    letra = input("Insira as letras de suas proposições:")
    letras.append([letra])
    i += 1

print(letras)

'''

Primeira tentativa de montar a tabela, o erro de formação se dava pelo fato de quan ser um numero int que era adicionado
dentro de camadas = [], fazendo com que ela tivesse vários quan dentro ao invés de camadas definidas pelo valor de quan.


#matrizes das tabelas
camadas = []
linha = []

#fórmula de possibilidades de valores, 2^n
linhas = 2 ** quan

#criação das linhas
for i in range(linhas):
    camadas.append([])
    verdade = len(camadas)
    for j in range(quan):
        linha.append(0)
        camadas.append(linhas)

print(camadas)
print (verdade)
'''

#Definição da matriz de camadas e contador de linhas
camadas = []

possibilidades = 2 ** quan

#modelo da tabela verdade
for linhas in range(possibilidades):
    linha = []

    for colunas in range(quan):
        linha.append(0)

    camadas.append(linha)

print(camadas)
