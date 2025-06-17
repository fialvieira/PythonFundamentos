# 1 - Função para imprimir uma mensagem
def welcome():
    print("Bem vindo ao sistema de filmes!")

# 2 - Função para calcular a média de notas
def calcAverage():
    numRatings = int(input("Digite quantas avaliações deseja fazer para o filme: "))
    total = 0
    for i in range(numRatings):
        rating = float(input("Digite a nota para o filme: "))
        total += rating
    
    if numRatings > 0:
        average = total / numRatings
    else:
        average = 0
    
    return average

# print(f"Média das avaliações: {calcAverage():.2f}")

# 3 - Função para cadastrar um filme
def inputMovie():
    name = input("Informe o nome do filme: ")
    yearLaunch = int(input("Informe o ano de lançamento do filme: "))
    moviePrice = float(input("Digite o preço do filme: "))
    movieRating = float(input("Informe a nota do filme: "))
    print(f"{name} ({yearLaunch}) - R$ {moviePrice:.2f} - Nota {movieRating}.")

inputMovie()
