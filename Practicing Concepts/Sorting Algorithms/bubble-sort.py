# In this algorithm, two loops are used. The outer loop starts from the end of the array and loops backwards 
# up until just before the beginning, second loop counts from beginning of the array up until where the outer array counter is

# This involves setting outer loop i at the end of the array, then inner loop counter j starts from the beginning of the array, 
# checking if element at index j is greater than element after it (j+1), if so, it swaps them, this checking occurs up to where index i currently is
# so this algorithm swaps bigger elements to the right and pushes smaller elements to the left in each pass

# Thus, after each iteration, the last part of the array will become sorted.
# Like: after the first iteration, the array up to the last index will be sorted, 
# and after the second iteration, the array up to the second last index will be sorted, and so on.

# The check variable in the code is the optimization. check is initially set to 0, if any swap occurs it changes to 1,
# after each iteration of outer loop, the check is set to 0 back, this is because once no swap occurs again and check remains 0
# this means that the array is already sorted and there is no need to keep looping, hence the need for the condition to break out of the loop once this happens.  

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        check = 0
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                check = 1
        if check == 0:
            break
    return arr

# Time complexity (worst case and average case):  O(n^2)
# Time complexity (best case): O(n) ie if given an already sorted array

# Space complexity: O(1)

