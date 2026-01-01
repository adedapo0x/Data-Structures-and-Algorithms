class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        Here the approach is to use the sliding window pattern, we go through the entire input array and for every element x we consider if we could have as many
        x as possible within the constraints of k given. since we know that we can only add to numbers to get element x, so we need to look at elements less than x, 
        so we sort the array, that way we know that the elements by the left of an index are for sure smaller or equal elements.

        we use left and right pointers here to maintain the sliding window, we start from index 0, then index 1, etc, as we move our right pointer to the right, we are adding the elements
        we come across to a total. The trick is if we have m elements in our sliding window and we want to check if all can be allowed to be the same element x, then
        we can do size of the window multiplied by the element x, we get size of window by r - l + 1, so after getting the product if all those m elements were x, we subtract from it the actual total in the window
        and if the difference is larger than k we know we do not have enough moves to increment to that extent and that window is not a valid one.

        so the while loop there is to resize the window to be valid back. The last line helps us recalculate the size of valid window we currently have through each iteration, and if the window increased and is valid,
        the value of size gets updated. then we return size after the loop, as the question is asking what is the max number of elements we get to be the same, which is what is represented by the size of 
        the window

        TC: O(NlogN) the NlogN comes from the sorting, the loop is O(N) because the while loop cannot grow to be O(N) 
        SC: O(N), primarily due to the sorting.
        

        '''
        sortedNums = sorted(nums)

        currentTotal = 0
        size = 0
        left = 0

        for right in range(len(sortedNums)):
            target = sortedNums[right]
            currentTotal += target

            while ((right - left + 1) * target ) - currentTotal > k:
                currentTotal -= sortedNums[left]
                left += 1

            size = max(size, right - left + 1)

        return size
