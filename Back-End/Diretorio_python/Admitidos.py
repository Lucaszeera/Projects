documentos = ("Ficha de registro", "Contrato de trabalho", "Docs Diversos", "Sindicato Carta", "VT Opção", "EPI's", 'ASO', 'LGPD')

def adicionarAdmitido():
    funcionarios_docs = []
    dados = []
    print('Digite os 5 dados: Empresa, RE, Nome, Status e Data de admissão.')
    for j in range(0, 5):
        dado = input('--> ')
        dados.append(dado)

    for i in range(len(documentos)):
        dados.append(documentos[i])
        funcionarios_docs.append(dados)
        dados.pop()

    return funcionarios_docs

admitidos = adicionarAdmitido()

print(admitidos)
# for i in range(len(admitidos)):
#     for j in range(len(documentos)):
