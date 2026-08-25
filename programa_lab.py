import os 
from datetime import datetime
import pandas as pd
import kits

Nome_Arquivo_excel = 'Gerenciamento_lab.xlsx'

mapeamento_menu ={
    '1':  ('colesterol', 'ponto final'),
    '2':  ('magnesio', 'ponto final'),
    '3':  ('glicose', 'ponto final'),
    '4':  ('hemoglobina', 'ponto final'),
    '5':  ('fosforo', 'ponto final'),
    '6':  ('proteinas totais', 'ponto final'),
    '7':  ('bilirrubina', 'especial'),
    '8':  ('acido urico', 'ponto final'),
    '9':  ('colesterol HDL', 'ponto final'),
    '10': ('albumina', 'ponto final'),
    '11': ('calcio', 'ponto final'),
    '12': ('ureia', 'cinetico'),
    '13': ('Triglicerides', 'ponto final'),
    '14': ('Lactato enzimatico', 'ponto final'),
    '15': ('ferro_serico', 'especial'),
    '16': ('LDH', 'especial'),
    '17': ('gama_GT', 'especial'),
    '18': ('Fosfatase Alcalina', 'ponto final'),
    '19': ('fosfatase_alcalina_DGKC', 'especial')
}
def inicializar_sistema():
    if not os.path.exists(Nome_Arquivo_excel):
        estoque_inicial = {
            'colesterol': 5, 'magnesio': 6, 'glicose': 8,
            'hemoglobina': 4, 'fosforo': 3, 'proteinas totais': 5,
            'bilirrubina': 6, 'acido urico': 4, 'colesterol HDL': 3,
            'albumina': 6, 'calcio': 1, 'ureia': 1, 'Triglicerides': 2,
            'Lactato enzimatico': 3, 'ferro_serico': 2, 'LDH': 3, 'gama_GT': 2,
            'Fosfatase Alcalina': 4, 'fofatase_alcalina_DGKC': 2
        }
        df_estoque= pd.DataFrame(list(estoque_inicial.items()), columns=['Kits','Estoque'])
        df_resultados = pd.DataFrame(columns= ['Data/Hora', 'Aluno', 'Absorbância teste', 'Absorbância padrão', 'Resultado', 'unidade', 'Classificação'])
        with pd.ExcelWriter(Nome_Arquivo_excel, engine= 'openpyxl') as writer:
            df_estoque.to_excel(writer, sheet_name='Estoque', index=False)
            df_resultados.to_excel(writer, sheet_name='Resultados', index=False)
        print('Arquivo Excel inicializado com sucesso!')

def carregar_estoque():
    df_estoque = pd.read_excel(Nome_Arquivo_excel, sheet_name='Estoque')
    #transforma o DataFrame de volta em um dicionário para facilitar a manipulação
    return dict(zip(df_estoque['Kits'], df_estoque['Estoque']))

def salvar_dados(dados_exame, estoque_kits):
    #Atualiza tanto o estoque quanto os dados de uma vez só
    dados_exame['Data/Hora'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    df_novo_resultado = pd.DataFrame([dados_exame])
    try:
        df_estoque= pd.DataFrame(list(estoque_kits.items()), columns= ['Kits' , 'Estoque'])
        df_resultados_existentes = pd.read_excel(Nome_Arquivo_excel, sheet_name='Resultados')
        #concatena os exames novos e antigos 
        df_resultados_atualizados = pd.concat([df_resultados_existentes, df_novo_resultado], ignore_index=True)
        with pd.ExcelWriter(Nome_Arquivo_excel, engine='openpyxl') as writer:
            df_estoque.to_excel(writer, sheet_name='Estoque', index=False)
            df_resultados_atualizados.to_excel(writer, sheet_name='Resultados', index=False)
        print(f'\nDados salvos no arquivo {Nome_Arquivo_excel} com sucesso')
    except PermissionError:
        print(f'ERRO!!! O arquivo {Nome_Arquivo_excel} está aberto no excel, por favor feche-o e refaça a operação para não perder dados')


def menu_principal():
    inicializar_sistema()
    while True:
        print('-='*40)
        print(f'{"Bem vindo ao programa de testes bioquímicos":^40}')
        print('-='*40)
        print('1-colesterol total           2-Magnésio                 3-Glicose')
        print('4-Hemoglobina                5-Fósforo                  6-Proteínas Totais')
        print('7-Bilirrubina                8-Ácido Úrico              9-Colesterol HDL')
        print('10-Albumina                  11-cálcio                  12-ureia')
        print('13-Triglicerides             14-Lactato enzimatico      15-ferro serico')
        print('16-LDH                       17-gama_GT                 18-Fosfatase Alcalina')
        print('19-fosfatase_alcalina_DGKC   20-Sair do programa')
    
        print('-='*40)

        opcao = input('Selecione o exame realizado: ').strip()

        if opcao == '20':
            print('Saindo do programa...')
            break
        if opcao not in mapeamento_menu:
            print('opção invalida, tente novamente !')
            continue
        nome_kit, tipo_teste = mapeamento_menu[opcao]
        dados_resultado= None 
        #execução modular, dependendo também da categoria do exame
        if tipo_teste == 'ponto final':
            dados_resultado, estoque_atualizado= kits.executar_teste_padrao(nome_kit)
        elif tipo_teste == 'cinetico':
            dados_resultado, estoque_atualizado= kits.executar_teste_cinetico(nome_kit)
        elif tipo_teste == 'especial':
            dados_resultado, estoque_atualizado= getattr(kits, nome_kit)()

        if dados_resultado:
            salvar_dados(dados_resultado, estoque_atualizado)
            print('\n === Resumo do Laudo ===:')
            for chave, valor in dados_resultado.items():
                print(f'{chave}: {valor}')
if __name__ == '__main__':
    menu_principal()


