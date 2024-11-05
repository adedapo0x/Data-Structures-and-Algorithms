# Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

# Your Task:  
# You dont need to read input or print anything.
# Complete the functions select() and selectionSort() ,where select() takes arr[] and starting point of unsorted array i as input parameters and returns the selected element for each iteration in selection sort,
# and selectionSort() takes the array and it's size and sorts the array.


class Solution: 
    def select(self, arr, i):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        return minIndex
            
    def selectionSort(self, arr,n):
        #code 
        for m in range(n):
            change = self.select(arr, m)
            arr[m], arr[change] = arr[change], arr[m] 
        