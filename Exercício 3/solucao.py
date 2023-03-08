import json

with open('Exercício 3/dados.json', encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

menor_faturamento, maior_faturamento = dados[0]['valor'], dados[0]['valor']
total_faturamento, media_faturamento, dias_uteis, dia_acima_media = 0, 0, 0, 0

for dia in dados:
    if dia['valor'] < menor_faturamento and dia['valor'] != 0.0:
        menor_faturamento = dia['valor']

    if dia['valor'] > maior_faturamento:
        maior_faturamento = dia['valor']

    if dia['valor'] > 0.0:
        dias_uteis += 1

    total_faturamento += dia['valor']

media_faturamento = total_faturamento / dias_uteis

for dia in dados:
    if dia['valor'] > media_faturamento:
        dia_acima_media += 1

print(f'O menor valor faturado em um dia no mês foi de: R${menor_faturamento:.2f}')
print(f'O maior valor faturado em um dia no mês foi de: R${maior_faturamento:.2f}')
print(f'A quantidade de dias acima da média de faturamento foi de: {dia_acima_media} dias')
print(f'A média de faturamento foi de R${media_faturamento:.2f}')