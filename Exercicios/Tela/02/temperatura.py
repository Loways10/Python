from cgitb import text
from tkinter import *

tela = Tk()
tela.title('Conversor de Temperatura v0.3')
tela.resizable(False, False)

# ______________ FUNÇÕES _______________
def calcular():
    c = txtNum
    calculo = float(((c * 9) / 5) + 32)
    farenheit = f'Fahrenheit {c}'
    lblExibir.config(text=farenheit)

# ___________ CENTRALIZANDO ____________
largura = 600
altura = 600

larguraUser = tela.winfo_screenwidth()
alturaUser = tela.winfo_screenheight()
posx = int((larguraUser - largura) / 2)
posy = int((alturaUser - altura) / 2 - 20)
tela.geometry(f'{largura}x{altura}+{posx}+{posy}')

# ______________ INPUT ________________
txtNum = Entry(tela).grid(row=1, columnspan=3)

lblTitulo = Label(tela, text='Conversor de Temperatura', font='Arial 20')
lblExibir = Label(tela)

lblTitulo.grid(row=0, columnspan=4)

Label(tela, text='Celcius', font='Calibri 12').grid(row=2, column=0)
Label(tela, text='Fahrenheit', font='Calibri 12').grid(row=2, column=2)
Label(tela, text='Kelvin', font='Calibri 12').grid(row=2, column=4)

# ______________ BOTÕES _______________

Button(tela, text='Converter', font='Arial 16', command=calcular).grid(row=3, columnspan=4)




tela.mainloop()