users = {
    "id" : 1,
    "name" : "Leanne Graham",
    "username" : "Bret",
    "email" : "Sincere@april.biz",
    "address" : {
        "street" : "Kulas light",
        "suite" : "Apt. 556",
        "city" : "Gwenborough",
        "zipcode" : "92998-3874",
        "geo" : {
                "lat" : "-37.3159",
                "lng" : "81.1496"
                    }
            }
} #jangan menggunakan angka agar dapat dijadikan Json
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print(users)
print(type(users))#cek tipe data
print("'nUbah dict ke Json")
import json #ubah python dict ke json
result = json.dumps(users)
print(type(result))#cek tipe data
print(result)

with open('result.json', 'w') as file:
    json.dump(users, file)

