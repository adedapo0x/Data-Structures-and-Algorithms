class Solution:
    def check(self, nums: List[int]) -> bool:

        # more optimal O(N) solution
        # goes through the loop and checks if the present element is greater than the element after it
        # we use the modulo operator cos of when we get to the end of the array, if rotated, we want to check that it is less than the beginning of the array if we have encountered the point of rotation before
        # for a testcase whereby the array is sorted but not rotated 0 times, the check of the last element against the beginning causes the count to increment by 1, the loop terminates and we still get true.
        
        count = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i+1) % len(nums)]:
                count += 1
            if count > 1:
                return False
        return True





        # less optimal solution
        # checks for every valid rotation starting from 1 to see if the there is any in which the formular works for 
        sortedArr = sorted(nums)
        for i in range(1, len(nums)+1):
            count = len(nums)
            for j in range(len(nums)):
                if not (sortedArr[j] == nums[(j+i) % len(nums)]):
                    break
                else:
                    count -= 1
            if count == 0:
                return True
        return False


        