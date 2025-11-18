names = ["a", "b", "c"]
for index, value in enumerate(names):
    print(index, value)


fruits = ["apple", "banana", "cherry"]
for i, f in enumerate(fruits, start=1):
    print(i, f)

s = "python"
for index, ch in enumerate(s):
    print(index, ch)

result = list(enumerate(["a", "b", "c"]))
print(result)
