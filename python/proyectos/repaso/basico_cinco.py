data = [1, 5, "xyz", True]
print(data[1])

print(data[2:4])

data.append("Hello")
print(data)

data[2] = "abc"
print(data)

data.remove("Hello")
print(data)

for i in data:
    print(i)

if 'abc' in data:
    print("yess..")

List2 = data.copy()
print(List2)

print(len(data))

list1 = [1, 4, 6, "hello"]
list2 = [2, 8, "bye"]
print(list1 + list2)

data = (1, 3, 5, "bye")
print(data)

print(data[3])

print(data[2:4])


data = (1, 3, 5, "bye")
data_two = list(data)
data_two[1] = 8
data = tuple(data_two)
print(data)

# sets - no se indexan ni estan ordenados ni se puede cambiar sus valores definidos
data = { "hello", "bye", 10, 15}
print(data, "type: ", type(data))

for i in data:
    print(i)

data.add("test")
print(data)

print(len(data))

data.remove("test")
print(data)

