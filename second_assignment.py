import time
list1 = []
list2 = []
print("Enter items for list 1:")
while True:
    item = input("Enter item: ")
    list1.append(item)
    done = input("Are you through? (yes/no): ")
    if done.lower() == 'yes':
        break
print("Enter items for list 2:")
while True:
        item = input("Enter item: ")
        list2.append(item)
        done = input("Are you through? (yes/no): ")
        if done.lower() == 'yes':
            break
        if len(list1) != len(list2):
            print("length of lists don't match")
        else:
            print("lengths match. proceeding")
            
            print("list1 =", list1)
            print("list2 =", list2)
            
            for i in range(3):
                time.sleep(1)
                print(".")
                
            my_dict = dict(zip(list1, list2))
            print(my_dict)