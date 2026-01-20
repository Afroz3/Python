#json is a syntax used for storing or exchanging data
#import json
#converting json into python
'''x = '{"name":"john","age":22,"city":"wgl"}'
y = json.loads(x)
print(y["age"])'''
#converting from python to json
'''import json
x= {
    "name":"john",
    "age":22,
    "city":"wgl"
}
y = json.dumps(x)
print(y)'''
#convert python objects into json strings, and print the values
'''import json
print(json.dumps({"name":"john","age":22}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple","bananas")))
print(json.dumps("hello"))
print(json.dumps(23))'''



