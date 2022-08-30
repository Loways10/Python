class Funcionario:
    valor_hora_cargo = [189.56, 86.05, 35.48]
    nome_cargo = ['Diretor', 'Gerente', 'Vendedor'] #usado na linha 15 // 0 - 1 - 2

    def __init__(self, nome, cargo, horas_trabalhadas, salario):
        self.nome = nome
        self.cargo = cargo
        self.horas_trabalhadas = horas_trabalhadas
        self.salario = salario

    def exibir_funcionario(self):
        print(f'NOME: {self.nome}')
        # print(f'CARGO: {self.cargo}')
        print(f'CARGO: {self.nome_cargo[self.cargo]}')
        print(f'HORAS TRABALHADAS: {self.horas_trabalhadas} horas')
        print(f'SALARIO: R${self.salario}')

    def adicionar_horas_trabalhadas(self):
        self.horas_trabalhadas += 1

    def calcular_salario(self):
        self.salario = self.horas_trabalhadas * self.valor_hora_cargo[self.cargo]
    
    @classmethod
    def alterar_salario_funcionarios(cls, indice, valor):
        cls.__valor_hora_cargo[indice] = valor

    @classmethod #decorador
    def retornar_cargos(cls):
        return cls.nome_cargo





fun = Funcionario('Gabriel', 0, 10, 0)

# print(fun.nome)
# print(fun.salario)
# print(fun.exibir_funcionario())
# fun.adicionar_horas_trabalhadas()
# print(fun.exibir_funcionario())

fun.calcular_salario()
print(fun.exibir_funcionario())