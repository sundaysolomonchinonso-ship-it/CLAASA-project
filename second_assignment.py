#Creating an empty list
list_1 = []
list_2 = []

# Populate List_1
while True:
    value = input(f"Enter value for list_1: ")
    list_1.append(value)

    user_done = input("Are you done? yes/no: ").lower()
    if user_done == "yes":
        break

# Populate List_2
while True:
    value = input(f"Enter value for list_2: ")
    list_2.append(value)

    user_done = input("Are you done? yes/no: ").lower()
    if user_done == "yes":
        break

#Checking if lengths match
if len(list_1) != len(list_2):
    print("\nlength of lists don't match")
else:
    print("\nlengths match. Proceeding...")

    for i in range(3):
        print(".")
        

    # Create dictionary
    my_dict = dict(zip(list_1, list_2))

    print("\nDictionary Created:")
    print(my_dict)