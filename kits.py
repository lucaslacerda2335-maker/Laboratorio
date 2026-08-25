
import programa_lab
from time import sleep 

#Mapeamento dos testes com seus fatores, unidades e faixa de referência
conf_testes ={
    'colesterol':{
        'fator': 200.0,
        'unidade':'mg/dL',
        'intervalo': [(200.0, 'Desejável'), (239.0, 'Limítrofe'), (float('inf'), 'Elevado')]
    },
    'magnesio':{
        'fator': 2.0,
        'unidade':'mg/dL',
        'intervalo': [(1.7,'Abaixo do desejável'), (2.6, 'Desejável'), (float('inf'), 'Elevado')]
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
    },
    'Triglicerides': {
        'fator': 200.0,
        'unidade': 'mg/dL',
        'intervalo':[(149.0, 'Desejável'), (200.0, 'Limitrofe'), (float('inf'), 'Elevado')]
    },
    'Lactato enzimatico':{
        'fator': 40,
        'unidade': 'mg/dL',
        'intervalo': [(4.49, 'Valor abaixo do IR'), (19.8, 'Desejável'), (float('inf'), 'Elevado')]
    },
    'Fosfatase Alcalina':{
        'fator': 45.0,
        'unidade': 'U/L',
        'intervalo': [(12.9, 'Valor abaixo do IR'), (43.0, 'Desejável'), (float('inf'), 'Elevado')]
    }
}

def estoque(nome_kit):
    estoque_kits = programa_lab.carregar_estoque()
    qtd_atual = estoque_kits.get(nome_kit, 0)
    print(f'\n [Estoque Atual de {nome_kit}: {qtd_atual} unidades]')
    while True:
        resp = str(input('Foi aberto um novo kit ? (Sim / Não)')).strip().upper()
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

def validade():
    val=str(input('Digite a validade o kit. modelo(dd/mm/aaaa):  '))
    return val

def obter_float(mensagem):
    # Garante que a entrada do usuário seja um número 
    # válido e maior que zero 
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
    val=validade()
    abs_teste, abs_padrao = absorbancias()
    resultado = (abs_teste/abs_padrao) * cfg['fator']
    classificacao = classificar_resultado(resultado, cfg['intervalo'])

    print(f'O valor do teste de: {nome_kit}  realizado por: {nome_usuario}. \n foi de: {resultado:.2f} {cfg["unidade"]}')
    print(f'Classificação: {classificacao}')

    return {
        'Aluno': nome_usuario,
        'Teste': nome_kit,
        'Absorbância teste': round(abs_teste,2),
        'Absorbância padrão': round(abs_padrao,2),
        'Resultado': round(resultado,2),
        'unidade': cfg['unidade'],
        'Classificação': classificacao,
        'validade': val
    }, estoque_atualizado 

def executar_teste_cinetico(nome_kit, qtd_leituras = 2):
    #Função utilizada para calcular os testes cinéticos 
    cfg=conf_testes[nome_kit]
    estoque_atualizado = estoque(nome_kit)
    nome_usuario=nome()
    val=validade()
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
            'Teste': nome_kit,
            'Absorbância teste':leituras[0],
            'Absorbância padrão':leituras[1],
            'Delta teste': round(delta_teste,2),
            'Delta padrão':round(delta_padrao,2),
            'Resultado': round(resultado,2),
            'unidade': cfg['unidade'],
            'Classificação': classificacao,
            'validade': val
        }, estoque_atualizado
        )
def bilirrubina():
    estoque_atualizado = estoque('bilirrubina')
    nome_usuario = nome()
    val = validade()
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
        'Resultado direta': round(resultado_d,2),
        'Resultado total': round(resultado_t,2),
        'Resultado indireta': round(resultado_i,2),
        'unidade': 'mg/dL',
        'Classificação direta': 'Desejável' if resultado_d <= 0.3 else 'Elevado',
        'Classificação total': 'Desejável' if resultado_t <= 1.2 else 'Elevado',
        'Classificação indireta': 'Desejável' if resultado_i <= 1.0 else 'Elevado',
        'validade': val
    }, estoque_atualizado
   
def ferro_serico():
    estoque_atualizado = estoque('ferro_serico')
    nome_usuario = nome()
    val = validade() 
    abs_teste = []
    num = 0
    for i in range(0,2):
        num = obter_float(f'Digite o valor da absorbância do teste {i + 1}:')
        abs_teste.append(num)
    abs_padrao = float(input('Digite a absorbância do padrão: '))
    delta_teste = abs_teste[1] - abs_teste[0]
    resultado = (delta_teste/abs_padrao) * 500.0

    print(f'O resultado do teste de ferro sérico, realizado por: {nome_usuario}\nfoi de:{resultado:.2f}')
    return {
        'Aluno': nome_usuario,
        'Teste':'ferro sérico',
        'Absorbância teste': abs_teste[:],
        'Delta teste': round(delta_teste,2),
        'Resultado': round(resultado,2),
        'unidade':'ug/dL',
        'Classificação': 'Desejável' if resultado >= 49.9 and resultado <= 170.0 else 'fora dos parâmetros',
        'validade': val
    }, estoque_atualizado
def LDH():
    estoque_atualizado = estoque('LDH')
    nome_usuario = nome()
    val = validade()
    abs_teste = []
    num = 0
    for i in range(0,2):
        num = obter_float(f'Digite o valor da absorbância do teste {i +1}: ')
        abs_teste.append(num)
    delta_teste = (abs_teste[0] - abs_teste[1])/2
    resultado = delta_teste * 8095
    print(f'O resultado do teste de ferro sérico, realizado por: {nome_usuario}\nfoi de:{resultado:.2f}')

    return{
        'Aluno':nome_usuario,
        'Teste': 'LDH',
        'Absorbância teste': abs_teste[:],
        'Delta teste':round(delta_teste,2),
        'Resultado':round(resultado,2),
        'unidade': 'U/L',
        'Classificação': 'Desejável' if resultado >= 200.0 and resultado <= 480.0 else 'fora dos parâmetros',
        'validade': val
    }, estoque_atualizado

def gama_GT():
    estoque_atualizado = estoque('gama_GT')
    nome_usuario = nome()
    val = validade()
    abs_teste = []
    num = 0
    for i in range(0,2):
        num = obter_float(f'Digite o valor da absorbância do teste {i +1}: ')
        abs_teste.append(num)
    delta_teste = (abs_teste[1] - abs_teste[0])/2
    resultado = delta_teste * 2577
    print(f'O resultado do teste de ferro sérico, realizado por: {nome_usuario}\nfoi de:{resultado:.2f}')
    return{
            'Aluno':nome_usuario,
            'Teste': 'gama GT',
            'Absorbância teste': abs_teste[:],
            'Delta teste':round(delta_teste,2),
            'Resultado':round(resultado,2),
            'unidade': 'U/L',
            'Classificação': 'Desejável' if resultado >= 5.0 and resultado <= 58.0 else 'fora dos parâmetros',
            'validade': val
        }, estoque_atualizado
def fosfatase_alcalina_DGKC():
    estoque_atualizado = estoque('fosfatase_alcalina_DGKC')
    nome_usuario = nome()
    val = validade()
    abs_teste = []
    num = 0
    for i in range(0,4):
        num = obter_float(f'Digite o valor da absorbância A{i}: ')
        abs_teste.append(num)
    delta_teste = (abs_teste[1]-abs_teste[0]) + (abs_teste[2]-abs_teste[1]) + (abs_teste[3]-abs_teste[2])
    resultado = (delta_teste/3) * 2720
    print(f'O resultado do teste de fosfatase alcalina DKGC, realizado por: {nome_usuario}\n foi de: {resultado:.2f}')
    return {
        'Aluno':nome_usuario,
        'Teste': 'fosfatase alcalina DGKC',
        'Absorbância teste': abs_teste[:],
        'Delta teste':round(delta_teste,2),
        'Resultado':round(resultado,2),
        'unidade': 'U/L',
        'Classificação': 'Desejável' if resultado >= 13.0 and resultado <= 43.0 else 'fora dos parâmetros',
        'validade': val
    }, estoque_atualizado



   