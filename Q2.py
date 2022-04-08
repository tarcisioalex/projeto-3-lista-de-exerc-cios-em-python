numero1 = int(input("Colocando 3 números em ordem crescente...\nDigite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))
numeros = []

if numero1 < (numero2 and numero3):
    if numero2 < numero3:
        numeros = [numero1, numero2, numero3]
        print(numeros)
    else:
        numeros = [numero1, numero3, numero2]
        print(numeros)
elif numero2 < (numero1 and numero3):
    if numero1 < numero3:
        numeros = [numero2, numero1, numero3]
        print(numeros)
    else:
        numeros = [numero2, numero3, numero1]
        print(numeros)
elif numero3 < (numero1 and numero2):
    if numero1 < numero2:
        numeros = [numero3, numero1, numero2]
        print(numeros)
    else:
        numeros = [numero3, numero2, numero1]
        print(numeros)
else:
    print("Deu bug")
