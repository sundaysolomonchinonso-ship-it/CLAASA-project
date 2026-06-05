# ==========================================
# ASSIGNMENT 3: TWO LISTS INTO A DICTIONARY
# ==========================================

import time

# ==========================================
# STEP 1: COLLECT ITEMS FOR LIST 1
# ==========================================

list1 = []

print("=== Let's fill up List 1 ===")

while True:
    item = input("Enter an item: ")
    list1.append(item)

    # Normalize user input
    done = input("Are you through? (yes/no): ")
    done = done.lower().strip()

    if done == "yes":
        break

    elif done == "no":
        continue

    else:
        print("")
        print("Invalid input! You must enter 'yes' or 'no'.")
        print("Starting afresh for List 1...")
        print("")

        # Restart List 1
        list1 = []

        print("=== Let's fill up List 1 ===")

# ==========================================
# STEP 2: COLLECT ITEMS FOR LIST 2
# ==========================================

list2 = []

print("")
print("=== Let's fill up List 2 ===")

while True:
    item = input("Enter an item: ")
    list2.append(item)

    done = input("Are you through? (yes/no): ")
    done = done.lower().strip()

    if done == "yes":
        break

    elif done == "no":
        continue

    else:
        print("")
        print("Invalid input! You must enter 'yes' or 'no'.")
        print("Starting afresh for List 2...")
        print("")

        # Restart List 2
        list2 = []

        print("=== Let's fill up List 2 ===")

# ==========================================
# STEP 3: VERIFY BOTH LISTS HAVE SAME LENGTH
# ==========================================

if len(list1) != len(list2):
    print("length of lists don't match")

else:
    # Display a short loading effect
    print("lengths match. Proceeding", end="")

    for i in range(3):
        time.sleep(1)
        print(".", end="", flush=True)

    print("")

    # ==========================================
    # STEP 4: CREATE THE DICTIONARY
    # ==========================================

    my_dict = {}

    # Use matching indexes from both lists
    for i in range(len(list1)):
        key = list1[i]
        value = list2[i]

        my_dict[key] = value

    print("")
    print("Here is your dictionary:")
    print(my_dict)
    