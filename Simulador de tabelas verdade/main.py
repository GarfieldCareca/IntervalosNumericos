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
print("Considere 0 como Falso e 1 como Verdadeiro")


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

    for colunas in range(possibilidades):
        if possibilidades == 4:
            for verdadeiros in range(2):
                linha[colunas][0] = "V"
            falsos = verdadeiros / 2
            for falsos in range(3, 4, 1):
                linha[colunas][2] = "F"

    camadas.append(linha)

print(camadas)
''' 
#2 Tentativa de preenchimento da tabela (não funcionou) 

verdades = 0
falsas = 1
periodos = possibilidades / 2

#Preenchimento da primeira coluna 
i = 0
if quan == 2:
   for valores in range(len(camadas)):
       linhas[valores][0] = verdades

#Tentativa de preenchimento da tabela (não funcionou dessa forma)   
    while i <= len(camadas):
        linha[i][0] = verdades
        i += 1
    j = i * 2
    while j >= i:
        linha[j][2] = falsas
        j -= 1
'''