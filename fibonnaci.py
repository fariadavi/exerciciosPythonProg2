def fibonacci(num):
    "Método que imprime os primeiros N números da sequência Fibonacci"
    fibonacci = 1
    aux = 0
    str = f'{aux}, {fibonacci}'
    for i in range(0, num):
        aux2 = fibonacci + aux
        aux = fibonacci
        fibonacci = aux2
        str += f', {fibonacci}'
    return str

print(fibonacci(5))