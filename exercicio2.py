#2.	Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
# - Homens: (72,7 × h) − 58
# - Mulheres: (62,1 × h) − 44,7
altura = float(input("Digite sua altura: "))
genero = input("Digite (m) para gênero masculino e (f) para gênero feminino: ")
homem = (72.7 * altura) -  58
mulher = (62.1 * altura) - 44.7
if genero.lower() == "m":
    print(f"O seu peso ideal é: {homem}")

elif genero.lower() =="f": 
    print(f"O seu peso ideal é: {mulher}")

else:
    print("Erro!")




   