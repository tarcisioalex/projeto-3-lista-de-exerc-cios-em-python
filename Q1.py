medias = {}
nome = input("Olá, vamos calcular a média aritmética do aluno!\nQual o nome do aluno?: ")
nota1 = float(input("Qual a primeira nota?: "))
nota2 = float(input("Qual a segunda nota?: "))

media = (nota1 + nota2) / 2

if media >= 7 and media <= 10:
    print("O aluno obteve média %0.1f, e está aprovado!" %(media))
    medias[nome] = media
    print(medias)
elif media >= 0 and media < 7:
    print("O aluno obteve média %0.1f, e está reprovado!" %(media))
    medias[nome] = media
    print(medias)
else:
    print("Algo deu errado, por favor tente novamente.")
