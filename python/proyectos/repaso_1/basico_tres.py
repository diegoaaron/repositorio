for i in range(3):
    print("Hello")


for i in range(1, 3):
    print("Hello 2 ")


for i in range(3):
    print("Hello 3 ")
else:
    print("Finished")

for i in range(3):
    for j in range(2):
        print("\t Inner loop")
    print("Outer loop")


for i in range(3):
    pass


i = 0
while i < 5:
    print("Number", i)
    i += 1

i = 0
while i < 5:
    if i == 4:
        break
    print("Number ", i)
    i += 1


i = 0
while i < 5:
    print("Number ", i)
    i += 1
else:
    print("Number is greater than 4")

i = 0
while i < 6:
    i += 1
    if i == 2:
        continue
    print("Number", i)
    print("Salto", i)

    