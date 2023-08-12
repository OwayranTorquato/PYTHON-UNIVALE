import tkinter as tk
from tkinter import messagebox

# Funções de operações matemáticas
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Não é possível realizar a divisão por 0"

# Função para calcular a operação selecionada
def calcular():
    escolha = operacao.get()
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())

    if escolha == 1:
        resultado.set(adicao(num1, num2))
    elif escolha == 2:
        resultado.set(subtracao(num1, num2))
    elif escolha == 3:
        resultado.set(multiplicacao(num1, num2))
    elif escolha == 4:
        resultado.set(divisao(num1, num2))
    else:
        messagebox.showerror("Erro", "Operação inválida")

# Configuração da interface gráfica, sendo 'root' utilizado para nomear uma instancia principal
root = tk.Tk()
root.title("Calculadora")

operacao = tk.IntVar()

# Sendo 'label' um widget para exibir textos ou imagens de maneira estáticas em uma janela
label_operacao = tk.Label(root, text="Escolha a operação:")
label_operacao.pack()

# Sendo 'radio' que permite ao usuário escolher um botão entre vários outros na tela
radio_adicao = tk.Radiobutton(root, text="Adição", variable=operacao, value=1)
radio_adicao.pack()

radio_subtracao = tk.Radiobutton(root, text="Subtração", variable=operacao, value=2)
radio_subtracao.pack()

radio_multiplicacao = tk.Radiobutton(root, text="Multiplicação", variable=operacao, value=3)
radio_multiplicacao.pack()

radio_divisao = tk.Radiobutton(root, text="Divisão", variable=operacao, value=4)
radio_divisao.pack()

# Sendo 'label' um widget para exibir textos ou imagens de maneira estáticas em uma janela
label_num1 = tk.Label(root, text="Digite o primeiro número:")
label_num1.pack()

# Sendo 'entry' que permite receber dados do usuário
entry_num1 = tk.Entry(root)
entry_num1.pack()

# Sendo 'label' um widget para exibir textos ou imagens de maneira estáticas em uma janela
label_num2 = tk.Label(root, text="Digite o segundo número:")
label_num2.pack()

# Sendo 'entry' que permite receber dados do usuário
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Sendo 'calcular_button' o botão inserido na tela para calcular os números inseridos
calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.pack()
resultado = tk.StringVar()

# Sendo 'label' um widget para exibir textos ou imagens de maneira estáticas em uma janela
label_resultado = tk.Label(root, textvariable=resultado)
label_resultado.pack()

# Sendo 'mainloop' definido para permitir o inicio do loop dos eventos da interface gráfica,
#se atualizando a cada momento de acordo com o uso do usuário
root.mainloop()
