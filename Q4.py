salarioFixo = float(input("Olá, vamos calcular seu salário total.\nDigite o valor de seu salário fixo: "))
valorVendas = float(input("Qual o valor total das vendas que você realizou: "))

if valorVendas <= 1500:
    salarioTotal = (valorVendas*3/100) + salarioFixo
    print("O seu salario total é de R$%0.2f" %(salarioTotal))
elif valorVendas > 1500:
    salarioTotal = (valorVendas*5/100) + 45 + salarioFixo #45 é 3% de 1500
    print("O seu salario total é de R$%0.2f" %(salarioTotal))
else:
    print("Deu bug")
