def my_decorator(func):
    def wrapper():
        print("Line Number 1")
        func()
        print("Line Number 3")
    return wrapper

def say_hello():
    print("Hello I am line Number 2")


say_hello = my_decorator(say_hello)

print(say_hello)

say_hello()