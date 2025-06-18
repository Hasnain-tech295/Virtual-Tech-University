# Problem 1 : Smart Calculator
This problem is specifically asked for dictionary dispatching right not the if-elif-else chaining.<br>
**Dictionary patching** - refers to use dictionary to map input value to function allow for dynamic function calling based on input.
Like we did in our problem <br>
## How I solve it.
1. I defined functions for each operation: add, subtract, etc.
2. Used a dictionary to map operator symbols to functions.
3. Took user input and checked whether that particular operator is in our dictionary or not
4. Called the correct function using the operator.
<br>

## Code Explanation 
def add(a, b) 
def sub(a,b)
...........
...........
*Here we simply define function which takes two parameters (a,b) and return the output*<br>

operation = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}
*Here we define a dictionary with operators as key and corresponding functions name as value which will help us in dynamic function call*<br>

def number_to_words(a: float, b: float, op: str):
*Here we define our function function which contains three parameters/arguments and their data types. Defining data types and return types earlier in func definition helps in debugging.*<br>

*Inside our function we are checking whether an op(operator) passed by user via function calling is exist in operation{} or not. If exist then will assign value of that particular key and then our mathematical function will run and return output*

## Alternatives 
*Yep, We can use if-elif-else chain to get the same result.*<br>
*Can use match-case as well*<br>

# Problem 2 : Number to Words
## How I solve it
1. First, I simply define a dictionary i.e., digits as key and number in words as value
2. We define our function which will take one argument (n) of type 'integer' and will return a 'string'
3. Inside my function : I covert my 'integer' to 'string' because I want to use iteration and integer in not iterable but string is.Then we iterate over each character of string. If the character is in our operation dictionary we are getting our value considering char as key and then adding/concatenating all the stuff together and that's done.

## ALternatives
Yep, we can use list + join() -> faster, cleaner<br>
words = [operation[char] for char in str(n)]<br>
return " ".join(words)  <br>
Why? We're building a string inside a loop - this becomes inefficient as size grows


# Problem 3 : Strong Password Validation
## How I solve it
1. Define a function which takes 1 argument of type string and return a string
2. Check the length of password if < 8 return "Weak"
3. define four variable to check whether password contains all requirements or not
4. Using loop to iterate over each character of password and then if-elif-else nested inside for loop with built in function like .islower(), .isupper() etc., to check the requirement.
5. Then simply calling the function inside print()

## Suggestion by tutor
Can be combined into single line<br>
return "Strong" if all([has_upper, has_lower, has_digits, has_special]) else "Medium"


# Problem 4 : Digits Pattern Extractor
## How I solve it
1. Here I use different approach just define different functions for differnt tasks
2. even function will return even numbers list
3. odd function will return odd numbers list and so on
4. Finally we are callin our main function which take integer as argument and returns dictionary

## Suggestion 
- We can use list comprehension in even and odd function
- we can use filter() too 


# Problem 5 :- Simple ATM Interface
## How I solve it 
1. I define atm() and set initial amount and multi line string which will be visible to user and it will ask to choose an option
2. We are using while loop and loop will end if user choose an option to end the loop
3. In other case it will run the if-elif conditions based on the choosen option and will simply print the the result
