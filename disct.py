car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
y = car.values()
print(y)
print(x) #before the change

car["color"] = "white"

print(x) #after the change

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

students = {
    "Alice": {"age": 25, "course": "Python"},
    "Bob": {"age": 22, "course": "Java"},
    "Charlie": {"age": 23, "course": "C++"}
}
for name, info in students.items():
    print(name, "->", info)
