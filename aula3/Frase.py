# faça um programa que pede para o usuario digitar uma frase, percorra essa frase e mostra na tela um print para cada vez que encontrar um numero dentro dessa frase.

frase = str(input("Digite uma frase: ")).lower()

for caracter in frase:
    if caracter in "0123456789":
        print(caracter)


# exemplo 2

frase = str(input("Digite uma frase: ")).lower()

for caracter in frase:
    if caracter in "0123456789":
        print(f"Número encontrado: {caracter}")