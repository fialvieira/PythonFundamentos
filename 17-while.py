# Lista de filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista de filmes usando while
print("#1")
index = 0
while index < len(moviesList):
    print(moviesList[index])
    index += 1

# 2 - Quando a condição for atendida, o loop será encerrado - break
print("#2")
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        break
    print(moviesList[index])
    index += 1

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração - continue
print("#3")
index = 0
while index < len(moviesList):
    if moviesList[index] == "Inception":
        index += 1
        continue
    print(moviesList[index])
    index += 1

# 4 - Avaliação do filme com while
print("#4")
movieName = input("Digite o nome do filme: ")
totalMovieRating = int(input("Digite quantas avaliações deseja fazer: "))

total = 0
count = 0

while count < totalMovieRating:
    rating = float(input("Digite a nota para o filme: "))
    total += rating
    count += 1

if totalMovieRating > 0:
    average = total / totalMovieRating
else:
    average = 0

print(f"Média de avaliação do filme {movieName} é: {average:.2f}")
