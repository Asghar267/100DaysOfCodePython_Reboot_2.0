print("Day 16 JSON = JavaScript Object Notation\n")

import json

"""JSON stands for JavaScript Object Notation, which is a widely used data format for
   Data interchange on the web."""

# print(dir(json))
print("\n Serializing JSON: ")
# {key:value mapping}
a = {"name": "John",
     "age": 31,
     "Salary": 25000}

b = json.dumps(a)  # conversion dict to JSON done by dumps() function
print(b, "\n")

print(json.dumps(['Welcome', "to", "100 days of python"]))  # list conversion to Array
print(json.dumps(("Welcome", "to", "100 days of python")))  # tuple conversion to Array
print(json.dumps("Hi"))  # string conversion to String

var = {"subject": {"math": 57, "physics": 78}}
with open("Sample.json", "w") as p:
    json.dump(var, p)  # dump() used for writing in file

print("\n Deserializing JSON")
c = json.loads(b) # JSON into Python Object
print(c)

with open("Sample.json", "r") as read_file:
    b = json.load(read_file)
print(b)


print("\n  pretty printed JSON")
# The indent parameter specifies the spaces that are used at the beginning of a line.
# The separator argument of a json.dump method you can specify any separator between key and value.
developer = {
    "name": "jane doe",
    "salary": 9000,
    "skills": ["Raspberry pi", "Machine Learning", "Web Development"],
    "email": "JaneDoe@pynative.com"
}

with open("developerPrettyPrint.json", "w") as write_file:
    json.dump(developer, write_file, indent=4, separators=(", ", ": "), sort_keys=True)
print("Done writing pretty printed JSON data into a file")

with open("developerPrettyPrint.json", "r") as read_file:
    b = json.load(read_file)
print(b)

print("\n Some exercise")
# Exercise 1: Access the value of key2 from the following JSON
sampleJson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sampleJson)
print(data['key2'], "\n")

# Exercise 2: PrettyPrint following JSON data
sampleJson = {"key1": "value1", "key2": "value2"}
data = json.dumps(sampleJson, indent=4, separators=(",", " = "))
print(data, "\n")

# Exercise 3: Sort JSON keys in and write them into a file
sampleJson = {"id": 1, "name": "value2", "age": 29}
with open("sampleJson.json", "w") as write_file:
    json.dump(sampleJson, write_file, indent=4, sort_keys=True)
    print("Done writing JSON data into a file")

print("\n")

# Exercise 4: Access the nested key ‘salary’ from the following JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

print(data['company']['employee']['payble']['salary'],"\n")
