x = int(input("Digite um número: "))
y = int(input("digite um outro número: "))
z = (x*y)+5
if z <= 0:
    resposta = "A"
elif z <= 100:
    resposta = "B"
else:
    resposta = "C"
print("Resultado final: %i. Resposta: %s" %(z,resposta))

#a) x = 5 e y = 10 -> 55, B
#b) x = 200 e y = 100 -> 20005, C
#c) x = 27 e y = -34 -> -913, A
#d) x = -8 e y =40 -> -315, A
#e) x = 50 e y = 3 -> 155, C
