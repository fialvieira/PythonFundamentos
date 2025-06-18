# 1 - Função para imprimir um nome completo
def full_name(first_name, last_name):
    print(f"Nome é: {first_name} {last_name}")

full_name("Filipe", "Vieira")

# 2 - Função para somar dois números
def sum_numbers(a, b):
    return a + b

print(f"A soma é {sum_numbers(10,50)}")

# 3 - Função com parâmetro padrão (default)
def address(country = "Brazil"):
    print(f"Eu moro em: {country}")

address()
address("Portugal")

# 4 - Função para avaliar filme
def rate_movie(num_ratings, movie_name):
    total = 0
    for i in range(num_ratings):
        rate = float(input("Digite a nota: "))
        total += rate
    
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0
    
    print(f"Média de avaliação do filme {movie_name} é {average:.2f}")

rate_movie(2, "Inception")