nomeProduto = input("Olá vamos analisar o estoque.\nQual o nome do produto?: ")
estoque = int(input("Qual a quantidade desse produto presente no estoque?: "))
estoqueMax = int(input("Qual a quantidade máxima desse produto no estoque?: "))
estoqueMin = int(input("Qual a quantidade mínima desse produto no estoque?: "))

estoqueMed = (estoqueMax + estoqueMin)/2

if estoque >= estoqueMed:
    print("A quantidade de %s em estoque é maior que a média, não é necessário efetuar a compra." %(nomeProduto))
else:
    print("A quantidade de %s em estoque é menor que a média, é necessário efetuar a compra." %(nomeProduto))
