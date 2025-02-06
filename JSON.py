import json

with open("test.json", "r") as json_file:
    a = json.load(json_file)

print(a)