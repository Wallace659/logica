letra = str(input("Digite uma Letra:")).lower()

if len(letra) == 1:

    if letra in "aeiou":
        print("Essa letra é uma vogal")
    elif letra in "bcdfghjlmnpqrstvxz":
        print("Essa letra é uma consoante")
    else:
        print("Digite apenas uma Letra")