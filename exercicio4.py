4.	#Escreva um programa que leia um número inteiro entre 1 e 7 e imprima o dia da semana correspondente a esse número. Isto é: domingo se for 1, segunda-feira se for 2, e assim por diante.

def dia_da_semana (numero):
    match numero:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sábado"
        case _:
            return "data inválida"
         
    
entrada= int(input("digite um numero de 1 a 7 para da semana"))

resultado= dia_da_semana (entrada)
print(resultado)