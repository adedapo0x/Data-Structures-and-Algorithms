# the binary search algorithm can be implemented either iteratively or recursively

# We will be implementing the recursive way here

def bs(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bs(arr, mid+1, right, target)
    else:
        return bs(arr, left, mid-1, target)