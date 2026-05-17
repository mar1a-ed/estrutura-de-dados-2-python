list = [None, None, None, None, None, None, None, None, None, None]

import funcoes as fc

fc.add("Bob", list)

print(list)

print(fc.hash_function("Maria"))

fc.add("Maria", list)

print(list)

print(fc.hash_function("Artur"))

fc.add("Artur", list)

print(list)

print(f"Contains 'Artur' ? : {fc.contains("Artur", list)}")
print(f"Contains 'Pete' ? : {fc.contains("Pete", list)}")