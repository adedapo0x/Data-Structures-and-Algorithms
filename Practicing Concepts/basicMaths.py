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



