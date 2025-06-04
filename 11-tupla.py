moviesTuple = ("Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Interestellar")
print(type(moviesTuple))

# 1 - Buscar os 2 primeiros itens da tupla
print(moviesTuple[:2])

# 2 - Buscar o último item da tupla
print(moviesTuple[-1])

# 3 - Filmes até uma determinada posição
print(moviesTuple[:3])

# 4 - Buscar filmes de uma posição em diante
print(moviesTuple[2:])

# 5 - Recuperar um item da tupla pelo nome
print(moviesTuple.index("Pulp Fiction"))