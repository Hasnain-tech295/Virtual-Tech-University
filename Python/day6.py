# Problem 1:- Valid Email checker

def is_valid_email(email: str) -> bool:
    count1 = 0
    count2 = 0
    
    for char in email:
        if char == "@":
            count1 += 1
        
        elif char == ".":
            count2 += 1
    
    if (count1 > 1 or count2 < 1) or (email[0] == "@" or email[-1] == "@" or email[0] == "." or email[-1] == "."):
        return False
    
    return True

# Alternative way - using built in functions
# def is_valid_email(email: str) -> bool:
#     if email.count("@") != 1:
#         return False

#     at_index = email.find("@")
    
#     # '.' must be after '@' and not at the end
#     if '.' not in email[at_index:] or email.startswith("@") or email.endswith("@") or email.endswith("."):
#         return False

#     return True


def test():
    assert is_valid_email("a@b.com") == True
    assert is_valid_email("a@b") == False
    assert is_valid_email("@domain.com") == False
    assert is_valid_email("test@domain..com") == True  # still okay here

    print("all test cases passed")

test()

# Problem 2 :- Even and Odd digits in a Number.
def count_even_odd_digits(n: int) -> tuple:
    even_count = 0
    odd_count = 0
    
    total = len(str(n))
    
    for char in str(n):
        if int(char) % 2 == 0:
            even_count += 1
    
    odd_count = total - even_count
    
    return (even_count, odd_count)

# Shorter Logic
# def count_even_odd_digits(n: int) -> tuple:
#     digits = [int(d) for d in str(n)]
#     even = sum(1 for d in digits if d % 2 == 0)
#     return (even, len(digits) - even)


def test_counter():
    assert count_even_odd_digits(12345) == (2, 3)
    assert count_even_odd_digits(2468) == (4, 0)
    assert count_even_odd_digits(25784568) == (5, 3)

    print("All test cases passed.")

test_counter()


# Problem 3:- Remove duplicates from List (Preserve order)
# We can use set but may be order will not be preserve
# Can use List Comprehension - preserve order - just compact version of our for loop below
# Can use Dictionary fromkeys() - preserve order : using dict.fromkeys() we can create a dict with unique value and convert back to list
def remove_duplicates(data: list) -> list:
    res = []
    
    for val in data:
        if val not in res:
            res.append(val)
    
    print(res)
    
    return res

def test_duplicate():
    assert remove_duplicates([1, 1, 2, 2, 3]) == [1, 2, 3]
    assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
    print("All test cases passed successfully.")

test_duplicate()


# Problem 4:- Count Words Longer Than N Characters
def count_long_words(text: str, n: int) -> int:
    texts = text.split()
    count = 0
    
    for word in texts:
        print(word)
        if len(word) > n:
            count += 1
    
    print(texts)

    return count

# More Pythonic
# def count_long_words(text: str, n: int) -> int:
#     return sum(1 for word in text.split() if len(word) > n)


# Inside function I am printing outputs at differnt positions to trace whether I am getting the desired output - on which I build my logic

def test_long_word():
    assert count_long_words("I love programming", 4) == 1
    assert count_long_words("This is quite interesting", 2) == 3
    print("All test cases passed successfully.")

test_long_word()


# Problem 5:- Password Strength Level
def password_strength(password: str) -> str:
    if len(password) < 8:
        return "Weak"

    has_digit = False
    has_alpha = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_alpha = True
        elif not char.isalnum():
            has_special = True

    if has_alpha and has_digit and has_special:
        return "Strong"
    elif has_alpha and has_digit:
        return "Medium"
    else:
        return "Weak"
        
        
assert password_strength("abc123") == "Weak"
assert password_strength("abc12345") == "Medium"
assert password_strength("abc12345@") == "Strong"


# Bonus Challenge
