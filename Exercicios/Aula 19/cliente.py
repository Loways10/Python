from random import randint

class Cliente:

    def __init__(self, nome, sexo, telefone, endereco):
        self.codigo = self.gerar_codigo_usuario()
        self.nome = nome
        self.sexo = sexo
        self.telefone = telefone
        self.endereco = endereco

    def atualizar_endereco(self, valor):
        self.endereco = valor

    def atualizar_telefone():
        pass

    def listar_cliente():
        pass

    @staticmethod
    def gerar_codigo_usuario():
        return randint(1001, 9999)

    

cliente = Cliente('Akio', 'M', 9968538007, 'Rio de Janeiro')
print(cliente.codigo)

while(True):
    menu = input('1 - Nome \n2 - sexo \n3 - telefone \n4 - mudar endereco \n5 - sair \nR: ')
    if(menu == '1'):
        print(cliente.nome)
    elif(menu == '2'):
        print(cliente.sexo)
    elif(menu == '3'):
        print(cliente.telefone)
    elif(menu == '4'):
        cliente.atualizar_endereco()
    else:
        break

print(cliente.endereco)