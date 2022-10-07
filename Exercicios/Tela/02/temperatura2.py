from tkinter import *

tela = Tk()
tela.title('Conversor de Temperatura')
Label(tela, text='Conversor', font='Arial 18').grid(row=0, columnspan=4)
Label(tela, text='Temperatura').grid(row=1, column=0, sticky=W)

temperatura = Entry(tela)
temperatura.grid(row=2, columnspan=3, sticky=W+E)
def verificar():
    if len(temperatura.get().strip()) > 0:
        return True
    return False

def limpaCampo():
    temperatura.delete(0, END)
    temperatura.focus()

def celFah():
    if verificar():
        calc = float(temperatura.get()) * 1.8 + 32
        lblExibir.config(text=f'{calc} °F')
        limpaCampo()
    else:
        limpaCampo()
    
Button(tela, text='Celsius > Fahrenheit', command=celFah).grid(row=3, column=0)
Button(tela, text='Fahrenheit > Celsius').grid(row=3, column=1)
Button(tela, text='Celsius > Kelvin').grid(row=3, column=2)
Button(tela, text='Kelvin > Celsius').grid(row=4, column=0)
Button(tela, text='Kelvin > Fahrenheit').grid(row=4, column=1)
Button(tela, text='Fahrenheit > Celsius').grid(row=4, column=2)

lblExibir = Label(tela, font='Arial 32')
lblExibir.grid(columnspan=3)

tela.mainloop()