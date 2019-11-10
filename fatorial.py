def fatorial(num):
    "Método que retorna o fatorial do número recebido como parâmetro"
    fatorial = num
    for i in range(num, 2, -1):
        fatorial = fatorial * (num-1)
        num = num-1
    return fatorial

print('Fatorial de 10: ', fatorial(10))
print('Fatorial de 15: ', fatorial(15))
print('Fatorial de 20: ', fatorial(20))