# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(num):
    # Inicializa os primeiros números da sequência
    fib_1, fib_2 = 0, 1
    
    # Verifica se o número é 0 ou 1, que pertencem à sequência por definição
    if num == 0 or num == 1:
        return True
    
    # Calcula a sequência de Fibonacci até encontrar o número ou passar dele
    while fib_2 <= num:
        if fib_2 == num:
            return True
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    
    # Se passou do número e não encontrou, então não pertence
    return False

# Entrada do número a ser verificado
numero = int(input("Informe o número para verificar se pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
