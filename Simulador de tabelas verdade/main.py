# Código corrigido e funcional
quantas = int(input("Quantas proposições você deseja simular? "))
letras = []
for i in range(quantas):
    letra = input(f"Digite a {i+1}ª variável (ex: A, B, C): ").strip()
    letras.append(letra)

print("\nConsidere 0 como Falso e 1 como Verdadeiro\n")

# Total de combinações possíveis
totalCombinacoes = 2 ** quantas
tabela = []


'''A genialidade do código a seguir se dá da seguinte forma, cada número em decimal
pode ser representado por bits de binário e cada posição de um dígito em binário possui
uma posição, como se fosse uma lista. O >> é como se fosse um empurrão dos dígitos uma
posição à frente, e acrescentando um 0 nas antigas posições de cada dígito. O & (AND)
compara as posições dos bits com o número 1 que atua como um filtro, isso porque o 1 em 
binário é 001, e as primeiras posições são 0 o que torna o 001 um filtro perfeito para
eliminar os primeiros bits de um número a ser comparado com o 1 em binário.'''

# Preenche cada linha da tabela usando contagem binária
for i in range(totalCombinacoes):
    linha = []  #Cria uma matriz para cada valor de i
    #Percorre os bits do número 'i' do mais significativo para o menos significativo
    for j in range(quantas - 1, -1, -1):
        bit = (i >> j) & 1  #Empurra os bits de i pra prosição j e depois compara isso com 001
        linha.append(bit) #Depois da comparação os únicos valores para bit serão 0 e 1
    tabela.append(linha)    #Adiciona cada linha com um bit na tabela

print(tabela)

#Início da feature de simulação de expressões
expressoes = input("Deseja fazer uma simulação de expressões numéricas? \n Digite S para sim e N para não")


