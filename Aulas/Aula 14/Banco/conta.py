from random import randint
class Conta:
    def __init__(self, titular, saldo, limite = 1000.0):
        self.numero = self.gerar_numero_conta()
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def gerar_numero_conta(self):
        numero = str(randint(10000, 99999)) + "-1"
        return numero

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
        print('Saque efetuado com sucesso')

    def depositar(self, valor):
        self.saldo += valor
        print('Deposito efetuado com sucesso')

    def extrato(self):
        print(f'{self.numero} de {self.titular.nome} \nsaldo de R$ {self.saldo} \ne limite de R$ {self.limite}')

    def transferir(self, contaDestinatario, valor):
        if not self.sacar(valor):
            return False
        else:
            contaDestinatario.depositar(valor)
            return True