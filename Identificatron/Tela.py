from tkinter import *

window = Tk()
entradaTexto = Entry(window)
labelDeTexto = Label(window)

def mudarTexto():
    myText = entradaTexto.get() 
    labelDeTexto.configure(text=myText) 

def configure():
    window.title("Teste do TKinter")

    window.geometry('600x600')

    entradaTexto.configure(width=10)
    entradaTexto.grid(column=0, row=0)

    labelDeTexto.configure(text="digite um texto")
    labelDeTexto.grid(column=1, row=1)

    botaoMudaTexto = Button(window, text="Pressione aqui", command=mudarTexto)
    botaoMudaTexto.grid(column=2, row=0)

    window.mainloop() 

configure()