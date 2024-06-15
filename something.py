import json

dict1 = {
    "name": "kira",
    "age": 20,
    "status": "dead",
}
with open("something.json", "w") as dumpfile:
    json.dump(dict1, dumpfile, indent=4)
