'''
Split array into contiguous subarrays such that the sum of the elements in each subarray is equal.
If it is not possible to split the array, raise a ValueError.
TC: O(N), SC: O(N) if we consider the space used by output, otherwise O(1)
'''
def split_array(arr):
    sumOfArr = sum(arr)
    if sumOfArr % 2 != 0:
        raise ValueError("Array cannot be correctly split")
    
    targetNum = sumOfArr // 2 
    leftTotal = 0

    for i in range(len(arr)):
        leftTotal += arr[i]
        if leftTotal == targetNum:
            return [arr[:i+1], arr[i+1:]]
    raise ValueError("Array cannot be correctly split")


# come back to implemntation of the split not necessarily being contiguous.