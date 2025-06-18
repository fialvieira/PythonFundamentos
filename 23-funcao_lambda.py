# Função de potência de um número
power = lambda num, expo: num ** expo
print(power(2,5))

# Função que verifica se o número é par
is_even = lambda x: x % 2 == 0
print(is_even(2))

# Função que divide um número por outro
div_num = lambda x, y: x / y
print(div_num(4,2))

# Função que inverte uma string
reverse_string = lambda s: s[::-1]
print(reverse_string("Filipe Alves"))

# Funcionalidades relacionadas aos filmes
movies_list = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic": [8.5, 9.0, 7.5],
    "The Godfather": [9.5, 9.8, 8.0],
    "Inception": [8.0, 7.0, 8.5],
    "Jurassic Park": [7.5, 7.0, 8.0],
    "The Matrix": [8.8, 9.2, 8.5]
}

# Função para calcular a média de avaliações de um filme
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
print(f"Média de avaliação do filme The Matrix: {average_rating("The Matrix"):.2f}")

# Função que verifica se um filme está na lista
check_movie = lambda movie_name: movie_name in movies_list
print(f"O filme Mario está na lista: {check_movie("Mario")}")

# Função para recomendar um filme com base na avaliação média
recommended_film = lambda movie_name: f"Recomendo assistir {movie_name} com média {average_rating(movie_name):.2f}."
print(recommended_film("The Godfather"))