# function to reverse an array recursively
# less efficient, yes I know. Upping my recursion game tho

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
