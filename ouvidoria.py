reclamacao = []
while True:
    print("\nMenu de reclamação: ")
    print("\n1) Listagem de manifestação \n2) Criar uma nova manifestação \n3) Exibir quantidade de manifestação \n4) Pesquisar uma manifestação por código \n5) Sair do sistema")
    try:    
        opcao = int(input("\nDigite sua opção: "))

        if opcao == 1:
            print("\nLista das manifestação: ")
            if len(reclamacao) == 0:
                print("\nAinda não existe reclamações!")
            else:
                for i in range(len(reclamacao)):
                    print(f"Reclamação {i + 1})", reclamacao[i])
                    
        elif opcao == 2:
            print("\nCriar uma nova manifestação: ")
            novaReclamacao = input("\nInforme a sua reclamação: ")
            if len(novaReclamacao) == 0:
                print("Reclamação inválida!")
            else:
                reclamacao.append(novaReclamacao)
                print("\nReclamação cadastrada com sucesso!")
                for i in range(len(reclamacao)):
                    print(f"Aqui está o código da reclamação: {i + 1}")
                
        elif opcao == 3:
            print("\nQuantidade de reclamções: ")
            if len(reclamacao) > 0:
                print(f"Até o momento, o sistema possui exatas {len(reclamacao)} manifestação(ões)")
            else:
                print("Sem reclamações disponíveis no momento!")

        elif opcao == 4:
            codigoManifestacao = int(input("\nDigite o código da manifestação: "))
            if codigoManifestacao > 0 and codigoManifestacao <= len(reclamacao):
                reclamacaoPesquisada = reclamacao[codigoManifestacao-1]
                print("Resultado da pesquia: ")
                print(f"A manifestação pesquisada é: {reclamacaoPesquisada}")
            else:
                print("\nO código informado não remete a nehuma reclamação!")

        elif opcao == 5:
            print("\nVocê decidiu encerrar o programa!")
            break
        else: 
            print("Está opção não se encontra no menu, por favor, digite uma opção válida!")
    except ValueError:
        print("Digite apenas números!")
