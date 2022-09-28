from tkinter import *
from tkinter import messagebox

# Funções
def limparCampo():
    txtNum.delete(0, END)
    txtNum.focus()

def calcular():
    if len(txtNum.get().strip()) == 0:
        messagebox.showwarning(message='Digite um numero')
    elif not txtNum.get().strip().isnumeric():
        messagebox.showerror(message='Digite um numero valido')
    else:
        numero = int(txtNum.get().strip())
        tabuada = ''
        for i in range(11):
            tabuada += f'{txtNum.get()} x {i} = {int(txtNum.get()) * i} \n'
        lblTabuada.config(text=tabuada)
    limparCampo()

# Variaveis


# Inicio do Programa
tela = Tk()
tela.title('Tabuada')
tela.geometry('+900+200')

'''
    1 - Multiplicar 2 valores

    Entry
    Entry
    Button
    Label

'''

txtNum = Entry(tela)

btnCalcular = Button(tela, text='Calcular', command=calcular)

Label(tela, text='Tabuada', font='Arial 30').pack()
lblTabuada = Label(tela, font='Arial 18', bg='#ccc', anchor=W, justify=LEFT)

# Exibir
txtNum.pack()

btnCalcular.pack()

lblTabuada.pack()

tela.mainloop()
