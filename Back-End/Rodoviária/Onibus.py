janela = ['0']*24
corredor = ['0']*24
print('='*30)
print("Passagens de ônibus")
print('='*30)
while True:
    menu = int(input("\n----- O que deseja? ----- " #Mostra o menu principal
      "\n1- Comprar passagem"
      "\n2- Cancelar compra"
      "\n3- Mostrar mapa de ocupação"
      "\n4- Sair"
      "\n-->"))

    if menu < 1 or menu > 4:  #Valida se a opção que o usuário digitou no menu são válidas
        print("Opção inválida. digite novamente")
        continue
    elif menu == 1: #Opção 1: comprar passagem
        if '0' not in janela and '0' not in corredor: #se não tiver assentos disponíveis
            print("O ônibus está lotado, sinto muito.\n")
            continue
        opcao = int(input("Você deseja um assento na janela ou corredor?"
                       "\n1- Janela"
                       "\n2- Corredor"
                       "\n-->"))
        if opcao < 1 or opcao > 2: #se o usuario não digitar 1 ou 2, a opção é inválida
            print("Opção inválida, tente novamente.")
            continue
        poltrona = int(input("Escolha uma poltrona de 1 a 24: "))
        if poltrona < 1 or poltrona > 24: #Se o usuario não digitar uma poltrona de 1 até 24, a opção é inválida
            print("Opção inválida, tente novamente.")
            continue
        elif opcao == 1 and janela[poltrona-1] == '0': #Se o usuário quer reservar um assento da JANELA, e ele estiver DESOCUPADO
            print("Venda realizada com sucesso!")
            del janela[poltrona-1]
            janela.insert(poltrona-1, '1')
        elif opcao == 1 and janela[poltrona-1] == '1': #Se o usuário quer reservar um assento da JANELA, e ele estiver OCUPADO
            print('Poltrona ocupada. Venda não realizada!')
        elif opcao == 2 and corredor[poltrona-1] == '0': #Se o usuário quer reservar um assento do CORREDOR, e ele estiver DESOCUPADO
            print("Venda realizada com sucesso!")
            del corredor[poltrona - 1]
            corredor.insert(poltrona-1, '1')
        elif opcao == 2 and corredor[poltrona-1] == '1': #Se o usuário quer reservar um assento do CORREDOR, e ele estiver OCUPADO
            print('Poltrona ocupada. Venda não realizada!')

    elif menu == 2:
        if '1' not in janela or '1' not in corredor: #Se o ônibus está vazio, então não é possível cancelar passagens
            print("O ônibus está vazio, não é possivel cancelar uma passagem.")
            continue
        opcao = int(input("O assento se localiza no corredor ou na janela?"
                      "\n1- janela"
                      "\n2- corredor"
                      "\n-->"))
        if opcao < 1 or opcao > 2: # se o usuário nao digitar 1 ou 2, a opção é inválida
            print("Informação inválida, digite novamente.")
            continue
        poltrona = int(input("Digite o numero da poltrona: "))
        if poltrona < 1 or poltrona > 24: #Se o usuário não digitar o número do assento de 1 a 24, a informação é inválida
            print("Informação inválida, digite novamente.")
            continue
        elif opcao == 1 and janela[poltrona-1] == '1': # Se o usuário quer cancelar um assento da JANELA, e o assento estiver OCUPADO
            del janela[poltrona-1]
            janela.insert(poltrona-1, '0')
            print("Compra cancelada com sucesso!")
        elif opcao == 1 and janela[poltrona-1] == '0': # Se o usuário quer cancelar um assento da JANELA, e o assento estiver DESOCUPADO
            print("A poltrona selecionada já está livre, compra não cancelada!")
        elif opcao == 2 and corredor[poltrona-1] == '1': # Se o usuário quer cancelar um assento do CORREDOR, e o assento estiver OCUPADO
            del corredor[poltrona-1]
            corredor.insert(poltrona-1, '0')
            print("Compra cancelada com sucesso!")
        elif opcao == 2 and corredor[poltrona-1] == '0': # Se o usuário quer cancelar um assento do CORREDOR, e o assento estiver DESOCUPADO
            print("A poltrona selecionada já está livre, compra não cancelada!")

    elif menu == 3:
        print(f'Mapa dos assentos no ônibus:' #Exibe um "mapa" das posições livres e ocupadas no ônibus
                  f'\nJanela:', '%62s' % (f'{janela[:12]}'),
                  f'\nCorredor: {corredor[:12]}',
                  f'\nCorredor: {corredor[12:24]}',
                  f'\nJanela:', '%62s' % (f'{janela[12:24]}'))

            ## alternativa para mostrar por extenso, o número do assento e o estado
        # for a in range(len(janela)):
        #     if janela[a] == '0':
        #         print(a+1, 'Livre')
        #     elif janela[a] == '1':
        #         print(a+1, 'Ocupada')
        #
        # print("---Corredor---")
        # for b in range(len(janela)):
        #     if corredor[b] == '0':
        #         print(b+1, 'Livre')
        #     elif corredor[b] == '1':
        #         print(b+1, 'Ocupada')
    elif menu == 4:
        print("Volte sempre!")
        break
