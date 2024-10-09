def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False


numero_informado = int(input('Digite o numero desejado: '))
if fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {
          numero_informado} não pertence à sequência de Fibonacci.")
