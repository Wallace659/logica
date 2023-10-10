alternativa = str(input("você deseja sair? s/n")).lower().strip()


if alternativa == "s" or alternativa == "n":
    print("operação válida")
else:
    print(" operação inválida")