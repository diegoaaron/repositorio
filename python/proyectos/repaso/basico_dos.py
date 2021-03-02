number = 5

if number == 10:
    print("Number is 10")

elif number < 10:
    print("Number is less than 10")

else:
    print("Number is more than 10")


is_available = True

if is_available:
    print("Yes, it is available")

else:
    print("Not available")

if not is_available:
    print("Not available")

else:
    print("Yes it is available")

data = None

if data:
    print("data is not none")

else:
    print("data is none")


num_a = 10
num_b = 5

if num_a > num_b: print("num_a is greater than num_b")

print("num_a is greater than num_b") if num_a > num_b else print("num_a is less than num_b")

num = 5
print("Number is five") if num == 5 else print("Number is not five")

num = 25

if num > 10:
    print("Number is greater than 10")
    if num > 20:
        print("Number is greater than 20")
    if num > 30:
        print("Number is greater than 30")

else:
    print("Number is smaller than 10")

num = 10

if num > 5 and num < 15:
    print(num)
else:
    print("Number may be small than 5 or larger than 15")

num = 10

if num > 5 or num < 7:
    print(num)

