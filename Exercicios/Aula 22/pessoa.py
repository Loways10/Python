class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):
    materiaTipos = ['Matematica', 'Portugues', 'Historia', 'Quimica', 'Fisica', 'Geografia']

    def __init__(self, nome, cpf, materia):
        super().__init__(nome)
        self.cpf = cpf
        self.materia = materia

    def listar_professor(self):
        print(f'{self.nome}')
        print(f'{self.cpf}')
        print(f'{self.materiaTipos[self.materia]}')


class Aluno(Pessoa):
    pass

p = Professor('Akio', '13781388727', 1)
p.listar_professor()