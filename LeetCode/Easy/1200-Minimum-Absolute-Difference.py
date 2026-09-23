class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        '''
        Sort the array first, then we can just iterate through the array and find the minimum difference between adjacent elements, 
        since they are sorted, the minimum difference will be between adjacent elements.

        TC: O(NlogN) for sorting, O(N) for iterating through the array, so O(NlogN)
        SC: O(N) for the output list
        '''
        arr.sort()

        minDiff = float("inf")

        result = []

        for i in range(1, len(arr)):
            currentDiff = arr[i] - arr[i-1]
            if currentDiff < minDiff:
                result = [[arr[i-1], arr[i]]]
                minDiff = currentDiff
            elif currentDiff == minDiff:
                result.append([arr[i-1], arr[i]])
            
        return result
