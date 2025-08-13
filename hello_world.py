print("1. Cadastrar Conta")
print("2. Cadastrar Movimentacao")
print("3. Sair")

opcao = 0

while opcao != 3:
    try:
        opcao = int(input("Digite sua opcao: "))
        if opcao == 1:
            name = input("Coloque seu nome: ")
            idade = int(input("Coloque sua idade (Ex: 1, 2, 15, 18, 68): "))
            if idade <= 18:
                idade = int(input("Idade invalida, tem que ser +18: "))
            elif idade >= 18:
                print("Deu certo")
    
        elif opcao == 2:
            print("Movimentação Concluida")
            
        elif opcao == 3:
            print("3. Sair")  

        else:
            print("Opção inválida. Por favor, digite.")    
    except ValueError:
        # Esta parte lida com entradas que não são números, como letras ou palavras.
        print("Entrada inválida. Por favor, digite um número....: 5")
 
print("Fim do programa.")