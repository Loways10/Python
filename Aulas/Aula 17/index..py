# Jogo da Velha

'''       0   1   2
    0   [ 1 , 2 , 3 ]
    1   [ 1 , 2 , 3 ]
    2   [ 1 , 2 , 3 ]

    Condição de vitoria
    linha
    X X X

    Coluna
    X
    X
    X

    Diagonal
    X
        X
            X
            X
        X
    X   
'''

from calendar import TUESDAY


tabuleiro = [
    [ 1 , 2 , 3 ],
    [ 4 , 5 , 6 ],
    [ 7 , 8 , 9 ]
]

board = []
cont = 1
for i in range(3):
    b = []
    for j in range(3):
        b.append(cont)
        cont += 1
    board.append(b[:])

# print(tabuleiro)
# print(board)

def listar_tabuleiro():
    for i in tabuleiro:
        print(i)

def pergunta_jogada():
    while(True):
        jogada = int(input('Onde deseja jogar? '))
        if verifica_vazio(jogada):
            return jogada

def verifica_vazio(valor):
    for i in tabuleiro:
        for j in i:
            if j == valor:
                return True
    return False

def verificaVitoria():
    #linha
    for i in range(len(tabuleiro)):
        if tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][0] == tabuleiro[i][1]:
            return True
        print('verifica colunas')
        print(tabuleiro[0][i], tabuleiro[1][i], tabuleiro[0][i])
        if (tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]):
            return True
    if(tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]):
        return True
    if(tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0]):
        return True

def alterarCampo(valor, letra):
    for i in range(len(tabuleiro)):
        if tabuleiro[i][0] == valor:
            tabuleiro[i][0] = letra
        elif tabuleiro[i][1] == valor:
            tabuleiro[i][1] = letra
        elif tabuleiro[i][2] == valor:
            tabuleiro[i][2] = letra

while(True):
    menu = input(' 1 - JOGAR \n 2 - SAIR \n R: ')
    if menu == "1":
        jogador1 = input('Digite aqui o nome do jogador 1: ')
        jogador2 = input('Digite aqui o nome do jogador 2: ')
        jogadas = 0
        contadorVitoria = 0
        while(True):
            listar_tabuleiro()
            if(jogadas % 2 == 0):
                print(jogador1)
                alterarCampo(pergunta_jogada(), "X")
                if verificaVitoria():
                    contadorVitoria += 1
                    print(f'{jogador1} ganhou a partida {contadorVitoria} vez(es)! ')
                    break
            else:
                print(jogador2)
                alterarCampo(pergunta_jogada(), "O")
                if verificaVitoria():
                    contadorVitoria += 1
                    print(f'{jogador2} ganhou a partida {contadorVitoria} vez(es)! ')
                    break

            jogadas += 1
            if jogadas == 9:
                print('Deu velha! ')
                break
    else:
        print('Até Logo')
        break




    
