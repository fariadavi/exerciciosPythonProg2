def fibonacci(num):
    "Método que imprime os primeiros N números da sequência Fibonacci"
    fibonacci = 1
    aux = 0
    print (aux)
    print (fibonacci)
    for i in range(0, num):
        aux2 = fibonacci + aux
        aux = fibonacci
        fibonacci = aux2
        print(fibonacci)


fibonacci(20)