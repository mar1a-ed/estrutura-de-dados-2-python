fruits = ["apple", "banana", "orange", "strawberry", "lemon"]

print(f"Lista: {fruits}")

print(f"Comprimento da lista: {len(fruits)}")

print(f"Tipo: {type(fruits)}")

print(f"Primeiro elemento: {fruits[0]}")

print(f"Ultimo elemento: {fruits[-1]}")

print(fruits[2:4])

print(fruits[:3])

if "apple" in fruits:
    print("Yes, apple in fruits")

fruits.append("pineapple") #insere 'pineapple' no fim da lista

fruits.insert(1, "fish") #insere 'fish' no indice 1

print(fruits)

if "banana" in fruits: #se existir 'banana' na lista, remove
    fruits.remove("banana")

fruits.pop(3) #deleta o elemento do indice 3 da lista

fruits.pop() #deleta o ultimo elemento da lista

del fruits #deleta a lista inteira