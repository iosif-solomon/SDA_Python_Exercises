
# ? 1. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# ? The function accepts the number as an argument. (3 factorial is 1 * 2 * 3 = 6)

def factorial(n):
    result = 1
    for num in range(1, n+1):
        result *= num
    return result

print(f"The factorial of {6} is {factorial(6)}.")

def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)

print(f"The factorial of {6} is {recursive_factorial(6)}.")



# ? 2. Write a Python function to check whether a number is in a given range. Return True or False.

# ! Rezolvarea 1
def is_within_range(number, start, stop):
    return number in range(start, stop+1)

print(is_within_range(6, 3, 6))

# ! Rezolvarea 2
def is_within_range2(number, start, stop):
    return start <= number <= stop

print(is_within_range2(6, 3, 6))



# ? 3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# * Sample String : 'The quick Brow Fox'
# * Expected Output : 
# * No. of Upper case characters : 3
# * No. of Lower case Characters : 12
# * HINT: use "T".isupper() or .islower()

def get_number_of_upper_and_lower_case_letters(string):
    upper_case_char = len([ch for ch in string if ch.isupper()])
    lower_case_char = len([ch for ch in string if ch.islower()])
    print(f"No. of Upper case characters: {upper_case_char}")
    print(f"No. of Lower case charachters: {lower_case_char}")

get_number_of_upper_and_lower_case_letters("The quick Brown Fox")



# ? 4. Write a Python function that takes a number as a parameter and check the number is prime or not.
# * Note : A prime number (or a prime) is a natural number greater than 1 
# * and that has no positive divisors other than 1 and itself. 

def is_prime(number):
    is_prime = True
    if number <= 1:
        is_prime = False
    else:
        for num in range(2,number):
            if number % num == 0:
                is_prime = False
                break
    return is_prime

print(is_prime(2))
print(is_prime(3))
print(is_prime(16))
print(is_prime(11))
print(is_prime(122))



# ? 5. Write a Python function that checks whether a passed string is palindrome or not.
# * Note: A palindrome is a word, phrase, or sequence that reads the same backward 
# * as forward, e.g., madam or nurses run.

def is_palindrome(string):
    return string.replace(" ","") == string.replace(" ","")[::-1]

print(is_palindrome("nurses run"))