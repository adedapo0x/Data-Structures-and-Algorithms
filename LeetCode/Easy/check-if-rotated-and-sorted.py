class Solution:
    def check(self, nums: List[int]) -> bool:

        # more optimal O(N) solution
        





        # less optimal solution
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


        