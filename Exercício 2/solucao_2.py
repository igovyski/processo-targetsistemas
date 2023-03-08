# Sem usar função 'index'

n = int(input('Insira um número: '))

i = 0
fibonacci = [0, 1, 1]

for i in range(500):
    if i < 3:
        pass
        # print(fibonacci[i])
    else:
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

if n in fibonacci:
    print(f'O número {n} está na Sequência de Fibonacci')
else:
    print(f'O número {n} não está na Sequência de Fibonacci')