#importando as funções a serem utilizadas
def adicao (x,y):
    return x+y
def subtracao (x,y):
    return x-y
def multiplicacao (x,y):
    return x*y
def divisao (x,y):
    if y !=0:
        return x/y
    else:
        "Não é possível realizare a divisão por 0"

#definindo a tabela de legendas para puxar a função
print ("1: ADIÇÃO")
print ("2: SUBTRAÇÃO")
print ("3: MULTIPLICAÇÃO")
print ("4: DIVISÃO")

#espaço reservado para entrada de dados do usuário
escolha = input("Digite a o número da operação a ser realizada: ")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

#selecionando as condicionais para mostrar o resultado na tela
if escolha == '1':
    print (num1, "+",num2,"=",adicao(num1,num2))
elif escolha=='2':
    print (num1,"-",num2,"=",subtracao(num1,num2))
elif escolha=='3':
    print (num1,"*",num2,"=",multiplicacao(num1,num2))
elif escolha=='4':
    print (num1,"/",num2,"=",divisao(num1,num2))
else:
    print ("Operação inválida")
