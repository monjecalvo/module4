dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
json_dictionary = {
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": True,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": None,
}


dictionary["cat"] = "misifu"
dictionary.update({"birds" : "jacinto"})
for elem in dictionary:
    print(dictionary[elem])

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
print(dictionary["cat"])
print(json_dictionary["address"]["state"])
print(json_dictionary["phoneNumbers"][1]["number"])
print(json_dictionary["phoneNumbers"].append({"type":"private","number":"1234567891"}))