import tkinter as tk



def inseriridade():
     idade=int(entry_idade.get())
     if idade >= 18:
          resultado.set('Você é maior de idade!')
     else:
          resultado.set('Você é menor de idade!')
    

root = tk.Tk()
root.title("Verificar Idade")

label_idade = tk.Label(root,text="Digite a sua idade: ")
label_idade.pack()

entry_idade=tk.Entry(root)
entry_idade.pack()

verificar = tk.Button(root, text="Verificar", command=inseriridade)
verificar.pack()

resultado=tk.StringVar()
label_resultado = tk.Label(root,textvariable=resultado)
label_resultado.pack()


root.mainloop()