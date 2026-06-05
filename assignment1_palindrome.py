# ==========================================
# ASSIGNMENT 1: PALINDROME CHECKER
# ==========================================

# List provided for the palindrome check
My_list = [
    'mummy',
    'hannah',
    'murder for a jar of red rum',
    'mom',
    'seagull',
    'tomato',
    'no lemon, no melon',
    'some men interpret nine memos',
    'madam'
]

# Check each item in the list
for item in My_list:

    # Remove spaces, punctuation and normalize case
    cleaned = ""

    for char in item:
        lower_char = char.lower()

        # Keep only alphabetic characters
        if lower_char in "abcdefghijklmnopqrstuvwxyz":
            cleaned = cleaned + lower_char

    # Reverse the cleaned text
    reversed_cleaned = cleaned[::-1]

    # Compare original cleaned text with its reverse
    if cleaned == reversed_cleaned:
        print(item + " is Palindrome")
    else:
        print(item + " is not a palindrome")