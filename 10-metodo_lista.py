moviesList = ["Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Interestellar"]

# 1 - Tamanho da lista
print(f"Tamanho da lista: {len(moviesList)} itens")

# 2 - Recuperar um item da lista pelo nome
print(f"Índice na lista: {moviesList.index("Interestellar")}")

# 3 - Adicionar um item no final da lista
moviesList.append("Lord of the rings")
print(moviesList)

# 4 - Ordenar a lista
moviesList.sort()
print(moviesList)

# 5 - Copiar os itens do uma lista para outra
moviesCopy = moviesList.copy()
moviesCopy.remove("Pulp Fiction")
print(moviesCopy)

# 6 - Remove todos os itens da lista
moviesList.clear()
print(moviesList)