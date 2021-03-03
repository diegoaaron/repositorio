import json

json_string = '{ "user_name":"Sharvin", "age":1000 }'
print(type(json_string))

data = json.loads(json_string)
print(type(data))

print(data)

jsonString = json.dumps(data)
print(type(jsonString))

