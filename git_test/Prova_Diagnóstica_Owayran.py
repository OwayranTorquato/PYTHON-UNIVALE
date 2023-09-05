#Importando as bibliotecas necessárias.
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

# Definindo a função que será executada para enviar a mensagem.
def exibir_mensagem():
    name = name_entry.get()
    message = message_entry.get()

    # Definindo condição para exibição da janela com a mensagem.
    if name and message:
        message_window = tk.Toplevel(window)
        message_window.title("Mensagem Enviada")
        
        message_label = tk.Label(message_window, text=f'{name} diz: {message}')
        message_label.pack()
        
        window.wait_window(message_window)  # Aguarda até que a janela de mensagem seja fechada
        
    # Mensagem de erro será exibida caso o usuário não insira as informações.
    else:
        messagebox.showerror("Erro", "Por favor, insira um nome e uma mensagem!")

# Configurando a janela
window = tk.Tk()
window.title("Mensagem")
window.geometry('250x150')
color1 = '#2d404a' #cinza escuro
color2 = '#fcfcfc' #branco
window.config(bg=color1)

# Configurando a entrada das informações referentes ao nome.
name_label = tk.Label(window, text="Nome", font="Ivy 12 ", bg=color1, fg=color2)
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Configurando a entrada das informações referentes à mensagem.
message_label = tk.Label(window, text='Mensagem', font="Ivy 12 ", bg=color1, fg=color2)
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()

# Configurando o botão de enviar.
send_button = tk.Button(window, text='Enviar', command=exibir_mensagem, font="Ivy 12 bold", relief="raised", overrelief="ridge", bg=color1, fg=color2)
send_button.pack()

# Configurando a mensagem que será exibida para aguardar o usuário inserir dados.
waiting_message = tk.Label(window, text="Aguardando o envio da mensagem", font="Ivy 12", bg=color1, fg=color2)
waiting_message.pack()

window.mainloop()
