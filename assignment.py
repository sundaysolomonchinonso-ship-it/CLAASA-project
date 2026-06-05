# determination of palindrome using the following words, phrase in the list below.
dera_list =  ['mummy', 'hannah', 'murder for a jar of red rum', 'mom', 'seagull', 'tomato', 'no lemon, no melon', 'some men interpret nine memos', 'madam' ]
for z in dera_list:

    z_length = len(z)
    z_inverse = z[-1:-(z_length+1):-1]
    if z ==z_inverse:
            print(f"{z} is a palindrome")
    else:
            print(f"{z} is not a palindrome")