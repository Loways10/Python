# .txt

'''
    r  -> Ler
    W  -> Escrever
    a  -> Acrescentar
    r+ -> Ler e Acrescentar

'''
caminho = './Aulas/Aula 31'

# Escrever / Se o arquivo não existe ele vai criar se ja existir ele sobrescreve
'''with open(f'{caminho}/teste.txt', 'w') as arquivo:
    arquivo.write('Hello, World')'''

# Acrescentar    
'''with open(f'{caminho}/teste.txt', 'a') as arquivo:
    arquivo.write('\nMais uma linha')'''

# Ler
'''with open(f'{caminho}/teste.txt', 'r') as arquivo:
    texto = []
    for linha in arquivo:
        texto.append(linha)
    texto[0] = 'Linha 1\n'
    print(texto)'''

'''with open(f'{caminho}/teste.txt', 'w') as arquivo:
    for linha in texto:
        arquivo.write(linha)'''

