import random
def criaTabuleiro():
    tab = []
    tab.append([' '] * 3)
    tab.append([' '] * 3)
    tab.append([' '] * 3)
    return tab


def trocaJogador(jogador):
    if jogador == 'X':
        return 'O'
    else:
        return 'X'


def haGanhador(m):
    for i in range(3):
        if m[i][0] == m[i][1] and m[i][1] == m[i][2] and m[i][0] != ' ':
            return True
        if m[0][i] == m[1][i] and m[1][i] == m[2][i] and m[0][i] != ' ':
            return True
    if m[0][0] == m[1][1] and m[1][1] == m[2][2] and m[0][0] != ' ':
        return True

    if m[0][2] == m[1][1] and m[1][1] == m[2][0] and m[0][2] != ' ':
        return True

    return False


def temEspaco(matriz):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == ' ':
                return True
    return False


def joga(matriz, lin, col, jogador):
    if lin < 0 or lin > 2 or col < 0 or col > 2:
        return False
    if matriz[lin][col] != ' ':
        return False
    matriz[lin][col] = jogador
    return True


def imprime(matriz):
    for lin in matriz:
        print(lin)

def cpu_jogar():
    lin = random.randint(0, 2)
    col = random.randint(0, 2)
    return lin, col