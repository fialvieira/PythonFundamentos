num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print("Aritméticos")
print(f"Soma: {sum}")
print(f"Subtração: {sub}")
print(f"Divisão: {div}")
print(f"Multiplicação: {mult}")
print(f"Resto da divisão: {mod}")
print(f"Potência de {num1} por {num2}: {exp}\n")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
notEqual = num1 != num2
biggerEqual = num1 >= num2
smallerEqual = num1 <= num2

print("Comparação")
print(f"Maior entre {num1} e {num2}: {bigger}")
print(f"Menor entre {num1} e {num2}: {smaller}")
print(f"Iguais entre {num1} e {num2}: {equal}")
print(f"Maior ou igual entre {num1} e {num2}: {biggerEqual}")
print(f"Menor ou igual entre {num1} e {num2}: {smallerEqual}")

# Atribuição
num1 += 1 # Serve para todos os operadores