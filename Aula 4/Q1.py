while True:
    numero = int(input("Digite um numero:"))

    if numero <= 10:
        print(f"valor do número {numero} é válido")
        break
    else:
        print(f"valor do número {numero} é invalido")



while True:
    nota = float(input("Digite uma nota:"))
    
    if nota >=0 and nota <=10:
        print("Nota valida")
        break
    else:
        print(nota)