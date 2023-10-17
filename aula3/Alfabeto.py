# faça um programa que print na tela todas as letras do alfabeto com excessão das vogais

alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto:
    if letra in "bcdfghjklmnpqrstvwxyz":
        print(letra)


#exemplo 2

alfabeto = "abcdefghijklmnopqrstuvwxyz"
vogais = "aeiou"

for letra in alfabeto:
    if letra not in "aeiou":
        print(letra)

for letra in alfabeto:
    if letra in "bcdfghjklmnpqrstvwxyz":
        print(letra)