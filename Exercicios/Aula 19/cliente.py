from random import randint

class Cliente:

    def __init__(self, nome, sexo, telefone, endereco):
        self.codigo = self.gerar_codigo_usuario()
        self.nome = nome
        self.sexo = sexo
        self.telefone = telefone
        self.endereco = endereco

    def atualizar_endereco():
        pass

    def atualizar_telefone():
        pass

    def listar_cliente():
        pass

    @staticmethod
    def gerar_codigo_usuario():
        return randint(1001, 9999)

    

cliente = Cliente('Akio', 'M', 9968538007, 'Rio de Janeiro')
print(cliente.codigo)
print(cliente.nome)
print(cliente.sexo)
print(cliente.telefone)
print(cliente.endereco)