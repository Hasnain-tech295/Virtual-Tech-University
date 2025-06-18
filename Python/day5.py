# # Number Patterns, Looping Logic & Formatting -> used in AI, GenAI prompt Template, low level matrix-manipulation

# # Problem 1 :- Multiplication table from 1 to 10

# def multiplication_table(n: int):
#     for i in range(1, 11):
#         result = "{} X {} = {}".format(n, i, n * i)
        
#         # Can use f-string better and readable
        
#         print(result)

# n = int(input("Type number to get multiplication table:- "))
# multiplication_table(n)        


# # Problem 2 :- Right angle triangle of stars

# def stars(n: int):
#     for i in range(1, n+1):
#         pattern = i * "*"
#         print(pattern)

# n = 4
# stars(n)

# Problem 3 :- FizzBuzz (Classic Interview Q)
def fizzbuzz(n: int):
    for i in range(1, n+1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        
        elif (i % 3 == 0):
            print("Fizz")
        
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i) 
    
n = 15
fizzbuzz(n)

# Problem 4 :- Central Pyramid Pattern of Stars


# Problem 5 :- Number Pyramid


# Try to solve atleast 20 Pattern Problems
