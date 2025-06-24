# Problem 2 - Sentence Analyzer toolkit
text = """A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern."""

def word_character_count(data: str) -> dict:
    word_count = len(data.replace(",", "").replace(".", "").split())
    character_count = len(data.replace(" ", ""))
    output = {
        "Number of words": word_count,
        "Number of Characters" : character_count
    }
    
    return output

def longest_word(data: str) -> str:
    words = data.replace(",", "").split()
    max_length = max(len(word) for word in words)
    longest_word = [word for word in words if len(word) == max_length]
    
    return longest_word
    
    
def most_frequent_word(data: str):
    from collections import Counter
   
    most_frequent = Counter(data.replace(",","").split()).most_common(1)[0][0]     
    
    return most_frequent

def stopwords_count(data: str) -> dict:
    stopwords = ['is', 'the', 'a', 'and', 'in']
    
    data = data.replace(",", "").replace(".", "").lower().split()
    counts = {word: 0 for word in stopwords}
    
    for word in data:
        if word in counts:
            counts[word] += 1
    return counts

def sentence_analyzer(text: str):
    return {
        "Word & Char Count": word_character_count(text),
        "Longest Word(s)": longest_word(text),
        "Most Frequent Word": most_frequent_word(text),
        "Stopwords Count": stopwords_count(text)
    }


print(sentence_analyzer(text))


# Problem 3 : Custom String Encryption and Decryption
def encrypt(data):
    # Shifting each character
    ord_list = []
    chr_list = []
    for char in data:
        new = ord(char) + 1
        ord_list.append(new)
    
    for element in ord_list:
        character = chr(element)
        chr_list.append(character)
        
    new_text = "".join(chr_list)
    
    # Reverse the entire string
    reverse_text = new_text[::-1]
    
    # Adding @ before each vowel
    new_rev = []
    for char in reverse_text:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            new_rev.append("@"+char)
        else:
            new_rev.append(char)
    new ="".join(new_rev)
    return new
text = encrypt(text)
print(text)

def decrypt(text):
    # Decrypt and get original string back
    data = text.replace("@", "")
    data = data[::-1]
    
    ord_list = []
    chr_list = []
    
    for char in data:
        ord_list.append(ord(char)-1)
    
    for element in ord_list:
        chr_list.append(chr(element))
    
    return "".join(chr_list)

decrypt = decrypt(text)
print(decrypt)

# Problem 4 :- Pattern Maker - String Edition
word = "CODE"
def vertical_display(text: str):
    for char in text:
        print(char)
        
def word_pyramid(text: str):
    for i in range(1, len(text)+1):
        print(text[:i])

def reverse_pyramid(text: str):
    for i in range(len(text)+1, 1, -1):
        print(text[:i])
        
def symmetric_mirror(text: str):
    for i in range(1, len(text) + 1):
        left = text[:i]
        right = text[:i][::-1]
        print(f"{left}|{right}")
        
vertical_display(word)
word_pyramid(word)
reverse_pyramid(word)
symmetric_mirror(word)

# Problem 5 :- Mini CLI Reciept generator
items = [("Apple", 40), ("Mango Juice Bottle", 120), ("Chips", 35)]
def item(items: list):
    count = 0
    for element in items:
        product = ""
        if len(element[0]) > 15:
            product = element[0].replace(element[0][15::], "..")
        else:
            product = element[0]
            
        price = element[1]
        count += 1
        
        print(f"{count}.{product.ljust(20)}|{price}")

def total_with_GST(items: list):
    print("---------------------")
    total = 0 
    for element in items:
        total += element[1]
        total_with_tax = total + ((total * 18) / 100)
    return f"Total (including 18 % GST): {total_with_tax}"


item(items)
print(total_with_GST(items))