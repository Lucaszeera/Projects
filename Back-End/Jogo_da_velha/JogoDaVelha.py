import velha, random, time

tab = velha.criaTabuleiro()
player = 'X'
modo = int(input("1 - Jogar contra CPU\n"
      "2 - Jogar com 2 players\n - "))
if modo == 2:
    while velha.temEspaco(tab) and not velha.haGanhador(tab):
        velha.imprime(tab)
        print("Vez do jogador: ", player)
        lin = int(input("Linha:"))
        col = int(input("Coluna:"))
        resp = velha.joga(tab, lin, col, player)
        if resp == True:
            player = velha.trocaJogador(player)
        else:
            print("Jogada invalida, digite outra posicao")
elif modo == 1:
    while velha.temEspaco(tab) and not velha.haGanhador(tab):
        velha.imprime(tab)
        if player == 'X':
            print("Vez do jogador: ", player)
        else:
            print("Vez do CPU")
        if player == 'O':
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.', end='')
            time.sleep(0.5)
            print('.')
            time.sleep(0.5)
            lin, col = velha.cpu_jogar()

        else:
            print('')
            lin = int(input("Linha: "))
            col = int(input("Coluna: "))
        resp = velha.joga(tab, lin, col, player)
        if resp == True:
            player = velha.trocaJogador(player)
        else:
            if player == 'X':
                print("Jogada invalida, digite outra posicao")
            else:
                while resp == False:
                    lin, col = velha.cpu_jogar()
                    resp = velha.joga(tab, lin, col, player)
                    if resp == True:
                        player = velha.trocaJogador(player)
player = velha.trocaJogador(player) 
if velha.haGanhador(tab):
    if modo == 2:
        print(player + " ganhou")
    else:
        if player == 'X':
            print(player + " ganhou")
        else:
            print("CPU ganhou")
else:
    print("Deu velha!")