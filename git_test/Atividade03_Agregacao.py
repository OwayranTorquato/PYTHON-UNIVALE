#ATIVIDADE AGREGAÇÃO
class Monitor:
    def __init__(self, modelo, tamanho):
        #Define monitor em modelo e tamanho.
        self.modelo = modelo
        self.tamanho = tamanho

    def informacoes_monitor(self):
        #Mostra as informações de monitor.
        print(f"Monitor {self.modelo} de {self.tamanho} polegadas")

class Computador:
    def __init__(self, nome, monitor=None):
        #Define informações de computador e qual monitor ele possui.
        self.nome = nome
        self.monitor = monitor

    def conectar_monitor(self, monitor):
        #Conecta um monitor.
        self.monitor = monitor

    def informacoes_monitor(self):
        #Mostra informações de um computador e de monitor.
        if self.monitor:
            print(f"Computador {self.nome} com o seguinte monitor:")
            self.monitor.informacoes_monitor()
        else:
            print(f"Computador {self.nome} sem monitor")

#Criação dos objetos e cumprimento dos métodos.
monitor1 = Monitor("Dell", 24)
computador1 = Computador("PC Gamer")
computador1.conectar_monitor(monitor1)
monitor2 = Monitor("LG", 27)
computador2 = Computador("Desktop Office")
computador1.informacoes_monitor()
computador2.informacoes_monitor()
