# function to count number given
def countNumber(num):
    from math import log10 

    count = log10(num) + 1
    return int(count)

# print(countNumber(1400)) # Test

