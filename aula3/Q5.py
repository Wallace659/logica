# faça um programa que pede para um usuario digitar 10 numeros e no final mostre a média desses 10 números.

soma = 0
for i in range(10):
    numero = float(input("Digite um numero:"))
    soma += numero

media = soma / 10
print(f"A média dos numeros é {media}")