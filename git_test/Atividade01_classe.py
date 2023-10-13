##Crie uma classe chamada ContaBancaria que possua os atributos: titular, saldo.
##b) O método construtor __init__ deve aceitar o titular da conta e iniciar o saldo com 0.
##c) Crie um método chamado depositar que aceite um valor e adicione esse valor ao saldo da conta.
##d) Crie outro método chamado sacar que aceite um valor e subtraia esse valor do saldo da conta. No entanto, o saque só pode ser feito se houver saldo suficiente. Se não houver, deve imprimir uma mensagem indicando que o saldo é insuficiente.
##e) Finalmente, crie um método chamado ver_saldo que imprima o saldo atual da conta.
##f) Crie um objeto da classe ContaBancaria para um titular de sua escolha. Faça alguns depósitos, saques e verifique o saldo para testar a funcionalidade da classe.
class ContaBancaria:

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"O depósito no valor de {valor} reais foi realizado com sucesso!")
        else:
            print("O valor do depósito deve ser maior que 0")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"O saque de {valor} reais foi realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser maior que zero")

    def ver_saldo(self):
        print(f'O saldo atual do {self.titular} é de {self.saldo} reais.')

conta = ContaBancaria("Owayran")
conta.depositar(1350)
conta.depositar(200)
conta.sacar(500)
conta.sacar(250)
conta.depositar(120)
conta.depositar(1800)
conta.sacar(50)
conta.sacar(3000)

conta.ver_saldo()


