
print('\n"3.6 Até 2020, reduzir pela metade as mortes e os ferimentos globais por acidentes em estradas.'
      '\n No Brasil, em 2015 ocorreu 19 mortes de trânsito para cada 100 mil habitantes.'
      '\n Em 2019, a taxa reduziu para 15 mortes para cada 100 mil habitantes, mas ainda longe da meta da ODS."\n')

lista_de_registros = [{'mes_ano_referencia':'01-2022', 'total_habitantes':100000, 'total_obitos':9},
                      {'mes_ano_referencia':'02-2022', 'total_habitantes':110000, 'total_obitos':12},
                      {'mes_ano_referencia':'03-2022', 'total_habitantes':130000, 'total_obitos':15},
                      {'mes_ano_referencia':'04-2022', 'total_habitantes':160000, 'total_obitos':17},
                      {'mes_ano_referencia':'05-2022', 'total_habitantes':180000, 'total_obitos':20},
                      {'mes_ano_referencia':'06-2022', 'total_habitantes':210000, 'total_obitos':24},
                      {'mes_ano_referencia':'07-2022', 'total_habitantes':250000, 'total_obitos':28},
                      {'mes_ano_referencia':'08-2022', 'total_habitantes':290000, 'total_obitos':33},
                      {'mes_ano_referencia':'09-2022', 'total_habitantes':340000, 'total_obitos':36},
                      {'mes_ano_referencia':'10-2022', 'total_habitantes':420000, 'total_obitos':40}]

menu_principal = ''' ------ Menu Principal ------
1 - Cadastrar mês de referência
2 - Exibir dados do mês de referência (pesquisa por mês)
3 - Relatório comparativo 
4 - Listar todos os meses cadastrados
'''

def funcoes_principais():
    print(menu_principal)
    opcao = int(input("Digite a opção desejada: "))
    while opcao > 0 < 5:
        if opcao == 1:
            print("\nCADASTRANDO MÊS-ANO DE REFERÊNCIA")
            mes_ano = input("Digite o mês e o ano (mm-aaaa): ")
            total_habitantes = int(input("Digite o total de habitantes: "))
            total_obitos = int(input("Digite o total de óbitos: "))
            lista_de_registros.append({'mes_ano_referencia':mes_ano, 'total_habitantes':total_habitantes, 'total_obitos':total_obitos})
            print("***** Gravado com sucesso *****")
            continuar_ou_voltar = input("\nDeseja cadastrar outro mês-ano? (S/N): ").upper()
            if 'S' in continuar_ou_voltar:
                continue
            else:
                pass
        elif opcao == 2:
            print("\nCONSULTANDO MÊS-ANO DE REFERÊNCIA")
            mes_ano = input("Digite o mês e o ano (mm-aaaa): ")
            contador = 0
            if len(lista_de_registros) > 0:
                while contador <= len(lista_de_registros) - 1:
                    if mes_ano in lista_de_registros[contador]['mes_ano_referencia']:
                        print(f"Data do registro: {lista_de_registros[contador]['mes_ano_referencia']}\n"
                              f"Total de habitantes: {lista_de_registros[contador]['total_habitantes']}\n"
                              f"Total de óbitos: {lista_de_registros[contador]['total_obitos']}")
                        print("\n***** Registro encontrado *****")
                        break
                    else:
                        if contador == len(lista_de_registros) - 1:
                            print("\nEsse registro ainda não foi cadastrado.\n")
                    contador += 1

        elif opcao == 3:
            print("\nRELATÓRIO COMPARATIVO DE TAXA DE MORTALIDADE ANUAL\n")
            ano_comparar = input("Digite o ano a ser comparado: ")
            ano_total_habitantes, ano_total_obitos, ano_taxa_100k = pegar_tudo_em_um_ano(ano_comparar, lista_de_registros)
            taxa_2019 = 15.0
            diferenca = comparar_2_anos(float(ano_taxa_100k), taxa_2019)
            print("Ano: {}\nTotal de habitantes: {}\nTotal de óbitos: {}\nTaxa por 100k habitantes - 2021: {:.2f}".format(int(ano_comparar), ano_total_habitantes, ano_total_obitos, float(ano_taxa_100k)))
            print("Taxa por 100k habitantes - 2019: 15.00\n"
                  f"\nComparativo % entre {ano_comparar} e 2019: {diferenca}")
        elif opcao == 4:
            print("\nTODOS OS RELATORIOS REGISTRADOS\n")
            print(f"Ano: {lista_de_registros}")


        print(menu_principal)
        opcao = int(input("Digite a opção desejada: "))

def pegar_tudo_em_um_ano(ano, lista_de_registros):
    total_habitantes = 0
    total_obitos = 0
    taxa_por_100k = 0
    contador = 0
    if len(lista_de_registros) > 0:
        while contador <= len(lista_de_registros) - 1:
            if ano in lista_de_registros[contador]['mes_ano_referencia'][2:]:
                total_habitantes += lista_de_registros[contador]['total_habitantes']
                total_obitos += lista_de_registros[contador]['total_obitos']
                taxa_por_100k += total_obitos / 100 / (total_habitantes // 100000 )
            contador += 1
        return total_habitantes, total_obitos, taxa_por_100k

def comparar_2_anos(taxa1, taxa2019):
    if taxa1 > taxa2019:
        resposta = ("+{:.2f}%".format(taxa1 / taxa2019 * 1000))
    else:
        resposta = ("-{:.2f}%".format(taxa1 / taxa2019 * 1000))
    return resposta

## Inicialização ##

funcoes_principais()