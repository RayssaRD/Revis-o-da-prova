'''7.	Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1 - Soma de 2 números
2 - Diferença entre 2 números (maior pelo menor)
3 - Produto entre 2 números
4 - Divisão entre 2 números (o denominador não pode ser zero)
Opção:'''
opcao = int(input("Digite o número da operação desejada: \n 1 - Soma de 2 números \n 2 - Diferença entre 2 números (maior pelo menor) \n 3 - Produto entre 2 números \n 4 - Divisão entre 2 números (o denominador não pode ser zero) \n"))

if opcao == 1:
    print("Você escolheu somar dois números!")
    numero1 = float(input("digite um número: "))
    numero2 = float(input("digite um número: "))
    print(f"a soma dos números {numero1} e {numero2} é {numero1 + numero2}")

elif opcao ==2 :
    print("Você escolheu saber a diferença entre 2 números!")
    numero1 = float(input("digite um número: "))
    numero2 = float(input("digite um número: "))
    if numero1 > numero2 :
        print(f"a diferença dos números {numero1} e {numero2} é {numero1 - numero2}")
    else:
        print("Erro! Tente novamente!")

elif opcao == 3:
    print("Você escolheu multiplicar dois números!")
    numero1 = float(input("digite um número: "))
    numero2 = float(input("digite um número: "))
    print(f"a soma dos números {numero1} e {numero2} é {numero1 * numero2}")

elif opcao ==4 :
    print("Você escolheu saber a divisão entre 2 números!")
    numero1 = float(input("digite um número: "))
    numero2 = float(input("digite um número: "))
    if numero2 ==0 :
        print(f"O denominador não pode ser 0")
    else:
        print(print(f"a divisão dos números {numero1} e {numero2} é {numero1 / numero2}"))

else:
    print("Número inválido")