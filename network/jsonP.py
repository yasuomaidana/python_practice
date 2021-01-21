import json
data='''{
    "name":"Chuck",
    "phone":{ 
        "type":"intl",
        "number":"+1 734 303 4456"
    },
    "email":{
        "hide":"yes"
        }
}
'''
data2='''[ "Glenn", "Sally", "Jen" ]'''
info = json.loads(data)
print(type(info))
print("Name:",info["name"])
print("Hide:",info["email"]["hide"])
info = json.loads(data2)
print(info)
