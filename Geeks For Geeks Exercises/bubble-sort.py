# Given an Integer n and a list arr. Sort the array using bubble sort algorithm.

# Your Task : 
# You don't have to read input or print anything. 
# Your task is to complete the function bubblesort() which takes the array and it's size as input and sorts the array using bubble sort algorithm.


class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n-1, 0, -1):
            count = 0
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    count = 1
            if count == 0:
                break
        return arr