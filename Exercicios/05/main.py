from empresa import Chefe, Comissionado

c = Chefe()
c.adicionarEmpregado('Gabriel Monteiro', 'Rua Itaim')
c.exibirEmpregado()
c.adicionarSalario(500)
c.adicionarSalario(100)
c.calcularSalario()


com = Comissionado(2000, 68, 12)
com.adicionarEmpregado('Pedro Batista', 'Rua das Malandragens')
com.exibirEmpregado()
com.calcularSalario()