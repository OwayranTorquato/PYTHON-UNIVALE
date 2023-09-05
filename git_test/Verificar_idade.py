from tkinter import *
import tkinter as tk

def inseriridade():
     idade=int(entry_idade.get())
     if idade >= 18:
          resultado.set('Você é maior de idade!')
     else:
          resultado.set('Você é menor de idade!')

#cores a serem utlizadas
cor1="#fbff24"
cor2="#0c9474"
cor3="#070808"

#criando janela
janela = Tk()
janela.title ("Verificação de idade")

janela.geometry ("245x150")
janela.config (bg=cor2)

#criando botão
label_idade = tk.Label(janela,text="Digite a sua idade: ", bg=cor2, fg=cor3, font="Ivy 16 bold", anchor="center")
label_idade.pack()

entry_idade=tk.Entry(janela, bg=cor1, font="Arial 12 bold", justify=CENTER)
entry_idade.pack()

verificar=tk.Button(janela, text="Verificar", command=inseriridade, bg=cor2, fg=cor3, font="Arial 14 bold", justify="center", relief=RAISED, overrelief=RIDGE)
verificar.pack()

resultado=tk.StringVar()
label_resultado = tk.Label(janela,textvariable=resultado, bg=cor2, font="Arial 12 bold")
label_resultado.pack()

janela.mainloop()
