name = input("Informe o nome do filme: ")
yearLaunch = int(input("Informe o ano de lançamento do filme: "))
movieRating = float(input("Informe a nota do filme: "))

print("\nDados do filme")
print("=============================")

# Alternativa 1
print("Nome do filme:", name)
print("Ano de lançamento:", yearLaunch)
print("Nota do filme:", movieRating)

# Alternativa 2
print("\nNome do filme:", name, "\nAno de lançamento:", yearLaunch, "\nNota do filme:", movieRating)

# Alternativa 3 - f string
print(f"\nNome do filme: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota do filme: {movieRating}")