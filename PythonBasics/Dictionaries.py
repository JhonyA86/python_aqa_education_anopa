# phonebook = {
#     "John" : 938477566,
#     "Jack" : 938377264,
#     "Jill" : 947662781
# }
# print(phonebook)

# phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
# for name, number in phonebook.items():
#     print(f"Phone number of {name} is {number}")


# phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
# del phonebook["John"]
# print(phonebook)


# Exercise
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
# my code goes here
phonebook["Jake"] = 938273443
del phonebook["Jill"]
print(phonebook)

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
