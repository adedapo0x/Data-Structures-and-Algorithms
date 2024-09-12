# function to count number given
def countNumber(num):
    from math import log10 

    count = log10(num) + 1
    return int(count)

# print(countNumber(1400)) # Test


# function to reverse a given number
def reverseNumber(num):
    new_num = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        new_num = (new_num * 10) + digit
    return new_num

# print(reverseNumber(145890900090)) # test

# Find greatest common divisor
def gcd(a, b):
    # Euclidean formular for finding GCD/HCF
    while a > 0 and b > 0:
        if a > b: a = a % b
        else: b = b % a
    if a == 0: return b
    return a

# or another method, start looping from the smaller of the two number, 
# first factor is the HCF
def hcf(a,b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
    return 1


# checks if a number is an armstrong number
# an armstrong number is a number that is equal to the sum of its own digits 
# each raised to the power of the number of digits.

def isArmStrong(num):
    copy = num
    length = len(str(num))
    result = 0
    while copy > 0:
        digit = copy % 10
        result += digit ** length
        copy = copy // 10
    return result == num



# function to get all divisors of a number
# rather than looping and checking for divisors till we get to the number, 
# take square root, find divisors up to square root, looped numbers and the scond number that divides it are divisors

def getDivisors(num):
    divisors = []
    from math import sqrt
    for i in range(1, int(sqrt(num))+1):
        if num % i == 0:
            divisors.append(i)
            if num // i != i:
                divisors.append(num // i)
    return divisors

