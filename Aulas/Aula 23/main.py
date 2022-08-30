from classe import * # * significa impórtar TUDO

editora = Editora()
# print(editora.codigo)
editora.razaoSocial = 'Safaria'
# print(editora.razaoSocial)
editora.email = "contato@safaria.com.br"
editora.telefone = "11969857463"
editora.listarEditora()


livro = Livro("O Titulo", "Pt-br")
livro.editora = editora


livro.listar_livro()
