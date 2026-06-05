my_list = [
    'mummy','hannah','murder for a jar of red rum','mom',
    'seagull','tomato','no lemon','no melon',
    'some men interpret nine memos','madam']

for item in my_list:
    cleaned = item.replace(" ", "")
    
    if cleaned == cleaned[::-1]:
        print (item, "is Palindrome")
    else:
        print (item, "is not a Palindrome")
        