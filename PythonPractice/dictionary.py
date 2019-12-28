# Create a dictionary to hold car models
car_model = {
    "brand": "Ford",
    "model": "Mustange",
    "year": 1964
}

# Get the value of the "brand" key:
print("Get the value of the brand key:")
x = car_model["brand"]
print(x)
# There is also a method called get() that will give you the same result:
print("There is also a method called get() that will give you the same result:")
x = car_model.get("model")
print(x)


# Change Values
# Change the "year" to 2018:
print("Change the year to 2018:")
x = car_model["year"]
print(x)
car_model["year"] = 2018
x = car_model["year"]
print(x)


# Loop through a Dictionary:
# Print all key keys in the dictionary, on by one:
print("Print all key names in the dictionary, on by one:")
for x in car_model:
    print(x)

# Print all values in the dictionary, on by one:
print("Print all values in the dictionary, on by one:")
for x in car_model:
    print(car_model[x])

# You can also use the values() fuction to return values of a Dictionary:
print("You can also use the values() fuction to return values of a Dictionary:")
for x in car_model.values():
    print(x)

# You can also loop through both keys and values by using the items() function:
print("You can also loop through both keys and values by using the items() function:")
for x, y in car_model.items():
    print(x, y)

# To determine if a specified key is present in a dictionary use the in keyword:
print("# To determine if a specified key is present in a dictionary use the in keyword:")
if "model" in car_model:
    print("Yes, 'model' is one of the keys in the car_model dictionary")

# To determine how many items (key-value pairs) a dictionary has, use the len() method:
print("To determine how many items (key-value pairs) a dictionary has, use the len() method:")
print(len(car_model))

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
print("Adding an item to the dictionary is done by using a new index key and assigning a value to it:")
car_model["color"] = "red"
print(car_model)