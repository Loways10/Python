from random import randint

class Pessoa:
    def __init__(self, nome, nascimento):
        self.__codigo = self.gerarCodigo()
        self.__nome = nome
        self.__nascimento = nascimento

    def getcodigo():
        pass

    def getnome(self, valor):
        self.__nome = valor

    def getnascimento():
        pass

    @staticmethod
    def gerarCodigo():
        return randint(1000, 9999)

    def exibirPessoa(self):
        print(f'Codigo: {self.__codigo}, Nome: {self.__nome}')