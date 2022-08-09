class Filme:
    def __init__(self, nome, autor, ano, tema, alugado = False):
        self.nome = nome
        self.autor = autor
        self.ano = ano
        self.tema = tema
        self.alugado = alugado

    def alugarFilme(self):
        if self.alugado:
            return print('Filme ja alugado')
        self.alugado = True
        return print(f'{self.nome} foi alugado com sucesso')

    def devolverFilme(self):
        if not self.alugado:
            return print('Filme ja foi devolvido')
        self.alugado  = False
        return print(f'{self.nome} foi devolvido com sucesso')

    def listarFilme (self):
        pass
        