cubes = {x: x**3 for x in range(1, 11)}
print(cubes)

words = ['apple', 'banana', 'kiwi']
word_length = {word: len(word) for word in words}
print(word_length)

keys = ['name', 'age', 'city']
values = ['Ravi', 25, 'Delhi']
my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)

nums = [1, 2, 3, 4, 5, 6]
even_squares = {x: x**2 for x in nums if x % 2 == 0}
print(even_squares)

d = {'a': 1, 'b': 2, 'c': 3}
swapped = {value: key for key, value in d.items()}
print(swapped)
