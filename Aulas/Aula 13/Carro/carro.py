class Carro:
    def __init__(self, nome, cor, placa, ligado=False, andando=False):
        self.nome = nome
        self.cor = cor
        self.placa = placa
        self.ligado = ligado
        self.andando = andando

    def ligar_carro(self):
        if self.ligado:
            print(f'{self.nome} ja está ligado')
        self.ligado = True
        print(f'{self.nome} ligou...')

    def desligar_carro(self):
        if not self.ligado:
            return print(f'{self.nome} ja esta desligado')
        if self.andando:
            return print(f'{self.nome} esta andando')
        self.ligado = False
        print(f'{self.nome} desligou...')

    def andar(self):
        if not self.ligado:
            return print(f'{self.nome} está desligado')
        self.andando  = True
        print(f'{self.nome} andou . . . ')

    def parar_carro(self):
        if not self.ligado:
            return print(f'{self.nome} está desligado')
        if not self.andando:
            return print(f'{self.nome} está parado')
        self.andando = False
        print(f'{self.nome} parou.. . .')