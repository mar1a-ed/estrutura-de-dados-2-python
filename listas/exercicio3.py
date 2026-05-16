
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []

qtdPar = 0

for n in numbers:
    if n % 2 == 0:
        pares.append(n)
        qtdPar += 1

print(f"A quantidade de numeros pares eh: {qtdPar}")
print(f"Os valores pares sao: {pares}")