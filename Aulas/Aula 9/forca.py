# Jogo da Forca
#Criando uma lista de palavras para o jogo
#Lista ou Vetor

from random import randint

palavras = ['Casa', 'Carro', 'Aviao', 'Moto', 'Mesa', 'Cadeira', 'Teto', 'Casarao', 'Terreno', 'Escola', 'Curso', 'Musica', 'Montanha', 'Piscina', 'Pia', 'Porto', 'Pa', 'Padaria', 'Empresa', 'Ilha', 'Televisao', 'Radio', 'Rua', 'Planta', 'Arvore', 'Portao', 'Computador', 'Escada', 'Sofa']

indice = randint(0, len(palavras)) # recebe um numero aleatorio
palavra_secreta = palavras[indice]
# palavra_secreta = palavras[1:] pega todos os itens da variavel
# palavra_secreta = palavras[1] pega o item 1
tentativa = []
chutes = []

for i in range(len(palavra_secreta)):
     tentativa.append('_')

print(palavra_secreta)
print(tentativa)

def exibirMsg(msg):
    print(msg)

def encontraLetra(chute):
    temLetra = False
    for i, letra in enumerate(palavra_secreta):
        if (chute.upper() == letra.upper()):
            tentativa[i] = chute.upper()
            temLetra = True
    return temLetra        
        

def jogar():
    tentativas = 5
    while(True):
        chute = input('Digite uma letra R: ')
        if(encontraLetra(chute)):
            exibirMsg(tentativa)
        
        else: 
            exibirMsg(f'Letra {chute} não encontrada')
            chutes.append(chute.upper())
            exibirMsg(chutes)
            tentativas -= 1
            exibirMsg(f'Restam {tentativas} tentativas')
            exibirMsg(tentativa)
        
        if(verificaVitoria()):
            exibirMsg('Parabens! Você venceu!')
            break
        
        if(tentativas <= 0):
            exibirMsg('Você perdeu! \n Jogue novamente')
            exibirMsg(f'A palavra secreta era {palavra_secreta.upper()}')
            break

def verificaVitoria():
    if('_' in tentativa):
        return False
    else:
        return True

def iniciaJogo():
    global indice
    indice = randint(0, len(palavras)) # recebe um numero aleatorio
    global palavra_secreta
    palavra_secreta = palavras[indice]
    # palavra_secreta = palavras[1:] pega todos os itens da variavel
    # palavra_secreta = palavras[1] pega o item 1
    global tentativa
    tentativa = []
    global chutes
    chutes = []

    for i in range(len(palavra_secreta)):
        tentativa.append('_')

while(True):
    iniciaJogo()
    exibirMsg('***** JOGO DA FORCA *****')
    menu = int(input('1 - Jogar \n 2 - Sair \n R: '))
    if(menu == 1):
        jogar()
    else:
        print('Tchau!')
        break