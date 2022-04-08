horaIni = int(input("Olá, irei calcular o tempo de jogo da partida de xadrez\nDigite a hora de inicio do jogo: "))
horaFim = int(input("Digite a hora do fim do jogo: "));

if ((horaIni and horaFim) < 24):
    if horaIni < horaFim:
        horaTotal = horaFim - horaIni
        print("Horas totais de jogo: %i" %(horaTotal))
    elif horaIni > horaFim:
        horaTotal = ((24 - horaIni) + horaFim)
        print("Horas totais de jogo: %i" %(horaTotal))
    else:
        print("Deu bug")
else:
    print("Formato de hora inválido, tente novamente")
