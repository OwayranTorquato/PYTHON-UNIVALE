def dicionario ():
    alunos={}
    for i in range(3):
        nome = input(f"Digite o nome do {i+1}° aluno: ")
        nota = float(input(f"Digite a nota do {i+1}° aluno: "))
        alunos[nome] = nota
    print("Dados dos alunos listados: ", alunos)
    soma_das_notas=0

    for nota in alunos.values():
        soma_das_notas += nota
    media = soma_das_notas/len(alunos)
    print(f"A média das notas dos alunos é: {media:.2f}")

if __name__ == "__main__":
    dicionario()