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
    def __init__(self, nome, ano_nascimento, ano_escolar):
        super().__init__(nome)
        self.ano_nascimento = ano_nascimento
        self.ano_escolar = ano_escolar

    def listar_aluno(self):
        print(f'{self.nome}')
        print(f'{self.ano_nascimento}')
        print(f'{self.ano_escolar}')

    def alterar_ano_escolar(self, valor):
        self.ano_escolar = valor

    def idade_aluno(self):
        print(f'{self.ano_escolar - self.ano_nascimento}')

p = Professor('Akio', '13781388727', 1)
p.listar_professor()
print('---' * 15)
a = Aluno('Kenji', 1994, 2019)
a.listar_aluno()
print('---' * 15)
a.alterar_ano_escolar(2022)
a.listar_aluno()
a.idade_aluno()