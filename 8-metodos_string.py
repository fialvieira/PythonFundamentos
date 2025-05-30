movieName = "Top Gun"
movieDescription = """
    Top Gun Maverick é um filme de aviação e aventura
    muito consagrado na indústria do cinema.
"""

print(movieName.upper()) # Tudo maiúscula
print(movieName.lower()) # Tudo minúscula
print(movieName.capitalize()) # Primeira letra maiúscula
print(movieName.title()) # Primeira letra de cada palavra em maiúscula
print(movieName.center(10, '-')) # Retorna string centralizada com caractere de preenchimento
print(movieName.find("u")) # Retorna o índice de um determinado caractere
print(movieDescription.count("o")) # Conta o número de caracteres
print(movieName.replace("Top", "Matrix")) # Altera elemento por outro
print(movieDescription.split(' '))