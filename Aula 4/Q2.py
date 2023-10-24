while True:
    usuario = input("Digite um usuário:")
    senha = input("Digite uma senha:")

    if usuario != senha:
        break
    else:
        print("Nome e senha não pode ser igual.")
