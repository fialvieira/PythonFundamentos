movieName = "Top Gun"
# string[início:fim] - índice começa na posição 0 | índice final - 1

# 1 - Buscar toda a string a partir da primeira posição
print(movieName[0:])

# 2 - Buscar toda string até a última posição
print(movieName[:7])

# 3 - Buscar toda a string da terceira até a última posição
print(movieName[2:])

"""
string[início:fim:passo] - índice começa na posição 0 | índice final - 1 | passo determina o incremento (por padrão 1)
"""

# 4 - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

# 5 - Buscar toda a string nos índices ímpares
print(movieName[1::2])

# 6 - Inverter uma string
print(movieName[::-1])