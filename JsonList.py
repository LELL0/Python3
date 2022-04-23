import json

# list []
input = '''[
    {   "id" : "001",
        "x" : "2",
        "name" : "chuck"
    },
    {   "id" : "009",
        "x" : "7",
        "name" : "chuck"
    }
]'''

info = json.loads(input)
print("Users count: ", len(info))
for item in info:
    print('\nName: ', item['name'])
    print('id: ', item['id'])
    print("Attribute: ", item['x'])
