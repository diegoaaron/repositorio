name = input("Enter your name: ")
print(name)

date = input("Toda's date: ")
print(type(date))

date_to_int = int(date)
print(type(date_to_int))

date = 12
date_to_float = float(date)
print(type(date_to_float))

date = 12
date_to_string = str(date_to_float)
print(type(date_to_string))

date = 22.0
date_to_int = int(date)
print(type(date_to_int))

user_details = {
    "fname": "Sharvin",
    "lname": "Shah",
    "profession": "Developer"
}

print(user_details['fname'])
print(user_details.get('fname'))

# probando con una llave que no existe

age = user_details.get('age')
print(age)

if "age" in user_details.keys():
    print("Yes it is present")
else:
    print("Not present")

user_details = {}

if user_details:
    print("Not empty")
else:
    print("Empty")

print(bool(user_details))

user_details = {
    "fname": "Sharvin"
}

print(bool(user_details))

user_details["profession"] = "Software Developer"
print(user_details)

user_details["profession"] = "Software Developer 2"
print(user_details)