# In this algorithm, two loops are used. The outer loop starts from the end of the array and loops backwards 
# up until just before the beginning, second loop counts from beginning of the array up until where the outer array counter is

# This involves setting outer loop i at the end of the array, then inner loop counter j starts from the beginning of the array, 
# checking if element at index j is greater than element after it (j+1), if so, it swaps them, this checking occurs up to where index i currently is
# so this algorithm swaps bigger elements to the right and pushes smaller elements to the left in each pass

#  

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