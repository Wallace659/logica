palavra = str(input("Digite uma palavra: ")).lower()
contador = 0
for letra in palavra:
    if letra in "bcdfghjklmnpqrstvwxyz":
        contador += 1

print(f"A palavra {palavra} possui {contador} consoantes.")