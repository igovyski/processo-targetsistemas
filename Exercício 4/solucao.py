faturamento_distribuidora = [
    {'Estado': 'SP', 'Valor': 67836.43},
    {'Estado': 'RJ', 'Valor': 36678.66},
    {'Estado': 'MG', 'Valor': 29229.88},
    {'Estado': 'ES', 'Valor': 27165.48},
    {'Estado': 'Outros', 'Valor': 19849.53}
]

total_faturamento = 0

for dados in faturamento_distribuidora:
    total_faturamento += dados['Valor']

for dados in faturamento_distribuidora:
    estado = dados['Estado']
    valor = dados['Valor']
    if estado != 'Outros':
        print(f'O estado de {estado} teve {(valor / total_faturamento)*100 :.2f}% de represetação no valor total da distribuidora')
    else:
        print(f'Os {estado} estados tiveram {(valor / total_faturamento)*100 :.2f}% de represetação no valor total da distribuidora')