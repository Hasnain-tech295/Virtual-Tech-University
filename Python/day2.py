# # Theme :- String Manipulation, Validation and Loop Patterns (Real World Inspired)
# # "Think like a Builder. Code like a Craftsman"

# # Problem 1 :- Email Cleaner and Extractor - Regrex learn and comeback to solve

# import re

# data = """
# Hi team, please contact john.doe@example.com or jane_doe@sample.org for info. 
# Also cc: support@EXAMPLE.com, not_an_email@, or just text@.
# """

# def email_extractor(data: str) -> list:
#     return re.findall(r'[\w\.-_]+@[\w\.-]+', data)

# def remove_duplicates(data: str):
#     new = []
#     email = email_extractor(data)
#     for element in email:
#         if element not in new:
#             new.append(element)
        
#         element = element.split("@")
#         if element[1] == element[1].upper():
#             new.append(element)
    
#     return new        

# print(remove_duplicates(data))

# Problem 2 :- Sentence Analyzer Toolkit, Learning :- split(), max(), counter, dict usage, data summarization

def word_count(data: str) -> int:
    return len(data.split())

def character_count(data: str) -> int:
    new_data = ''.join(data.split())
    return len(new_data)

def longest_word(data: str) -> str:
    return max(data, key=len)
data = """
Batteries included Rich collection of already existing bricks of classic numerical methods, plot
ting or data processing tools. We don’t want to re-program the plotting of a curve, a Fourier
transform or a fitting algorithm. Don’t reinvent the wheel!
Easy to learn Most scientists are not paid as programmers, neither have they been trained so.
They need to be able to draw a curve, smooth a signal, do a Fourier transform in a few minutes.
Easy communication To keep code alive within a lab or a company it should be as readable
as a book by collaborators, students, or maybe customers. Python syntax is simple, avoiding
strange symbols or lengthy routine specifications that would divert the reader from mathematical
or scientific understanding of the code
"""

print(longest_word(data))