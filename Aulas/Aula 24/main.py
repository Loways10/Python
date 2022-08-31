from classe import *

agua = Produto('Agua 500ml', 2.50)
cerveja = Produto('Skola 350ml', 4.50)
refrigerante = Produto('Coca-Cola', 6.0)
agua.listarProduto()

cc = CarrinhoCompra()
cc.adicionar_produto(agua)
cc.adicionar_produto(cerveja)
cc.adicionar_produto(refrigerante)
cc.finalizar_compra()