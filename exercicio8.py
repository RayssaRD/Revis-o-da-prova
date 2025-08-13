#Crie um programa que leia três números e imprima o maior entre eles.
numeroum = int(input("Digite o primeiro número"))
numerodois = int(input("Digite o segundo número"))
numerotres = int(input("Digite o terceiro número"))
maior = max(numeroum,numerodois, numerotres)
print(f"O maior número é {maior}")
