class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        Bruteforce approach, gives TLE, this is the most intuituve solution, where we use the rule directly, that the sum of any two sides of the triangle
        must be greater than the third side, else that triplet are not valid triangle sides

        TC: O(N^3), SC: O(1)
        '''
        if len(nums) < 3:
            return 0

        count = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    num1, num2, num3 = nums[i], nums[j], nums[k]
                    if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
                        count += 1

        return count
                
        