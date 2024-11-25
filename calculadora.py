while True:
    #Esse é o menu de operações a ser realizado
    print("================== CALCULADORA ==================\n")
    print("Escolha uma operação:\n")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("\n0 - SAIR")
    print("\n=================================================")

    #Input de qual operação o usuário deseja realizar
    operacao = int(input("Digite o número da operação desejada: "))

    #Condição para determinar qual operação será realizada
    if operacao in (1,2,3,4):

        n1 = float(input("Insira o primeiro número: ")) #Solicito os números para realizar a operação e já convertendo os números para float
        n2 = float(input("Insira o segundo número: "))

        if operacao == 1:
            print("\nO resultado da soma é: ", n1 + n2)
            voltar = input("\nAperte Enter para voltar para a calculadora\n") #Input utilizado para que o usuário veja bem o resultado antes de voltar para a calculadora

        elif operacao == 2:
            print("\nO resultado da subtração é: ", n1 - n2)
            voltar = input("\nAperte Enter para voltar para a calculadora\n")

        elif operacao == 3:
            print("\nO resultado da multiplicação é: ", n1 * n2)
            voltar = input("\nAperte Enter para voltar para a calculadora\n")
        
        elif operacao == 4:
            if  n2 == 0:
                print("\nDivisão por zero não é permitida.\nVoltando para o menu da calculadora...") #Na matematica nenhum número pode ser divisivel por 0
            else:
                print("\nO resultado da divisão é: ", n1 / n2)
                voltar = input("\nAperte Enter para voltar para a calculadora\n")

    elif operacao == 0: #Condição para encerrar o looping do menu de operação
        print("Obrigado por utilizar o programa!")
        break

    else:
        print("Número de operação inválida!\n") #Caso o número escolhido seja diferente das opções ele emite essa mensagem

    

#Pensei em utilizar funções para criar a calculadora, mas vou seguir de acordo com o que for passando nos conteúdos!