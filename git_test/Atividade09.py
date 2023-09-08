# Definindo uma função sem parâmetros e sem retorno, função simples que exibe mensagem ao ser chamada.
def owayran_nota_100():
    print("Owayran vai tirar nota 100 na matéria de Programação de Sistemas II")
owayran_nota_100()

# Definindo uma função com parâmetros e sem retorno, será utilizada para demonstrar os valores de multiplicação entre A e B.
def multiplicação(a,b):
    resultado = a*b
    print(f'A multiplicação de {a} e {b} é igual a {resultado}')
multiplicação(2,3)

# Definindo uma função com parâmetros e com retorno, que será usada para calcular a média de preços de produtos.
def media_preco(preco):
    total = sum(preco) # A função sum é utilizada para somar os elementos de uma sequência, ajuda a manter o código mais limpo. Encontra a soma de valores em uma sequencia numérica.
    media = total / len(preco)
    return media
preco_itens = [10.50, 11.60, 15.40, 8.90, 7.55]
media_itens = media_preco(preco_itens)
print(f"A média dos valores dos itens é de:{media_itens}")