nome = str(input("digite uma palavra: ")).lower()
tem_a_letra_a = False
quantidade = 0


for letra in nome:
    if letra == "a":
        tem_a_letra_a = True
        quantidade = quantidade + 1

if tem_a_letra_a == True:
    print(f"Sua palavra possui {quantidade} letras A")
else:
    print("Sua palavra não possui a letra A")