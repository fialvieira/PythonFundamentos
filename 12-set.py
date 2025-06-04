moviesSet = {"Inception", "The Shawshank Redemption", "The Dark Knight", "Pulp Fiction", "Interestellar"}
print(type(moviesSet))

# 1 - Buscar o tamanho do set
print(len(moviesSet))

# 2 - True e 1 são considerados o mesmo valor
examples = {"Inception", True, 1, 8.7}
print(examples)

# 3 - Adicionar item de outro set
moviesSet.update(examples)
print(moviesSet)

# 4 - Remover um item do set
moviesSet.remove(True) # type: ignore
moviesSet.remove(8.7) # type: ignore
print(moviesSet)