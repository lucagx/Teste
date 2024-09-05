def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        prox_valor = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(prox_valor)
    return fib_sequence

def is_fibonacci(number):
    if number < 0:
        return False

    fib_sequence = fibonacci_sequence(number)

    return number in fib_sequence

while True:
    numero = int(input("Informe um número para ser verificar se pertence à sequência de Fibonacci: "))

    pertence = is_fibonacci(numero)
    mensagem = f"O número {numero} {'pertence' if pertence else 'não pertence'} à sequência de Fibonacci."
    print(mensagem)

    continuar = input("Você deseja verificar outro número? (s/n): ").strip().lower()
    if continuar != 's':
        print("Programa finalizado.")
        break