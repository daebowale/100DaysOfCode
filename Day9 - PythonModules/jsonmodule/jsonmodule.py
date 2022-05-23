# Javascript object notation ( JSON ) Module

# JSON is a technique to send the data. Same as web protocol. You can call / send / receive the data using JSON.
# JSON is written in { ... } . And you can not add a comment in JSON
import json

data = '{"Name":"Datt Panchal", "Age" : 17}'

# print(data)
# You cannot access the JSON data using print
# print(data['Name'])
# print(data['Age'])

# json.loads() parse the data
parsed = json.loads(data)
print(parsed)
print(type(parsed)) # dict

# You can access the JSON data using loads()
print(parsed['Name'])
print(parsed['Age'])

data2 = {
    "employee": "John",
    "Role": ['Python Programmer', "Web Developer"]
}

# json.dumps() returns a javascript compotable object
jscomp = json.dumps(data2)
print(jscomp)

# You can explore more module function on documentation