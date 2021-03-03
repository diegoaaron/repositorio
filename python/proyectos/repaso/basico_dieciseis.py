try:
    print(value)
except Exception as e:
    print("Something went wrong")
    print(e)


i = 5
if i < 6:
    raise Exception("Number below 6 are not allowed")