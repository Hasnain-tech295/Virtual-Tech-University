from math import sqrt

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def test_function():
    assert is_prime(2) == True
    assert is_prime(10) == False
    assert is_prime(17) == True
    print("Successfully passed all test cases")
test_function()