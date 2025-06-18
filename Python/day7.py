# # <--------------- Problem 1 : String Manipulation and Cleaning ------------->
# # 1.1 - Remove extra spaces
# def remove_spaces(text: str) -> str:
#     text = text.strip().split()
#     text = ' '.join(text)

#     return text

# print(remove_spaces("   Hello    world    "))


# # 1.2 - swap case of each character
# def swap_case(text: str) -> str:
#     texts = ""
#     for char in text:
#         if char.isupper():
#             char = char.lower()
#         elif char.islower():
#             char = char.upper()
            
#         texts = texts + char
    
#     return texts

# print(swap_case("HUR@IN"))

# # 1.3 - Count Digits, Letter, Spaces
# # We can use .get() method, counter from collection method right but let's not use that right now for a moment will explore later
# def count_digits_numbers_spaces(text: str) -> dict:
#     letters = 0
#     digits = 0
#     spaces = 0
#     space = 0
    
#     for char in text:
#         if char.isdigit():
#             digits += 1
        
#         elif char.isupper() or char.islower():
#             letters += 1

#         elif char.isspace():
#             space += 1
    
#     output = {'letters': letters, 'digits': digits, 'spaces': space}
    
#     return output

# print(count_digits_numbers_spaces("Hello    123!"))

# # 1.4 - Normalize Email text
# def normalize_email(email: str) -> str:
#     return email.strip().lower()

# print(normalize_email("   HELLO@GMAIL.COM   "))

# # 1.5 - Remove All HTML tags from String
# # Can use regular expression 
# # def remove_html_tags(text: str) -> str:
# #     new_text = ""
# #     for char in text:
# #         if char == "<":
# #             index = text.index(char)
# #             print(index)
# #             new_text = new_text + text[index + 3:]
# #     print(new_text)
            
# #     return new_text

# import re

# def remove_html_tags(text: str) -> str:
#     clean_text = re.sub(r'<[^>]*>', '', text)
#     return clean_text

# print(remove_html_tags("<p>Hello <b>World</b></p>"))


# # <--------------- Problem 2 Loops and Math Logic ---------------->
# # 2.1 - Print First N even numbers
# def first_even_numbers(n: int) -> int:
#     num = [x for x in range(1, n*2+1) if x % 2 == 0]
#     # num = [x * 2 for x in range(1, n+1)]
#     print(num, end="")
    
# first_even_numbers(5)

# # 2.2 - Sum of digits of numbers
# def sum_of_digits(num: int) -> int:
#     num = str(num)
#     total = 0
#     for char in num:
#         total += int(char)
    
#     return total

# print(sum_of_digits(1234))

# # 2.3 - Check if Number is Prime
# def check_prime(num: int) -> bool:
#     if num <=1:
#         return False

#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
    
#     return True

# print(check_prime(17))

# # 2.4 - Print all prime<= N
# def prime(n: int):
#     if n <= 1:
#         return "Prime of 1 or less than 1 doesn't exist"
    
#     # Logic
                
# prime(20)

# # 2.5 - Prime Factorization  - Review it and try to build own logic( alternative)
# def prime_factors(n: int) -> list:
#     factors = []
#     # Check divisibility by 2 first
#     while n % 2 == 0:
#         factors.append(2)
#         n //= 2
    
#     # Check odd numbers up to sqrt(n)
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         while n % i == 0:
#             factors.append(i)
#             n //= i
    
#     # If n is still greater than 1, it's prime
#     if n > 1:
#         factors.append(n)
    
#     return factors

# # Example usage:
# num = 100
# print(prime_factors(num))  # Output: [3, 7]
    

# # <--------------------- Problem 3 :- Lists and Data Processing
# # 3.1 - sum of all elements
# def sum_of_elements(lst: list) -> int:
#     return sum(lst)

# print(sum_of_elements([1,2,3]))

# # 3.2 - Seocond Largest elements
# # I use manual soring technique here - We can use in build methos .sort() for sorting
# def second_largest(lst: list) -> int:
#     for i in range(len(lst)):
#         if lst[i-1] < lst[i]:
#             x = lst[i-1]
#             lst[i-1] = lst[i]
#             lst[i] = x
#     return lst[-2]
# print(second_largest([1,4,7,2,5]))

# # 3.3 - Remove Duplicates (Preserve order)
# # Can use dict.fromkeys(), .get() method, set()- not preserved, manually
# def remove_duplicate(input_list: list) -> list:
#     new_list = []
#     for element in input_list:
#         if element not in new_list:
#             new_list.append(element)
    
#     return new_list

# print(remove_duplicate([1,2,2,3,3,4]))

# # 3.4 - All numbers occuring more than once   -   Have Bugs
# def more_occurence(lst: list) -> list:
#     new_lst = []
    

# print(more_occurence([1,2,2,3,3,4]))

# # 3.5 - Rotate list bt K places   -   Have Bugs
# def rotate_list(lst: list, k: int) -> list:
#     for i in lst:
#         x = lst[i]
#         if i+k > len(lst)-1:
#             new = (i+k)-(len(lst))
#             lst[i] = lst[new]
#         else:
#             lst[i] = lst[i+k]
    
#     return lst

# print(rotate_list([1,2,3,4,5], 2))

# <------------------ Problem 4 :- Dictionary and Frequency ------------>
# 4.1 - Create dict from two list
def create_dict(keys: list, values: list) -> dict:
    if len(keys) == len(values):
        for i in range(len(keys)):
            dict = {keys[i]: values[i]}
    
    print(dict)
    
create_dict(keys = ['a', 'b'], values = [1, 2])