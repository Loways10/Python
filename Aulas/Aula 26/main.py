from funcionario import *
from endereco import *

est1 = Estado('Estado 1', 'SG')
cid1 = Cidade('Cidade 1 ', est1)
end1 = Endereco('Rua do End 1', 12, 'Bairro Nobre', '12347-450', cid1)

g = Gerente('Nome completo', '15/02/1995', '123.123.456-55', end1)
print(g.endereco.rua)
g.getSalario()


est2 = Estado('São Paulo', 'SP')
cid2 = Cidade('São Paulo', est2)
end2 = Endereco('Av. Paulista', 19, 'Centro', '12d347-450', cid2)

v = Vendedor('Vendedor nome completo', '05/11/1987', '144.444.854-85', end2)
print(v.endereco.listar())
print(round(v.getSalario(), 2))
print(v.equipe)