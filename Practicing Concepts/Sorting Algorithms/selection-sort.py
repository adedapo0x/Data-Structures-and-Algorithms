# We run two loops, an inner and outer one,
# Outer one is initially from the beginning of the array to the end using index i where we assume element at index i to be the smallest initially,
# Inner loop then checks, using variable j, from i+1, to see if there is any element smaller than the initial element at index i assumed to be the smallest
# If any is found, we update the minIndex variable,
# then swap the element at index i with element at minIndex and continue the loop

# after each iteration, we will find that the array is sorted up to where i is currently


def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        if minIndex != i: # only try to swap if smaller element is found
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

# Time Complexity: O(n^2)
# Space Complexity: O(1)
