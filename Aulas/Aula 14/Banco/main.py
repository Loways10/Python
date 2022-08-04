from conta import Conta
from cliente import Cliente

print('-' * 30)
print('Banco dos Bancos')
print('-' * 30)

cliente1 = Cliente('Sayumi', '123.654.987-13')
conta1 = Conta(cliente1, 1000)
print(conta1.titular.nome)
print(conta1.titular.cpf)

# conta1.extrato()
if(conta1.sacar(500)):
    print('Saque efetuado com sucesso')
else:
    print('Saldo insuficiente')

cliente2 = Cliente('Igor Oliveira', '987.951.753-53')
conta2 = Conta(cliente2, 1000, 3000.0)

conta2.extrato()
conta1.extrato()
# conta2.extrato()

# if(conta2.transferir(conta1, 150)):
#     print('Saldo insuficiente')
# else:
#     print('Transferencia efetuada com sucesso')

# conta2.extrato()
# conta1.extrato()

# conta3 = Conta('Mateus', 5000)
# if conta1.transferir(conta2, 50):
#     print('Transferencia realizada com sucesso')
# else:
#     print('Saldo insuficiente')

# conta2.extrato()
# conta1.extrato()