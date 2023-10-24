while True:
    nome = str(input("Digite um nome:"))

    if len(nome) > 3:
        break
    else:
        print("Digite um nome com no minimo 3 caracteres.")

while True:
    idade = int(input("Digite sua idade:"))

    if idade >=0 and idade <=150:
        break
    else:
        print("Digite uma idade entre 0 a 150")

while True:
    salario = float(input("Digite um valor:"))
    if salario > 0:
        break
    else:
        print("Digite um salário maior do que 0.")

while True:

    sexo = str(input("Digite seu sexo ( F ou M ):")).upper()
    if len(sexo) == 1:
        if sexo == "M" or sexo == "F":
            break
        else:
            print("Digite um sexo válido ou M ou F")
    else:
        print("Digite apenas uma letra")

while True:    
    estadocivil = str(input("Digite seu estado civil:")).upper()