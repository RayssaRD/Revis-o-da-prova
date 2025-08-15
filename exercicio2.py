'''Crie uma função que receba uma lista de números 
e retorne uma nova lista com os números ordenados em ordem crescente.'''
def ordenar_lista(lista):
    return sorted(lista)

numeros = [1,3,10,9,6,2,4,5,7,8]
numeros_ordenados = ordenar_lista(numeros)
print(numeros_ordenados)