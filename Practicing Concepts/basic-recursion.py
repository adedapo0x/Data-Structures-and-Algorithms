# function to reverse an array recursively using just one pointer
# gotten from Striver's YT channel

def reverseRecursively(arr,i):
    n = len(arr)
    if i > n // 2:
        return arr
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return reverseRecursively(arr, i + 1)

# another method to reverse array using recursion
# two pointer approach

def swap(arr, l, r):
    if l >= r:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    return swap(arr, l + 1, r - 1)


# recursive function to check if a string is a palindrome
def isPali(string, i):
    n = len(string)
    if i >= n // 2:
        return True
    if string[i] != string[n-i-1]: # uses the n-i-1 trick used in reversing an array solution that is above
        return False
    return isPali(string,i+1)
