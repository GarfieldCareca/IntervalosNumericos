quan = int(input("Quantas proposições você deseja simular?"))
letras = []
i = 0

while i < quan:
    prop = input("Insira as letras de suas proposições:")
    letras.append([prop])
    i += 1

print(letras)

tam = (len(letras) - 1)

if tam <= 2:
    print(letras[0], "|", letras[0])
    print("  V   |   v  ")





