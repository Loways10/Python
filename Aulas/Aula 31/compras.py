from tkinter import *
from tkinter import messagebox

def limparCampo():
    txtItem.delete(0, END)
    txtItem.focus()

def verificarEntry():
    if len(txtItem.get().strip()) > 0:
        return True
    False

def adicionar():
    if verificarEntry():
        lista.insert(END, txtItem.get().strip())
        itens.append(txtItem.get().strip())
    limparCampo()
    print(itens)

def remover():
    indice = retornarIndex()
    if not indice == None:
        lista.delete(indice)
        del itens[indice]
    print(itens)

def retornarIndex():
    for indice in lista.curselection():
        return indice

def salvar():
    with open(f'{caminho}/listaDeCompras.txt', 'w', encoding='utf-8') as arquivo:
        for i in itens:
            arquivo.write(i + '\n')
    messagebox.showinfo(message='Lista salva com sucesso!')

def carregarArquivo():
    with open (f'{caminho}/listaDeCompras.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            itens.append(str(linha).replace('\n', ''))
            lista.insert(END, linha)
    print(itens)

# Variaveis
itens = []
caminho = './Aulas/Aula 31'

tela = Tk()
tela.geometry('300x400+1920+100')
tela.title('Lista de Compras')
tela.resizable(False, False)

Label(tela, text='Lista de Compras', font='Calibri 24').pack()

txtItem = Entry(tela)
txtItem.pack()

Button(tela, text='Adicionar', font='Arial 12', command=adicionar).pack()

lista = Listbox(tela)
Label(tela, font='Calibri 10').pack()
lista.pack()

Button(tela, text='Salvar', font='Arial 12', command=salvar).pack()
Button(tela, text='Remover', font='Arial 12', command=remover).pack()

carregarArquivo()
tela.mainloop()