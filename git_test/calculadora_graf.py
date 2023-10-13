#importar as bibliotecas necessárias para config gráfica da calculadora
from tkinter import *
from tkinter import ttk
import tkinter as tk

#cores a serem utilizadas
color1 = '#272930' #cinza escuro
color2 = '#fcfcfc' #branco
color3 = '#2b3759' #azul
color4 = '#84a5b3' #azul cinza
color5 = '#fa7a0a' #laranja

#configurando o título da janela
janela = Tk()
janela.title ("Calculadora")

#definindo tamanho da janela da calculadora
janela.geometry('235x310')

#config da janela
janela.config(bg=color1) #cor de fundo

#dividindo frame display
frame_tela = Frame(janela, width=235, height=50, bg=color3)
frame_tela.grid(row=0, column=0)

frame_body = Frame(janela, width=235, height=268)
frame_body.grid(row=1, column=0)

#váriavel todos os valores
todos_valores=''

#criando Label
valor_texto = StringVar()

#criando lógica da calculadora
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)

    
    #passando valor para a tela
    valor_texto.set(todos_valores)

def calcular():
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))

#funcao limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")



app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=color3, fg=color2)
app_label.place(x=0, y=0)

#criando botões e estilizando
b_clean = Button(frame_body, command=limpar_tela, text = "C", width=11, height=2, bg=color4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_clean.place(x=0,y=0)
b_percent = Button(frame_body, command=lambda:entrar_valores('%'), text ="%", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_percent.place(x=118,y=0)
b_div = Button(frame_body, command=lambda:entrar_valores('/'),text = "/", width=5, height=2, bg=color5, fg=color2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_div.place(x=177,y=0)

b_7 = Button(frame_body, command=lambda:entrar_valores('7'),text = "7", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_7.place(x=0,y=52)
b_8 = Button(frame_body, command=lambda:entrar_valores('8'),text = "8", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_8.place(x=59,y=52)
b_9 = Button(frame_body, command=lambda:entrar_valores('9'),text = "9", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_9.place(x=118,y=52)
b_mult = Button(frame_body, command=lambda:entrar_valores('*'),text = "*", width=5, height=2, bg=color5, fg=color2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_mult.place(x=177,y=52)

b_4 = Button(frame_body, command=lambda:entrar_valores('4'),text = "4", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_4.place(x=0,y=104)
b_5 = Button(frame_body, command=lambda:entrar_valores('5'),text = "5", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_5.place(x=59,y=104)
b_6 = Button(frame_body, command=lambda:entrar_valores('6'),text = "6", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_6.place(x=118,y=104)
b_sub = Button(frame_body, command=lambda:entrar_valores('-'),text = "-", width=5, height=2, bg=color5, fg=color2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_sub.place(x=177,y=104)

b_1 = Button(frame_body, command=lambda:entrar_valores('1'),text = "1", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_1.place(x=0,y=156)
b_2 = Button(frame_body, command=lambda:entrar_valores('2'),text = "2", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_2.place(x=59,y=156)
b_3 = Button(frame_body, command=lambda:entrar_valores('3'),text = "3", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_3.place(x=118,y=156)
b_adic = Button(frame_body, command=lambda:entrar_valores('+'),text = "+", width=5, height=2, bg=color5, fg=color2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_adic.place(x=177,y=156)

b_0 = Button(frame_body, command=lambda:entrar_valores('0'),text = "0", width=11, height=2, bg=color4, font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_0.place(x=0,y=208)
b_ponto = Button(frame_body, command=lambda:entrar_valores('.'),text = ".", width=5, height=2, bg=color4,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_ponto.place(x=118,y=208)
b_result = Button(frame_body, command= calcular,text = "=", width=5, height=2, bg=color5, fg=color2,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_result.place(x=177,y=208)

#permitir loop dos eventos dentro da calculadora
janela.mainloop()
