texto = input('Digite algo: ')

texto_invertido = []

for char in texto:
    texto_invertido.insert(0, char)

texto_invertido = ''.join(texto_invertido)
print(texto_invertido)