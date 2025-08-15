'''Escreva uma função que receba dois parâmetros: uma string e um caractere,
 e conte quantas vezes esse caractere aparece na string.'''

def contagem(texto, caractere):
  contador = 0
  for c in texto: #c = caractere
    if c == caractere:
      contador+=1
  return contador

texto = input("Digite uma string: ").lower()
caractere = input("Digite o caractere que deseja contar: ").lower()

print(f"O caractere {caractere} aparece {contagem(texto,caractere)} vezes na string.")




   