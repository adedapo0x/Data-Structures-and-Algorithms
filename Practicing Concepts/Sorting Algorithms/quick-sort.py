'''
Quick Sort algorithm uses the divide and conquer paradigm like Merge sort but do not use any extra array for sorting
The algo is simply the recursive repetition of these two steps:

a. Pick a pivot and place it in its correct place in the sorted array, by
b. Shifting smaller elements(i.e. Smaller than the pivot) on the left of the pivot and larger ones to the right.

For the pivot, it could be any position, but we pick the first position (saw online it's called the Hoare Partition Scheme), 
so after picking the pivot position, we then try to place it in its correct position by shifting the smaller elements(i.e. Smaller than the pivot element) to the left of the pivot and the larger ones to the right of the pivot.

so to implement this in code logically, we use two pointers:

Initially, the low points to the first index and the high points to the last index(as the range is n i.e. the size of the array).
so we then take two pointers, i and j. the i starts from low and goes to the right, and the j starts from high and goes to the left. Then while the two 
pointers have not crossed (ie. i is still less than j), we move i till we come across an element greater than pivot, then move j leftwards till we come across
an element lesser or equal to the pivot element. Then we swap the elements at these two positions. We keep on doing this till the pointers i and j cross each other
After that, we swap the element at our pivot position (low) with where pointer j stops at. pointer j at this point is our PARTITION INDEX. This is because 
to the left of position j lies unsoerted smaller elements of pivot element and to its right are unsorted larger elements of the pivot element.


After placing the pivot in the partition index(within the partition() function specified), we need to call the function quickSort() for the left and the right subarray recursively. 
So, the range of the left subarray will be [low to (partition index - 1)] and the range of the right subarray will be [(partition index + 1) to high]. 
This is how the recursion will continue until the range becomes 1, ie only one element left in the subarrays(which is sorted already on its own)

TC: O(nLogn), SC: O(1)
'''


class Solution:

    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSort(arr, low, pIndex - 1)
            self.quickSort(arr, pIndex + 1, high)
        
    
    def partition(self,arr,low,high):
        pivot = arr[low]
        i = low
        j = high
        
        while i < j:
            # this keeps running until we find a greater element that needs to go to the right
            while arr[i] <= pivot and i < high:  # i < high, so we don't go out of bounds as we increment i
                i += 1
            # this keeps running until we find a smaller or equal element that needs to go to the left
            while arr[j] > pivot and j > low:
                j -= 1
                
            if i < j: # swap keeps occuring until the i and j cross i.e i becomes greater than j
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[low], arr[j] = arr[j], arr[low] # swaps element at pivot with partition indexx
        return j # returns partition index
             
            