#ATIVIDADE COMPOSICAO
class Cabeça:
    #Define a cor da cabeça.
    def __init__(self, cor):
        self.cor = cor

class Boneco:
    #Cria boneco.
    def __init__(self, nome, cor_cabeça):
        self.nome = nome
        #Faz a composição entre duas classes.
        self.cabeça = Cabeça(cor_cabeça)
        self.destruido = False  #Inicialmente, o boneco não foi destruído.

    def destruir(self):
        print(f"{self.nome} foi destruído!")
        self.cabeça = None  #A cabeça não esta associada.
        self.destruido = True  #O boneco foi destruído.

#Criando um boneco com uma cabeça.
boneco = Boneco("Boneco", "Verde")

# Acessando a cor da cabeça do boneco.
print(f"A cabeça do {boneco.nome} é da cor {boneco.cabeça.cor}")

#Destruindo o boneco.
boneco.destruir()

#Tentando acessar a cabeça após a destruição.
if boneco.destruido:
    print("O boneco não existe, sua cabeça também foi destruída.")
else:
    print(f"A cabeça do {boneco.nome} está {boneco.cabeça}")
