from tkinter import *

telaInicial = Tk() # Instanciar
telaInicial['bg'] = '#cc22fa' # altera a cor de fundo / tem que vir antes de iniciar o mainloop
telaInicial.title('Minha primeira tela')
# telaInicial.geometry('500x500+3050+250')

largura = 850
altura = 650
larguraUser = telaInicial.winfo_screenwidth()
alturaUser = telaInicial.winfo_screenheight()
print(larguraUser, alturaUser) # Tela do Usuario
larguraX = int((larguraUser - largura)/2)
alturaY = int((alturaUser - altura)/2)

telaInicial.geometry(f'{largura}x{altura}+{larguraX}+{alturaY}')
telaInicial.resizable(True, True) # trava o usuario de aumentar ou diminuir a tela, tem que passar largura e altura(False, False)
telaInicial.minsize(850, 650)
telaInicial.maxsize(1920, 1080)
# telaInicial.state('zoomed') #zoomed ja abre a tela Cheia / iconic abre a tela minimizado

labelUsu = Label(telaInicial, text='Usuario: ')
labelUsu.pack()
labelSenha = Label(telaInicial, text='Senha: ')
labelSenha.pack()

def entrar():
    print('Ola, mundo!')
    labelMsg.config(text='ola, mundo!')

btnEntrar = Button(telaInicial, text='Entrar', command=entrar) # Cria o botão mas não gera ele na tela
btnEntrar.pack() # Faz o botão aparecer na tela

labelMsg = Label(telaInicial, text='Label') # Texto na tela da janela aberta
labelMsg.pack()



telaInicial.mainloop()

