def hash_function(value):
    sum_of_chars = 0

    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10

def add(name, list):
    index = hash_function(name)
    list[index] = name

def contains(name, list):
    index = hash_function(name)
    return list[index] == name

