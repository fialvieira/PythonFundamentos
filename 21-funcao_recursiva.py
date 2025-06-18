"""
Fatorial de um número:
1 -> 1 * 1          1
2 -> 2 * 1          2 * factorial(1)
3 -> 3 * 2 * 1      3 * factorial(2)
4 -> 4 * 3 * 2 * 1
"""

# 1 - Fatorial de um número
def factorial(num):
    if num == 1: # Condição de parada
        return 1
    else:
        return (num * factorial(num - 1))

number = 4

print(f"O fatorial de {number} é {factorial(number)}.")

# 2 - Soma total de um número
def total_sum(num):
    if num == 1: # Condição de parada
        return 1
    else:
        return (num + total_sum(num - 1))
    
number = 4

print(f"O somatório de {number} é {total_sum(number)}.")