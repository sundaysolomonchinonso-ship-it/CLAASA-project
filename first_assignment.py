my_list = ['mummy', 'hannah', 'murder for a jar of red rum', 'mom',
           'seagull', 'tomato', 'no lemon, no melon',
           'some men interpret nine memos', 'madam']

for list in my_list:
    formatted_text = list.replace(" ", "")

    if formatted_text == formatted_text[::-1]:
        print(list, "is Palindrome")
    else:
        print(list, "is not a palindrome")
derah_list = ['mummy', 'hannah', 'murder for a jar of red rum', 'mom', 'seagull', 'tomato', 'no lemon' 'no melon', 'some men interpret nine memos', 'madam']
for item in derah_list:
    stripped = item.replace('', '').replace(',', '').lower()
    if stripped == stripped[::-1]:
        print(f"{item} is a palindrome")
else:
    print(f"{item} is not a palindrome")
