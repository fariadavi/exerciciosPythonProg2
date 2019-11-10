def limite(num):
    "Método que calcula o limite(1 + 1/n)^n, para n -> +inf"
    return (1 + 1/num) ** num

print(limite(1e100))