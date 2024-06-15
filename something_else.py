import json

with open("something_else.json", "r") as file:
    data = json.load(file)

print(data['BOB'])
