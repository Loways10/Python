from tkinter import *
from typing import final

def calcular():
    f = float(txtbox1.get())
    c = (f-32) *5/6
    final.set(str(round(c, 2)) + " graus Celcius")

tela = Tk()
tela.title("Conversor de Fahrenheit para Celsius")

final = StringVar()

lbl1 = Label(tela, text='Graus Fahrenheit:')
txtbox1 = Entry(tela)
btn1 = Button(tela, text='Calcular', command=calcular)
lblResultado = Label(tela, textvariable=final)

lbl1.grid()
txtbox1.grid()
btn1.grid()
lblResultado.grid()


tela.mainloop()