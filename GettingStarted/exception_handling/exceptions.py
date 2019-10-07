# the following code will generate a KeyError
# student = {
#     "name": "Mark",
#     "student": 15163,
#     "feedback": None
# }

# last_name = student["last_name"]

# the following code will have a try/except block to handle the error more gracefully
# student = {
#     "name": "Mark",
#     "student": 15163,
#     "feedback": None
# }

# try:
#     last_name = student["last_name"]
# except KeyError:
#     print("Error finding last_name")

# # to make sure our try/except works we will print something outside of the block
# print("This code executes!")

# the following code will also check for a TypeError

# student = {
#     "name": "Mark",
#     "student": 15163,
#     "feedback": None
# }

# student["last_name"] = "Kowalski"

# try:
#     last_name = student["last_name"]
#     numbered_last_name = 3 + last_name
# except KeyError:
#     print("Error finding last_name")
# except TypeError:
#     print("I can't add these two together")
# except Exception:
#     print("Unknown error")

# # to make sure our try/except works we will print something outside of the block
# print("This code executes!")

# the following code will help identify where the error is when adding a try/except by using "as error: and printing the error"
student = {
    "name": "Mark",
    "student": 15163,
    "feedback": None
}

student["last_name"] = "Kowalski"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last_name")
except TypeError as error:
    print("I can't add these two together")
    print(error)
except Exception:
    print("Unknown error")

# to make sure our try/except works we will print something outside of the block
print("This code executes!")