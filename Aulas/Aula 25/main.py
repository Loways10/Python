from banco import Cliente, Conta

c1 = Cliente('Mateus F', '123.456.789-85')
c2 = Cliente('Igor F.', '987.654.321-85')

cc = Conta(4321, 100, c1)
# cc.sacar(10)
# cc.depositar(20)
# cc.listar_conta()

cc2 = Conta(1234, 400, c2)

cc.transferir(cc2, 50)
cc.listar_conta()

cc2.listar_conta()
