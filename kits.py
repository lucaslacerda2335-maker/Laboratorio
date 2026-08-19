
import programa_lab
from time import sleep 
kits=['colesterol', 'magnesio', 'glicose', 'hemoglobina', 'fosforo', 'proteinas totais', 
      'bilirrubina', 'acido urico', 'colesterol HDL', 'albumina', 'calcio', 'ureia']
#Mapeamento dos testes com seus fatores, unidades e faixa de referência
conf_testes ={
    'colesterol':{
        'fator': 200.0,
        'unidade':'mg/dL',
        'intervalo': [(200.0, 'Desejável'), (239.0, 'Limítrofe'), (float('inf'), 'Elevado')]
    },
    'magnésio':{
        'fator': 2.0,
        'unidade':'mg/dL',
        'intervalo': [(1.7,'Abaixo do desejável'), (2,6, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'glicose':{
        'fator': 100.0,
        'unidade': 'mg/dL',
        'intervalo': [(64.9, 'Valores abaixo do desejável (hipoglicemia)'), (99.0, 'Desejável'), (125.0, 'Limitrofe'), (float('inf'), 'Valores elevados (hiperglicemia)')]
    },
    'hemoglobina':{
        'fator': 10.0,
        'unidade': 'g/dL',
        'intervalo':[(11.9, 'Valores abaixo do IR (anemia)'), (16.0, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'fosforo':{
        'fator': 5.0,
        'unidade':'mg/dL',
        'intervalo':[(2.4, 'Valores abaixo do IR'), (4.5, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'proteinas totais':{
        'fator': 4.0,
        'unidade': 'g/dL',
        'intervalo':[(5.9, 'Valores abaixo do IR'), (8.3, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'acido urico':{
        'fator': 6.0,
        'unidade':'mg/dL',
        'intervalo': [(3.49, 'Valores abaixo do IR'), (7.2, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'colesterol HDL':{
        'fator': 40.0,
        'unidade': 'mg/dL',
        'intervalo': [(39.9, 'Valores abaixo do IR'), (60.0, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'albumina':{
        'fator': 3.8,
        'unidade':'g/dL',
        'intervalo':[(3.49, 'Valores abaixo do IR'), (5.5, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'calcio':{
        'fator': 10.0,
        'unidade': 'mg/dL',
        'intervalo':[(8.79, 'Valores abaixo do IR'), (11.0, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'ureia':{
        'fator': 70.0,
        'unidade': 'mg/dL',
        'intervalo':[(14.9, 'Valores abaixo do IR'), (45.0, 'Desejável'), (float('inf'), 'Elevado')]
    }
}

tipo_teste=['teste', 'padrão']
tipo_teste2=['teste1', 'teste2', 'padrão1', 'padrão2']
def estoque(nome_kit):
    estoque_kits = programa_lab.carregar_estoque()
    qtd_atual = estoque_kits.get(nome_kit, 0)
    print(f'\n [Estoque Atual de {nome_kit}: {qtd_atual} unidades]')
    resp = str(input('Foi aberto um novo kit ? (Sim / Não)')).strip().upper()
    while True:
        if resp in ['SIM', 'S'] and estoque_kits[nome_kit] > 0:
            estoque_kits[nome_kit] -= 1
            print(f'Novo estoque de {nome_kit}: {estoque_kits[nome_kit]} unidades')

        elif resp in ['SIM', 'S'] and estoque_kits[nome_kit] == 0:
            print(f'Não há kits de {nome_kit} em estoque')

        elif resp in ['NÃO', 'N', 'NAO']:
            print(f'Sem alteração no estoque')
        else:
            print('Por favor digite apenas (sim ou não)')
            continue
        print('-='*40)
        return  estoque_kits
    
    
def nome():
    return input('Digite seu nome: ').strip()
def obter_float(mensagem):
    # Garante que a entrada do usuário seja um número válido e maior que zero 
    while True:
        try:
            valor = float(input(mensagem))
            return valor 
        except ValueError:
            print('Erro! Por favor digite um número válido.')

def absorbancias():
    abs_teste = obter_float('Digite o valor da absorbância [teste]:')
    while True:
        abs_padrao = obter_float('Digite o valor da absorbância [padrão]:')
        if abs_padrao != 0:
            break
        print('A absorbância do padrão não pode ser zero.')
    return abs_teste, abs_padrao

def classificar_resultado(resultado, intervalo):
    #Classifica o resultado baseado em faixa e valores 
    for limite, classificacao in intervalo:
        if resultado <= limite:
            return classificacao 
    return 'fora dos padrões'

def executar_teste_padrao(nome_kit):
    #Função utilizada para calcular os testes com reação de ponto final
    cfg= conf_testes[nome_kit]
    estoque_atualizado = estoque(nome_kit)
    nome_usuario = nome()
    abs_teste, abs_padrao = absorbancias()
    resultado = (abs_teste/abs_padrao) * cfg['fator']
    classificacao = classificar_resultado(resultado, cfg['intervalo'])

    print(f'O valor do teste de: {nome_kit}  realizado por: {nome_usuario}. \n foi de: {resultado:.2f} {cfg["unidade"]}')
    print(f'Classificação: {classificacao}')

    return {
        'Aluno': nome_usuario,
        'Absorbância teste': abs_teste,
        'Absorbância padrão': abs_padrao,
        'Resultado': resultado,
        'unidade': cfg['unidade'],
        'Classificação': classificacao
    }, estoque_atualizado 

def executar_teste_cinetico(nome_kit, qtd_leituras = 2):
    #Função utilizada para calcular os testes cinéticos 
    cfg=conf_testes[nome_kit]
    estoque_atualizado = estoque(nome_kit)
    nome_usuario=nome()
    categorias = ['teste', 'padrão']
    leituras = [[], []]
    for idx, categoria in enumerate(categorias):
        print(f"\n---Leituras do {categoria}---")
        for i in range(1, qtd_leituras + 1):
            while True:
                try:   
                    val = float(input(f'Digite a leitura {i} do {categoria}:'))
                    leituras[idx].append(val)
                    break 
                except ValueError:
                    print('ERRO! por favor digite um número válido')

    #Cálculo do Delta (primeira - ultima leitura) para o teste e o padrão
    delta_teste = leituras[0][0] - leituras[0][-1]
    delta_padrao = leituras[1][0] - leituras[1][-1]
    if delta_padrao == 0:
        print('\nERRO ! A variação do padrão não pode resultar em 0.')
        return None, estoque_atualizado
    resultado = (delta_teste/delta_padrao) * cfg['fator']
    classificacao = classificar_resultado(resultado, cfg['intervalo'])
    
    print(f'O valor do teste de: {nome_kit}  realizado por: {nome_usuario}. \n foi de: {resultado:.2f} {cfg["unidade"]}')
    print(f'Classificação: {classificacao}')
    return (
        {
            'Aluno': nome_usuario,
            'Absorbância teste':leituras[0],
            'Absorbância padrão':leituras[1],
            'Delta teste': delta_teste,
            'Delta padrão':delta_padrao,
            'Resultado': resultado,
            'unidade': cfg['unidade'],
            'Classificação': classificacao
    }, estoque_atualizado
        )
def bilirrubina():
    estoque_atualizado = estoque('bilirrubina')
    nome_usuario = nome()
    
    bili_d = obter_float('Digite a Absorbância do teste de bilirrubina direta: ')
    bili_t = obter_float('Digite a Absorbância do teste de bilirrubina total: ')
    
    resultado_d = (bili_d / 0.337) * 10
    resultado_t = (bili_t / 0.337) * 10
    resultado_i = resultado_t - resultado_d
    
    print(f'\nResultados para {nome_usuario}:')
    print(f'Direta: {resultado_d:.2f} mg/dL | Total: {resultado_t:.2f} mg/dL | Indireta: {resultado_i:.2f} mg/dL')

    return {
        'Aluno': nome_usuario,
        'Absorbância teste direta': bili_d,
        'Absorbância teste total': bili_t,
        'Resultado direta': resultado_d,
        'Resultado total': resultado_t,
        'Resultado indireta': resultado_i,
        'unidade': 'mg/dL',
        'Classificação direta': 'Desejável' if resultado_d <= 0.3 else 'Elevado',
        'Classificação total': 'Desejável' if resultado_t <= 1.2 else 'Elevado',
        'Classificação indireta': 'Desejável' if resultado_i <= 1.0 else 'Elevado'
    }, estoque_atualizado

   