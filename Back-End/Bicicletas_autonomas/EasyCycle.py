#Equipe: Grupo 2
# rm94013: Lucas Costa
# rm94260: João Pedro
# rm94700: Kauan Altino
# rm95434: Gabriel Cerqueira

import datetime
import string
import random
import time

'''
MVP da solução global: bicicletas autônomas
'''

boas_vindas = '''
*                         Seja bem vindo ao EasyCycles!                          *
*       Fornecemos bicicletas autônomas para locomoção fácil e ecológica         *
----------------------------------------------------------------------------------
'''

menu_logar_ou_cadastrar = '''
        Inicie uma sessão ou cadastre-se        
1 - Cadastrar
2 - Login
'''

menu_servicos = '''
1 - Utilizar transportes Easy-bike
2 - Visualizar tempo restante
3 - Adicionar tempo
4 - Alterar meus dados
5 - Informações do serviço Easy-cycle
6 - Encerrar sessão
'''

descricoes_servicos = '''
*****************************************************************************************************************
\nNossa plataforma oferece um sistema de aluguel de bicicletas para fácil locomoção das pessoas.
\n-A ideia é que todos que forem cadastrados na plataforma, com seus dados preenchidos corretamente e confirmados,
têm direito a utilizar as Easy-bikes por um periodo.
\n-As Easy-bikes vieram para facilitar o acesso aos passageiros, suprimir a poluição de automóveis movidos à
combustiveis poluentes e oferecer um serviço mais em conta.\n 
\n-Ao cadastrar-se na plataforma você tem acesso à 4 serviços: 
\n1- Utilizar easy-bikes (Uma Easy-bike virá até você e você poderá pedalar pelo tempo que informar)
\n2- Vizualiar tempo restante (após reservar você pode olhar o tempo restante da reserva)
\n3- Adicionar tempo (Se seu tempo esgotar, você pode ir na plataforma e adicionar mais alguns minutos)
\n4- Alterar dados (Você poderá mudar seu email ou senha)
*****************************************************************************************************************
'''

usuarios = [{'id':'admin', 'senha':'admin', 'email':'admin@easycycle.com', 'rg':'08101054383'}]
qtd_bicicletas = 3
modelos = ('PADRAO', 'ARO 20', 'ESPECIAL')
momento_reserva = datetime.datetime(2000, 12, 12, 00, 00)

def start_system():
    print(menu_logar_ou_cadastrar)
    opcao = int(input("Digite a opção: "))
    cadastro_ou_login(opcao)

def cadastro_ou_login(login_opcao):
        #Cadastrar
    if login_opcao == 1:
        cadastrar()
        start_system()
        #Fazer Login
    elif login_opcao == 2:
        id_login = input("Digite o seu id: ")
        senha_login = input("Digite sua senha: ")

        for a in range(0, len(usuarios)):
            if id_login == usuarios[a]['id'] and senha_login == usuarios[a]['senha']:
                print("\nVocê está logado na plataforma!")
                    # USUARIO ESTÁ LOGADO #
                operar_servicos(id_login)
                break
            elif a == len(usuarios) - 1:
                print("\nUsuario ou senha incorretos, tente de novo!\n")
                cadastro_ou_login(2)

def operar_servicos(id):
    hora_reserva = datetime.datetime(2000, 12, 12, 00,00,00)
    tempo_contador = 0
    print(menu_servicos)
    opcao = int(input('Digite a opção: '))
    while opcao < 7:
        if opcao == 1:
                #Utilizar transportes Easy-bike
            hora_reserva, tempo_contador = reservar_bicicleta()
        elif opcao == 2:
                #Vizualizar tempo restante
            visualizar_tempo_restante(hora_reserva, tempo_contador)
        elif opcao == 3:
                #Adicionar tempo
            adicionar_tempo(hora_reserva, tempo_contador)
        elif opcao == 4:
                #Alterar meus dados
            alterar_dados(id, usuarios)

        elif opcao == 5:
                #informações do serviço Easy-cycle
            print(descricoes_servicos)
            time.sleep(1)
            print(".", end="")
            time.sleep(1.5)
            print(".", end="")
            time.sleep(1.5)
            print(".")
            time.sleep(1.5)
        elif opcao == 6:
            start_system()
        print(menu_servicos)
        opcao = int(input('Digite a opção: '))

def reservar_bicicleta():
    if qtd_bicicletas <= 0:
        print("\nTodas as bicicletas estão ocupadas no momento, por favor tente novamente mais tarde.\n")
        operar_servicos()
    else:
        especial = input("\nPrecisa de um modelo de Easy-bike menor ou especial?(S/N)\n -  ").upper()
        if "N" in especial or "NAO" in especial:
            modelo = modelos[0]
        elif "S" in especial or "SIM" in especial:
            print("\nEscolha o modelo ideal para você\n")
            qual_modelo = input("1 - Modelo pequeno, para crianças ou pessoas de baixa estatura\n"
                         "2 - Modelo especial, tricíclo para pessoas com deficiencia ou qualquer dificuldade em equilíbrio\n - ")
            if qual_modelo == '1':
                modelo = modelos[1]
            elif qual_modelo == '2':
                modelo = modelos[2]
            else:
                print("Por favor, digite uma opção válida.")
                reservar_bicicleta()

        endereco = input("Informe o endereço à esperar pela easy-bike\n - ")

        print("Deseja reservar por quanto tempo? ( O tempo contará quando a easy-bike chegar à sua localização )"
              "\n1 -  0     ~ 30 min: R$0.80 > 10 min"
              "\n2 - 30 min ~ 1 hora: R$0.60 > 10 min"
              "\n3 - 1 hora ~ 2 hrs:  R$0.55 > 10 min"
              "\n4 - 2 horas  ++:     R$0.50 > 10 min")
        opcao = int(input(" --> "))
        if opcao == 1:
            tempo_contador = 30
        elif opcao == 2:
            tempo_contador = 60
        elif opcao == 3:
            tempo_contador = 120
        else:
            print("Por favor, digite uma opção válida.")
            reservar_bicicleta()
        momento_reserva = datetime.datetime.now()
        print("\nA reserva foi feita em: " + momento_reserva.strftime("%H:%M"))
        time.sleep(1)
        print(".", end="")
        time.sleep(0.7)
        print(".", end="")
        time.sleep(0.7)
        print(".")
        time.sleep(0.4)
        print(f"\nCerto, permaneça no local informado, a Easy-bike {modelo} chegará em 10 minutos no endereço: {endereco}"
              f", você terá {tempo_contador} minutos para pedalar!"
              f"\nCaso o tempo esgote, você pode entrar na plataforma e adicionar mais tempo")
        return momento_reserva, tempo_contador

def visualizar_tempo_restante(momento_reserva, tempo_contador):
    if momento_reserva == datetime.datetime(2000, 12, 12, 00,00,00):
        print("Não há nenhuma reserva pendente no momento!")
    else:
        hora_final = momento_reserva + datetime.timedelta(minutes= tempo_contador)
        print("Você tem até " + hora_final.strftime('%H:%M') + " para pedalar, aproveite!")

def adicionar_tempo(momento_reserva, tempo_contador):
    tempo_contador += int(input("Quantos minutos deseja adicionar: "))
    visualizar_tempo_restante(momento_reserva, tempo_contador)

def alterar_dados(id_logado, usuarios):
    s_n_email = input("Deseja alterar o email? (S/N)\n - ").upper()
    if "S" in s_n_email or "SIM" in s_n_email:
        email_novo = input("Digite seu novo email\n - ")
        contador = 0
        if len(usuarios) > 0:
            while contador <= len(usuarios) - 1:
                if id_logado in usuarios[contador]['id']:
                    usuarios[contador]['email'] = email_novo
                contador += 1

    s_n_senha = input("Deseja alterar a senha? (S/N)\n - ").upper()
    if "S" in s_n_senha or "SIM" in s_n_senha:
        senha_nova = input("Digite sua nova senha (mínimo: 8 caracteres)\n - ")
        contador = 0
        if len(usuarios) > 0:
            while contador <= len(usuarios) - 1:
                if id_logado in usuarios[contador]['id']:
                    usuarios[contador]['senha'] = senha_nova
                contador += 1
    if s_n_email != 'N' or s_n_senha != 'N':
        print('\nDados alterados com sucesso!\n')
    else:
        print('\nNenhum dado informado, então não houve alterações.\n')

def cadastrar():
    email_usuario = input("Digite seu email: ")
    if '@' not in email_usuario or '.' not in email_usuario:
        print("\nPor favor, Digite um email válido.\n")
        cadastrar()
    senha_usuario = input("Digite sua senha (mínimo: 8 caracteres): ")
    if len(senha_usuario) < 8:
        print("\nSua senha deve ter pelo menos 8 caracteres!\n")
        cadastrar()
    login_usuario = gerar_login(usuarios)
    usuario = {'id':login_usuario, 'senha':senha_usuario, 'email':email_usuario}
    print('\nID do usuario: ', usuario['id'])

    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!\n")

def gerar_login(lista_usuarios):
    novo_login = ''.join(random.choice(string.ascii_lowercase) + random.choice(string.digits) for a in range(3)) #gera um login de 6 caracteres, contendo letras minusculas e numeros

    contador = 0
    if len(lista_usuarios) > 0:
        while contador <= len(lista_usuarios) - 1:
            if novo_login in lista_usuarios[contador]['id']:
                gerar_login(lista_usuarios)
            else:
                if contador == len(lista_usuarios) - 1:
                    return novo_login
            contador += 1
    else:
        return novo_login

    #SISTEMA#
print(boas_vindas)

start_system()