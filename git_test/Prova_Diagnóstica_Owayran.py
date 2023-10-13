# CÓDIGO DESENVOLVIDO PELO ALUNO OWAYRAN
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

# Configurando a janela e definindo cores.
window = tk.Tk()
window.title("Mensagem")
window.geometry('250x150')
color1 = '#2d404a' #cinza escuro
color2 = '#fcfcfc' #branco


# Configurando a entrada das informações referentes ao nome.
name_label = tk.Label(window, text="Nome")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Configurando a entrada das informações referentes à mensagem.
message_label = tk.Label(window, text='Mensagem')
message_label.pack()
message_entry = tk.Entry(window)
message_entry.pack()



# Configurando o botão de enviar.
send_button = tk.Button(window, text='Enviar', command=exibir_mensagem)
send_button.pack()

# Configurando a mensagem que será exibida para aguardar o usuário inserir dados.
waiting_message = tk.Label(window, text="Aguardando o envio da mensagem")
waiting_message.pack()

window.mainloop()
 