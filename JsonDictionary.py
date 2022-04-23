import json

# Dictionary {}
data = '''{
    "name" : "chuck",
    "phone" : {
        "type" : "int1",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print("Name: ", info["name"])
print("Hide: ", info["email"]["hide"])
