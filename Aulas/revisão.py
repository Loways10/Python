# Leia 5 valores, mostre a media dos numeros e a soma

numeros = []

# numeros.insert[indice] = valor
# numeros.append(valor) -> adiciona ao final da lista

for i in range(5):
    numeros.append(int(input('Digite um valor ')))
# print(numeros[i])

soma = 0
for numero in numeros:
    soma += numero

media = soma / len(numeros)

print(soma)
print(media)