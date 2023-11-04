#ATIVIDADE ASSOCIAÇÃO
class Professor:
    def __init__(self,nome):
        self.nome = nome
        #Inicia uma lista vazia para armazenar os cursos para cada professor.
        self.cursosAssociados = []

    def associar_curso(self, curso):
        #Permite associar um curso a um professor.
        curso.associar_professor(self)
        self.cursosAssociados.append(curso)

    def cursos_associados(self):
        #Verifica se um professor está associado a um curso.
        if self.cursosAssociados:
            print(f"O professor {self.nome}, ministra os seguintes cursos:")
            for curso in self.cursosAssociados:
                print(curso.nome)
        else:
            print(f"O professor {self.nome}, não está associado a nenhum curso atualmente.")
    
class Curso:
    def __init__(self, nome):
        self.nome = nome
        #None significa que o professor ainda não está associado ao curso.
        self.professor = None

    def associar_professor (self,professor):
        #Permite associar o professor a um curso, garantindo que o professor se torne um atributo de Curso.
        self.professor = professor

#Cria objetos da classe professor.
professor1 = Professor("Mário")
professor2 = Professor("Dieimes")
professor3 = Professor("Michael")
professor4 = Professor("Giulio")

#Cria objetos da classe Curso
curso1 = Curso("Filosofia")
curso2 = Curso("Sistemas de Informação")
curso3 = Curso("Analise e Desenvolvimento de Sistemas")
curso4 = Curso("Gerenciamento de Banco de Dados")
curso5 = Curso("História")

#Associa professores a cursos.
professor1.associar_curso(curso1)
professor2.associar_curso(curso2)
professor3.associar_curso(curso3)
professor4.associar_curso(curso4)

#Exibe os cursos aos quais os professores estão associados.
print("Cursos ministrados pelos professores:")
professor1.cursos_associados()
professor2.cursos_associados()
professor1.associar_curso(curso5)

print("Cursos ministrados pelos professores após reajuste de grade:")
professor1.cursos_associados()
professor2.cursos_associados()
