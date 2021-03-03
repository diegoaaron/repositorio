def my_decorator(func):
    def wrapper():
        print("Line number 1")
        func()
        print("Line number 3")
    return wrapper

@my_decorator
def say_hello():
    print("Hello I am line number 2")

say_hello()