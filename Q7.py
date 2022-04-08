homem1 = int(input("Olá vamos calcular a idade de vcs\nQual a idade do primeiro homem?: "))
homem2 = int(input("Qual a idade do segundo homem?: "))
mulher1 = int(input("Qual a idade da primeira mulher?: "))
mulher2 = int(input("Qual a idade da segunda mulher?: "))

if homem1 > homem2:
    homemMaisVelho = homem1
    homemMaisJovem = homem2
else:
    homemMaisVelho = homem2
    homemMaisJovem = homem1

if mulher1 > mulher2:
    mulherMaisVelha = mulher1
    mulherMaisJovem = mulher2
else:
    mulherMaisVelha = mulher2
    mulherMaisJovem = mulher1

soma = homemMaisVelho + mulherMaisJovem
produto = homemMaisJovem * mulherMaisVelha

print("A soma das idades do homem mais velho com a mulher mais jovem é %i " %(soma))
print("O produto das idade do homem mais jovem com a mulher mais velha é %i " %(produto))
