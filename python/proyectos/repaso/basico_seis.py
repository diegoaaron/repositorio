def hello_world():
    print("Hello world")

hello_world()

def add(a, b):
    print(a + b)

add(3, 4)

def add2(*num):
    print(sum(num))

add2(1,2,3,4,5,6)

def user_details(username, age):
    print("Username is ", username)
    print("Age is ", age)

user_details("Sharvin", 100)

user_details(age=100, username="Sharvin2")

def user_details2(username, age=None):
    print("Username is: ", username)
    print("Age is ", age)

user_details2("Diego")

print("--------------------------")

def user(**username):
    print(username)

user(username1="xyz", username2="abc")

def user2(**user_details):
    print(user_details['username'])

user2(username="Sharvin", age=1010)

greet = "Hello World"

def testing():
    print(greet)

testing()

def add3(a, b):
    return a + b

print(add3(1, 3))
