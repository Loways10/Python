from carro import Carro

c1 = Carro('Palio', 'Preta', ' IU12Y4')
print(c1.nome, c1.placa, c1.cor, c1.ligado, c1.andando)

c1.ligar_carro()
c1.andar()
c1.parar_carro()
c1.desligar_carro()

# c1.ligar_carro()
# print(c1.ligado)
# c1.ligar_carro()
# # c1.desligar_carro()
# print(c1.ligado)

# c1.nome = 'Celta'
# print(c1.nome, c1.placa, c1.cor)

# c2 = Carro('Corsa', 'Prata', 'TRA18U4')
# print(c2.nome, c2.placa, c2.cor, c2.ligado, c2.andando)