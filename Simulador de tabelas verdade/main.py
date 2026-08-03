#Input de operador e quantidade de proposições
letras = []
quant = int(input("Insira quantas proposições você quer simular? digite 0 para sair.\n:"))
i = 0
while i < quant:
    letraProp =input("Insira a letra da proposição (Em maiúsculo)")
    letras.append(letraProp)

    i += 1

        

op = int(input("Digite 1 para conjunção, 2 para disjunção, 3 para condicional e 4 para bicondicional \n :"))
tam = (len(letras) - 1)


for i in range(tam):
    for posi in range(tam):
        if op == 1:
            print(letras[posi], "|", (letras[posi] + i))


