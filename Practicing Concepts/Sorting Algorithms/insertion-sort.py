# Insertion sort is a simple and efficient sorting algorithm 
# that works by iteratively building a sorted subarray at the beginning of the original array

# this means we have an outer loop that iterates the entire array say with a counter i
# then we have an inner counter say j, whereby j checks elements in the subarray [from beginning of array till where i is currently]
# it checks if element at position j which is initially instantiated as i is lesser than the element before it [j-1]
# if it is both are swapped, j decreases by one till it gets to the beginning of the array and does the check each time

# important to note that j in decreasing stops at 1, not the beginning itself which is 0, because j-1 gives -1 when j=0 and this can lead to logic errors

def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

# Time Complexity (worst and average case): O(n^2)
# Time complexity (best case ie already sorted array): O(n)

# Space complexity: O(1)