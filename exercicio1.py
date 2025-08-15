#Faça um programa que lê o salário de um trabalhador e o valor da prestação de um empréstimo, depois verifica se a prestação é maior que 20% do salário e imprime a mensagem: "Empréstimo não concedido", caso contrário, imprime: "Empréstimo concedido".
salario = float(input("Olá, digite seu salário mensal: "))
valor_emprestimo = float(input("Agora digite o valor que deseja pagar por mês na prestação do empréstimo: "))

if valor_emprestimo <= 20/100 * salario:
    print("Empréstimo Concedido!")

else:
    print("Empréstimo não concedido!")

    