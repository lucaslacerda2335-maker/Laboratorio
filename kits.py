
import programa_lab

kits=['colesterol', 'magnesio', 'glicose', 'hemoglobina', 'fosforo', 'proteinas totais', 
      'bilirrubina', 'acido urico', 'colesterol HDL', 'albumina', 'cálcio']

tipo_teste=['teste', 'padrão']

def estoque(nome_kit):
    estoque_kits = programa_lab.carregar_estoque()
    print(f'\n [Estoque Atual de {nome_kit}: {estoque_kits[nome_kit]} unidades]')
    resp = str(input('Foi aberto um novo kit ? (Sim / Não)')).strip().upper()
    if resp in ['SIM', 'S'] and estoque_kits[nome_kit] > 0:
        estoque_kits[nome_kit] -= 1
        print(f'Novo estoque de {nome_kit}: {estoque_kits[nome_kit]} unidades')
    elif resp in ['SIM', 'S'] and estoque_kits[nome_kit] == 0:
            print(f'Não há kits de {nome_kit} em estoque')
    else:
        print()#para evitar a repetição do print do estoque caso o usuário digite "Não" ou qualquer outra coisa que não seja "Sim"
    print('-='*40)
    return  estoque_kits
    
    
def nome():
    nome_digitado = str(input('Digite seu nome: '))
    return nome_digitado

def absorbancias():
    values = []
    for const in range(0,2):
        num = float(input(f'Digite o valor da Absorbância {tipo_teste[const]} :'))
        values.append(num)
    return values #importante para retornar os valores do teste 

def colesterol():
    estoque_atualizado=estoque('colesterol')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 200
    print(f'O valor do teste de colesterol realizado por: {nome_usuario}, foi de: {result :.2f} mg/dL')
    if result <= 200.0: 
        print('O nível do colesterol está dentro do desejável')
    elif result > 200.0 and result <= 239.0:
        print('Os níveis de colesterol estão no limítrofe')
    else:
        print('Os níveis de colesterol estão elevados')
    
    return (
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'mg/dL',
        'Classificação:': 'Desejável' if result <= 200.0 else 'Limítrofe' if result <= 239.0 else 'Elevado'  
        }, 
        estoque_atualizado
    )

def magnesio():
    estoque_atualizado=estoque('magnesio')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 2.0
    print(f'O valor do teste de magnesio realizado por: {nome_usuario}, foi de: {result :.2f} mg/dL')
    if result <= 1.7: 
        print('O nível do magnesio está abaixo do desejável')
    elif result > 1.7 and result <= 2.6:
        print('Os níveis de magnesio estão dentro do desejável')
    else:
        print('Os níveis de magnesio estão elevados')

    return(
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'mg/dL',
        'Classificação:': 'Abaixo do desejável' if result <= 1.7 else 'Dentro do desejável' if result <= 2.6 else 'Elevado'
        }, 
        estoque_atualizado
    ) 
        

def glicose():
    estoque_atualizado = estoque('glicose')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 100
    print(f'O valor do teste de glicose realizado por: {nome_usuario}, foi de: {result :.2f} mg/dL')
    if result >=65.0 and result <= 99.0: 
        print('O nível da glicose está dentro do desejável')
    elif result > 99.0 and result <= 125.0:
        print('Os níveis de glicose estão no limítrofe')
    elif result > 125.0:
        print('Os níveis de glicose estão elevados')
    elif result < 65.0:
        print('Os níveis de glicose estão baixos (hipoglicemia)')

    return (
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'mg/dL',
        'Classificação:': 'Dentro do desejável' if result >= 65.0 and result <= 99.0 else 'Limítrofe' if result <= 125.0 else 'Elevado' if result > 125.0 else 'Baixo',
        }, 
        estoque_atualizado
    )
 
def hemoglobina():
    estoque_atualizado = estoque('hemoglobina')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 10.0
    print(f'O valor do teste de hemoglobina realizado por: {nome_usuario}, foi de: {result :.2f} g/dL')
    if result >= 12.0 and result <= 16.0: 
        print('O nível da hemoglobina está dentro do desejável')
    elif result < 12.0:
        print('Os níveis de hemoglobina estão baixos (anemia)')
    else:
        print('Os níveis de hemoglobina estão elevados')
    
    return (
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'g/dL',
        'Classificação:': 'Dentro do desejável' if result >= 12.0 and result <= 16.0 else 'Baixo (anemia)' if result < 12.0 else 'Elevado'
        }, 
        estoque_atualizado
    )

def fosforo():
    estoque_atualizado = estoque('fosforo')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 5.0
    print(f'O valor do teste de fosforo realizado por: {nome_usuario}, foi de: {result :.2f} mg/dL')
    if result >= 2.5 and result <= 4.5: 
        print('O nível do fosforo está dentro do desejável')
    elif result < 2.5:
        print('Os níveis de fosforo estão baixos')
    else:
        print('Os níveis de fosforo estão elevados')

    return (
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'mg/dL',
        'Classificação:': 'Dentro do desejável' if result >= 2.5 and result <= 4.5 else 'Baixo' if result < 2.5 else 'Elevado'
        }, 
        estoque_atualizado
    )

def proteinas_totais():
    estoque_atualizado = estoque('proteinas totais')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 4.0
    print(f'O valor do teste de proteinas totais realizado por: {nome_usuario}, foi de: {result :.2f} g/dL')
    if result >= 6.0 and result <= 8.3: 
        print('O nível das proteinas totais está dentro do desejável')
    elif result < 6.0:
        print('Os níveis das proteinas totais estão baixos')
    else:
        print('Os níveis das proteinas totais estão elevados')

    return (
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'mg/dL',
        'Classificação:': 'Dentro do desejável' if result >= 6.0 and result <= 8.3 else 'Baixo' if result < 6.0 else 'Elevado'
        }, 
        estoque_atualizado
    )

def bilirrubina():
    estoque_atualizado = estoque('bilirrubina')
    nome_usuario = nome()
    biliD = float(input('Digite o valor da Absorbância do teste de bilirrubina direta:'))
    biliT = float(input('Digite o valor da Absorbância do teste de bilirrubina total:'))
    resultd = (biliD / 0.337) * 10
    resultT = (biliT / 0.337) * 10
    resultI = resultT - resultd
    print(f'O valor do teste de bilirrubina realizado por: {nome_usuario}')
    print(f'O valor do teste de bilirrubina direta foi de: {resultd :.2f} mg/dL')
    print(f'O valor do teste de bilirrubina total foi de: {resultT :.2f} mg/dL')
    print(f'O valor do teste de bilirrubina indireta foi de: {resultI :.2f} mg/dL')

    return(
        {
        'Aluno:': nome_usuario,
        'Absorbância teste direta:': biliD,
        'Absorbância teste total:': biliT,
        'Resultado direta:': round(resultd, 2),
        'Resultado total:': round(resultT, 2),
        'Resultado indireta:': round(resultI, 2),
        'unidade:': 'mg/dL',
        'Classificação direta:': 'Desejável' if resultd <= 0.3 else 'Elevado',
        'Classificação total:': 'Desejável' if resultT <= 1.2 else 'Elevado',
        'Classificação indireta:': 'Desejável' if resultI <= 1.0 else 'Elevado'
        }, 
        estoque_atualizado
    )

def acido_urico():
    estoque_atualizado = estoque('acido urico')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 6.0
    print(f'O valor do teste de acido urico realizado por: {nome_usuario}, foi de: {result :.2f} mg/dL')
    if result >= 3.5 and result <= 7.2: 
        print('O nível do acido urico está dentro do desejável')
    elif result < 3.5:
        print('Os níveis do acido urico estão baixos')
    else:
        print('Os níveis do acido urico estão elevados')

    return (
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'mg/dL',
        'Classificação:': 'Dentro do desejável' if result >= 3.5 and result <= 7.2 else 'Baixo' if result < 3.5 else 'Elevado'
        }, 
        estoque_atualizado
    )
    
def colesterol_hdl():
    estoque_atualizado = estoque('colesterol HDL')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 40.0
    print(f'O valor do teste de colesterol HDL realizado por: {nome_usuario}, foi de: {result :.2f} mg/dL')
    if result >= 40.0 and result <= 60.0: 
        print('O nível do colesterol HDL está dentro do desejável')
    elif result < 40.0:
        print('Os níveis do colesterol HDL estão baixos')
    else:
        print('Os níveis do colesterol HDL estão elevados')

    return (
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'mg/dL',
        'Classificação:': 'Dentro do desejável' if result >= 40.0 and result <= 60.0 else 'Baixo' if result < 40.0 else 'Elevado'
        }, 
        estoque_atualizado
    )

def albumina():
    estoque_atualizado = estoque('albumina')
    nome_usuario = nome()
    abs_values = absorbancias()
    result = (abs_values[0]/abs_values[1]) * 3.8
    print(f'O valor do teste de albumina realizado por: {nome_usuario}, foi de: {result :.2f} g/dL')
    if result >= 3.5 and result <= 5.5: 
        print('O nível da albumina está dentro do desejável')
    elif result < 3.5:
        print('Os níveis da albumina estão baixos')
    else:
        print('Os níveis da albumina estão elevados')

    return(
        {
        'Aluno:': nome_usuario,
        'Absorbância teste:': abs_values[0],
        'Absorbância padrão:': abs_values[1],
        'Resultado:': round(result, 2),
        'unidade:': 'g/dL',
        'Classificação:': 'Dentro do desejável' if result >= 3.5 and result <= 5.5 else 'Baixo' if result < 3.5 else 'Elevado'
        }, 
        estoque_atualizado
    )
def calcio():
    estoque_atualizado = estoque('cálcio')
    nome_usuario = nome()
    abs_values= absorbancias()
    result = (abs_values[0]/abs_values) * 10
    print(f'O valor do teste de cálcio realizado por: {nome_usuario}, foi de: {result:.2f} mg/dL')
    if result >= 8.8 and result <=11.0:
        print(f'os valores de cálcio estão dentro da normalidade para um individuo adulto')
    elif result < 8.8:
        print(f'os valores de cálcio estão muito baixos')
    else:
        print('valores de cálcio muito elevados')
    return(
        {
            'Aluno': nome_usuario,
            'Absorbância teste': abs_values[0],
            'Absorbância padrão': abs_values[1],
            'Resultado': round(result, 2),
            'unidade': 'mg/dL',
            'Classificação': 'Dentro do valor de referência' if result >= 8.8 and result <=11.0  else 'Fora dos padrões'  
        },
        estoque_atualizado
    )