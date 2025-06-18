# Theme - Fundamental of Input, Output, Conditions and Loops

# Problem 1 - Smart Calculator
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Divide by zero error"

operation = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

def smart_calculator(a: float, b: float, op: str):
    if op in operation:
        return operation[op](a, b)
    else:
        return "Invalid operator"

print(smart_calculator(1.5, 2.5, '+'))


# Problem 2 - Numbers to WOrds
operation = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine',
    '0' : 'Zero'
}

def number_to_words(n: int) -> str:
    num = str(n)
    new_str = ""
    for char in num:
        if char in operation:
            new_str = new_str +" " + operation[char]
    
    return new_str.strip()

print(number_to_words(123))

# Problem 3 - Strong Password Validation
def password_strength(password: str) -> str:
    if len(password) < 8:
        return "Weak"
    
    has_upper = False
    has_lower = False
    has_digits = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digits = True
        elif not char.isalnum():
            has_special = True
    
    if has_upper and has_digits and has_lower and has_special:
        return "Strong"
    else: return "Medium"

print(password_strength("Pass@123"))


# Problem 4 - Digit Pattern Extractor
def even(n: int) -> list:
    num = str(n)
    even_list = []
    for i in num:
        if int(i) % 2 == 0:
            even_list.append(int(i))
    
    return even_list

def odd(n: int) -> list:
    num = str(n)
    odd_list = []
    for i in num:
        if int(i) % 2 != 0:
            odd_list.append(int(i))
    
    return odd_list

def total_digits(n: int) -> int:
    num = str(n)
    return len(num)
    

def digit_analysis(n: int) -> dict:
    output = {
        "even": even(n),
        "odd" : odd(n),
        "total digits" : total_digits(n)
    }
    
    return output

print(digit_analysis(1234567))


# Problem 5: Mini ATM Interface (Elite)
def atm():
    amt = 10000
    display = """
    Choose an option :-
        1. Check Balance
        2. Withdraw Amount
        3. Deposit Amount
        4. exit
    """ 
    print(display)
    
    while True:
        choice = int(input("Enter your choice:- "))
        if choice == 2:
            withdraw = int(input("Enter amount to withdraw :- "))
            if amt>withdraw:
                amt -= withdraw
                print("Amount '{}' withdrawn successfully.".format(withdraw))
                print("Remaining Amount :- {}".format(amt))
            else:
                print("Insufficient Amount...")
                
        elif choice == 3:
            deposit = int(input("Enter Amount to deposit :- "))
            print("Amount '{}' deposited successfully...".format(deposit))
            amt += deposit
            print("Total Amount :- {}".format(amt))
        
        elif choice == 1:
            print("Balance:- {}".format(amt))
            
        else:
            break
    
atm()

# <-------------------------- Suggestions ----------------------------->

# In problem 2 - we can use list + join() -> faster, cleaner
# words = [operation[char] for char in str(n)]
# return " ".join(words)  
# Why? We're building a string inside a loop - this becomes inefficient as size grows


# In Problem 3 - Can be combine into single line
# return "Strong" if all([has_upper, has_lower, has_digits, has_special]) else "Medium"


# In Problem 4 - perfect, can use filter() or list comprehension to practive alternative patterns
# even_list = [int(i) for i in str(n) if int(i) % 2 ==0]


# In problem 5 - Add Basic Validation
# if withdraw > amt:
#     print("Insufficient funds.")
#     continue


# | Skill                      | Where You Used It  |
# | -------------------------- | ------------------ |
# | Function dispatch          | Smart calculator   |
# | Mapping numbers to strings | number\_to\_words  |
# | Password logic pattern     | password\_strength |
# | Loop + list building       | digit\_analysis    |
# | CLI app structure          | ATM                |


# <-------------- BONUS CHALLENGE ------------------------------------->
# Expense Tracker (CLI App) - Apply what we learned

# Build a simple terminal-based app to:
#     - Add expenses (amount, category, note)
#     - Show total expenses
#     - Filter by category
#     - Exit

# Use:
#     - Dictionary/List for storage
#     - Loop for menu
#     - Functions for modularity