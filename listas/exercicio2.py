numbers = [1, 22, 5, 71, 99, 81, 0]

maior = 0

for n in numbers:
    if n > maior:
        maior = n

menor = 0

for n in numbers:
    if n < menor:
        menor = n

print(f"O menor numero da lista eh: {menor}")
print(f"O maior numero da lista eh: {maior}")

