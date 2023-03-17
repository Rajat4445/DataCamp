'''
For example, passing the string 'ukulele' to the retrieve_character_indices() function should result in the following output: 
{'e': [4, 6], 'k': [1], 'l': [3, 5], 'u': [0, 2]}.
'''
def character_position(string):                       
    output = dict()
    
    for index, character in enumerate(string):
        if character in output:
            output[character].append(index)
        else:
            output[character] = [index]
            
    return output

'''
A prime number is a natural number that is divisible only by 1 or itself (e.g. 3, 7, 11 etc.). However, 1 is not a prime number.

Your task is, given a list of candidate numbers cands, to filter only prime numbers in a new list primes.

But first, you need to create a function is_prime() that returns True if the input number 
n
 is prime or False, otherwise. To do so, it's sufficient to test if a number is not divisible by any integer number from 2 to 
n
'''
def is_prime(n):
    # Define the initial check
    if n < 2:
       return False
    # Define the loop checking if a number is not prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
# Filter prime numbers into the new list
primes = [num for num in cands if is_prime(num) is True]
print("primes = " + str(primes))

'''
Two numbers a and b are coprime if their Greatest Common Divisor (GCD) is 1. GCD is the largest positive number that divides two given numbers 
a and b. For example, the numbers 7 and 9 are coprime because their GCD is 1.

Given two lists list1 and list2, your task is to create a new list coprimes that contains all the coprime pairs from list1 and list2.
'''
def gcd(a, b):
    # Define the while loop as described
    while b != 0:
        temp_a = a
        a = b
        b = temp_a % b    
    # Complete the return statement
    return a
    
# Create a list of tuples defining pairs of coprime numbers
coprimes = [(i, j) for i in list1 
                   for j in list2 if gcd(i, j) == 1]
print(coprimes)

