import os 
from datetime import datetime
import pandas as pd
import kits

Nome_Arquivo_excel = 'Gerenciamento_lab.xlsx'

def inicializar_sistema():
    estoque_kits = {
    'colesterol': 5,
    'magnesio': 6,
    'glicose': 8,
    'hemoglobina': 4,
    'fosforo': 3,
    'proteinas totais': 5, 
    'bilirrubina': 6,
    'acido urico': 4,
    'colesterol HDL': 3,
    'albumina': 6,
    'cálcio': 1
    }
    if not os.path.exists(Nome_Arquivo_excel):
        # cria o DataFrame do estoque com os kits e suas quantidades
        df_estoque = pd.DataFrame(list(estoque_kits.items()), columns=['Kit', 'Estoque'])
        # cria a tabela de resultados com as colunas especificadas, mas sem dados
        df_resultados = pd.DataFrame(columns=['Data/Hora'])
        
        #salva ambas no mesmo arquivo excel, mas em abas diferentes
        with pd.ExcelWriter(Nome_Arquivo_excel) as writer:
            df_estoque.to_excel(writer, sheet_name='Estoque', index=False)
            df_resultados.to_excel(writer, sheet_name='Resultados', index=False)

def carregar_estoque():
    df_estoque = pd.read_excel(Nome_Arquivo_excel, sheet_name='Estoque')
    #transforma o DataFrame de volta em um dicionário para facilitar a manipulação
    return dict(zip(df_estoque['Kit'], df_estoque['Estoque']))

def salvar_estoque_atualizado(estoque_kits):
    df_estoque = pd.DataFrame(list(estoque_kits.items()), columns=['Kit', 'Estoque'])
    with pd.ExcelWriter(Nome_Arquivo_excel, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        df_estoque.to_excel(writer, sheet_name='Estoque', index=False)
  
def salvar_no_excel(dados_exames):
    ''' terá por função receber os dados obtidos do return, adicionar data/hora e adiciona ao excel '''
    dados_exames['Data/Hora'] = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    df_novo=pd.DataFrame([dados_exames])

    colunas = ['Data/Hora'] + [col for col in dados_exames.keys() if col != 'Data/Hora']
    df_novo = df_novo[colunas]

    df_existente = pd.read_excel(Nome_Arquivo_excel, sheet_name='Resultados')
    df_atualizado = pd.concat([df_existente, df_novo], ignore_index=True)

    with pd.ExcelWriter(Nome_Arquivo_excel, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
        df_atualizado.to_excel(writer, sheet_name='Resultados', index=False)
    print(f'Dados salvos no arquivo {Nome_Arquivo_excel} com sucesso!')


def menu_principal():
    while True:
        print('-='*40)
        print(f'{"Bem vindo ao programa de testes bioquímicos":^40}')
        print('-='*40)
        print('1-colesterol total           2-Magnésio                 3-Glicose')
        print('4-Hemoglobina                5-Fósforo                  6-Proteínas Totais')
        print('7-Bilirrubina                8-Ácido Úrico              9-Colesterol HDL')
        print('10-Albumina                  11-cálcio                  12-Sair do programa')
        print('-='*40)

        opcao = input('Selecione o exame realizado: ').strip()
        dados_resultado = None
        if opcao == '1':
            dados_resultado, estoque_atualizado = kits.colesterol()
        elif opcao == '2':
            dados_resultado, estoque_atualizado = kits.magnesio()
        elif opcao == '3':
            dados_resultado, estoque_atualizado = kits.glicose()
        elif opcao == '4':
            dados_resultado, estoque_atualizado = kits.hemoglobina()
        elif opcao == '5':
            dados_resultado, estoque_atualizado = kits.fosforo()
        elif opcao == '6':
            dados_resultado, estoque_atualizado = kits.proteinas_totais()
        elif opcao == '7':
            dados_resultado, estoque_atualizado = kits.bilirrubina()
        elif opcao == '8':
            dados_resultado, estoque_atualizado = kits.acido_urico()
        elif opcao == '9':
            dados_resultado, estoque_atualizado = kits.colesterol_hdl()
        elif opcao == '10':
            dados_resultado, estoque_atualizado = kits.albumina()
        elif opcao == '11':
            dados_resultado, estoque_atualizado = kits.calcio()
        elif opcao == '12':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')
            continue

        if dados_resultado:
            salvar_no_excel(dados_resultado)
            salvar_estoque_atualizado(estoque_atualizado)
            print('\n === Resumo do Laudo ===:')
            for chave, valor in dados_resultado.items():
                print(f'{chave}: {valor}')


