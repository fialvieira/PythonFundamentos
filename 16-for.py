# Lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista
print("#1")
for movie in moviesList:
    print(movie)

# 2 - Quando a condição for atendida o loop será encerrado
print("#2")
for movie in moviesList:
    if (movie == "Inception"):
        break
    print(movie)

# 3 - Quando a condição for atentida o loop vai para a próxima iteração
print("#3")
for movie in moviesList:
    if (movie == "Inception"):
        continue
    print(movie)

# 4 - Avaliação do filme
movieName = input("Digite o nome do filme: ")
totalMovieRating = int(input("Digite quantas avaliações deseja fazer: "))

total = 0

for i in range(totalMovieRating):
    rating = float(input("Digite a nota para o filme: "))
    total += rating

if totalMovieRating > 0:
    average = total / totalMovieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")