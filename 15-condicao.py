# # Informações sobre o filme
# name = input("Digite o nome do filme: ")
# yearRelease = int(input("Digite o ano de lançamento "))
# rating = float(input("Digite a nota de avaliação do filme: "))

# # Verifica se o filme é recomendado

# if rating > 8.0 and yearRelease > 2015:
#     print(f"O filme {name} é muito bom. Recomendado!")
# else:
#     print(f"O filme {name} ainda não atingiu uma boa nota.")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = input("Digite a operação a ser realizada (+ - * /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = 0
        print("Erro: Divisão por Zero")
else:
    result = 0
    print("Operação inválida!")

print(f"Resultado da operação é: {result:.2f}")