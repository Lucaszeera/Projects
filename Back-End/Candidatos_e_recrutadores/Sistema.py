'''
Implementação em Python de um menu listando todas as funcionalidade do sistema. 
Observe que ao escolher uma opção, o programa deverá mostrar na tela a opção selecionada e exibir novamente o menu com todas as funcionalidades do sistema. 
Entregável: Arquivo py (Implementação em Python)

'''

            # Texto de bem vindo
welcome_text = """
-------------------------- IBMatch --------------------------
Seja bem vindo(a)! Escolha uma das opções abaixo para iniciar:
(1) Cadastro de recrutador
(2) Cadastro de candidato
(3) Verificar cadastros
(4) Consultar meus dados
(5) Sair
"""

            # Area de atuacao CANDIDATO
atuacao_can = """
Qual é a sua área de atuação? Digite o número correspondente a área:
(1) Tecnologia
(2) Humanas 
(3) Engenharia
(4) Economia e negócios
(5) Outra área
"""

            # Area de atuacao RECRUITER
atuacao_rec = """
Qual é sua área de recrutamento? Digite o número correspondente a área:
(1) Tecnologia
(2) Humanas 
(3) Engenharia
(4) Economia e negócios
(5) Outra área
"""

            # Array para tupla de recruiters e candidatos
recruiters = [[0, 'lucas', '@.', 'Tecnologia']]
candidatos = []
 # Opções do menu principal, enquanto o usuário nao escolher a opcao 5, ele nao saira do sistema #
def choose_number():
    option = int(input("Digite o número: "))
    if option == 1:
        print(str("Bem-vindo, recrutador!"))
        cad_recruiter()
    elif option == 2:
        print(str("Bem-vindo, candidato!"))
        cad_candidato()
    elif option == 3:
        lista_cadastro()
    elif option == 4:
        perfil()
    elif option == 5:
        iniciar = int(input("Sistema finalizado. Para iniciar novamente, tecle 1\n"))
        if iniciar == 1:
            welcome_system()
    else:
        print("Opcao inválida. Escolha entre 1 a 5")
        choose_number()


# Procedimento(1): cadastro do recrutador
def cad_recruiter():
    id_rec = len(recruiters) + len(candidatos)
    name_rec = str(input("Digite o seu nome completo: "))
    email_rec = str(input("Digite o seu email: "))
    if email_valido(email_rec):
        print(str(atuacao_can))
        area = int(input("Qual a área: "))
        area_rec = nome_area(area)
    else:
        print("Por favor, digite um email válido!")
        cad_recruiter()

    if name_rec != '' and email_rec != '' and area_rec != '':
        print("\nSEUS DADOS: \nId: " + str(id_rec + 1) + "\nNome: " + name_rec + "\nEmail: " + email_rec + "\nÁrea: " + str(area_rec))
        print(str("\nDigite: \n(1) Confirmar \n(2) Corrigir\n"))
        conf_corr = int(input("RESPONDA -> "))
        if conf_corr == 1:
            recruiters.append((id_rec, name_rec, email_rec, area_rec))
            print("Recrutador cadastrado com sucesso.")
            welcome_system()
        else:
            print(str("Corrija o seu cadastro:"))
            cad_recruiter()
    else:
        print(str("Cadastro não realizado. Todas as opções são obrigatórias"))
        cad_recruiter()

# Procedimento(2): cadastro do candidato
def cad_candidato():
    id_can = len(recruiters) + len(candidatos)
    name_can = str(input("Digite o seu nome completo: "))
    email_can = str(input("Digite o seu email: "))
    if email_valido(email_can):
        print(str(atuacao_can))
        area = int(input("Qual a área: "))
        area_can = nome_area(area)
    else:
        print("Por favor, digite um email válido!")
        cad_candidato()

    if name_can is not None and email_can is not None and area_can is not None:
        print("\nSEUS DADOS: \nId: " + str(id_can + 1) + "\nNome: " + name_can + "\nEmail: " + email_can + "\nÁrea: " + str(area_can))
        print(str("\nDigite: \n(1) Confirmar \n(2) Corrigir\n"))
        conf_corr = int(input("RESPONDA -> "))
        if conf_corr == 1:
            candidatos.append((id_can, name_can, email_can, area_can))
            print("Candidato cadastrado com sucesso.")
            welcome_system()
        elif conf_corr == 2:
            print(str("Corrija o seu cadastro:"))
            cad_candidato()
    else:
        print(str("Cadastro não realizado. Todas as opções são obrigatórias"))
        cad_candidato()

# Procedimento(3): Exibe todos os candidatos ou todos os recrutadores cadastrados
def lista_cadastro():
    listar = int(input("Voce é \n(1) Recrutador \n(2) Candidato \n"))
    if listar == 1:
        print("Recrutadores cadastrados:")
        if len(recruiters) != 0:
            print("\nRecruiters cadastrados:")
            for a in range(0, len(recruiters)):
                print(" \nId: " + str(recruiters[a][0] + 1) + "\nNome: " + str(recruiters[a][1]) + "\nEmail: " + str(recruiters[a][2]))
            welcome_system()
        else:
            print("Nenhum recrutador foi cadastrado.")
            welcome_system()
    elif listar == 2:
        if len(candidatos) != 0:
            print("\nCandidatos cadastrados:")
            for a in range(0, len(candidatos)):
                print(" \nId: " + str(candidatos[a][0] + 1) + "\nNome: " + str(candidatos[a][1]) + "\nEmail: " + str(
                    candidatos[a][2]))
            welcome_system()
        else:
            print("Nenhum candidato foi cadastrado.")
            welcome_system()
    else:
        print("Por favor, informe se você é um candidato ou recruiter!")
        lista_cadastro()


 # Procedimento(4): Mostra ao usuário seus dados ##
def perfil():
    id = (int(input("Digite seu id: ")) - 1)
    if id_valido(id):
        if qual_perfil(id) == 1:
            meus_dados(1, id)
        elif qual_perfil(id) == 2:
            meus_dados(2, id)
        else:
            print("Por favor, informe se você é recrutador ou candidato!")
            welcome_system()
    else:
        print('Por favor, informe um id válido!')
        welcome_system()


 ## Função que verifica se o usuário digitou um id existente ##
def id_valido(id):
    if len(candidatos) > 0 >= id or len(recruiters) > 0 >= id:
        return True
    return False

 ## Função que verifica se o id que o usuario digitou está na lista candidatos ou na lista recruiters ##
def qual_perfil(id):
    if id in recruiters:
        return 1
    return 2


 ## Função que retorna os dados individuais de um perfil, o usuario deve informar o id ##
def meus_dados(perfil, id):
    if perfil == 1:
        print("\nSEUS DADOS: \nId: " + str(recruiters[id][0] + 1) + "\nNome: " + str(recruiters[id][1]) + "\nEmail: " + str(recruiters[id][2]) + "\nÁrea: " + str(recruiters[id][3]))
    elif perfil == 2:
        print("\nSEUS DADOS: \nId: " + str(candidatos[id][0] + 1) + "\nNome: " + str(candidatos[id][1]) + "\nEmail: " + str(candidatos[id][2]) + "\nÁrea: " + str(candidatos[id][3]))
    welcome_system()


 ## função que valida a área do candidato ou recruiter, também retorna a area em string ##
def nome_area(opcao):
    if opcao == 1:
        area_can = 'Tecnologia'
    elif opcao == 2:
        area_can = 'Humanas'
    elif opcao == 3:
        area_can = 'Engenharia'
    elif opcao == 4:
        area_can = 'Economia e negócios'
    elif opcao == 5:
        area_can = str(input("Digite o nome da área: "))
    return area_can

 ## função que valida se o email do candidato ou recruiter contém "@" e "." (@seila.algo) ##
def email_valido(email):
    if '@' and '.' in email:
        return True
    return False

 ## Mostra as opcoes na tela e chama funcao de escolher o número ##
def welcome_system():
    print(str(welcome_text))
    choose_number()


welcome_system()
