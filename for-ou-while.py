#For: usamos para repetir o código com um número CONHECIDO E DEFINIDO
# de vezes

for i in range(1,6): #range = intervalo de 1 a 6 i= indice do vetor
    print(i)

#Outra forma
alunos = ["Melquisedeque","Rebeca","Sara", "Abraão","Paulo","Noé"]

for aluno in alunos:# in = dentro
    print(aluno) #Printa o elemnto sozinho

print(alunos)

#While: usado para repetir o código enquanto a condição for verdadeira
#não sabemos quantas vezes irá repetir
i = 1

while i<=5:
    print(i)
    i += 1

