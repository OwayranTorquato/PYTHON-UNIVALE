def listagem():
    numeros = []
    for i in range(5):
         numero = int(input(f"Digite o {i+1}° número inteiro: "))
         numeros.append(numero)
    soma_numeros = 0

    for numero in numeros:
        soma_numeros += numero

    print(f'A soma dos números é {soma_numeros}')
    print("Números inseridos: ",numeros)

if __name__=="__main__":
    listagem()

