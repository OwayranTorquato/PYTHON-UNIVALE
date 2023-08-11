#puxar a função para exibir os valores
def exibir_maior_valor(valor1,valor2):
    if valor1>valor2:
        return valor1
    else:
        return valor2

#definir as váriaveis que irão receber os dados do usuário
valor1=float(input("Digite o primeiro valor a ser considerado: "))
valor2= float(input("Digite o segundo valor a ser considerado: "))

#relaciona a função para exibir o maior valor inserido
maior_valor = exibir_maior_valor(valor1,valor2)

#exibir o valor
maior_valor = print("O maior valor digitado foi: ", maior_valor)
