"""
1- Escreva uma programa que lê dois nomes e retorne uma string 
formatada no formato "ÚltimoNome, PrimeiroNome".
2- Inverta a ordem das palavras em uma string fornecida.
3-Verifique se uma string fornecida é um palíndromo _
(pode ser lida da mesma forma de trás para frente).
"""

primeiroNome = str(input("Digite o primeiro nome: "))
splitNome = primeiroNome.split()
ultimoNome = str(input("Digite o último nome: "))
invertido = " ".join(splitNome[::-1])

print(f"{ultimoNome}, {primeiroNome}\n")

print(f"Primeiro nome invertido: {invertido.lower()}\n")

if (primeiroNome.lower().replace(" ", "") == invertido.lower().replace(" ", "")):
    print("Palíndromo")
else:
    print("Não é palíndromo")