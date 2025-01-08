class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Optimal approach, use the sum of the numbers, and subtract the sum of the elements in the array from it to get which is missing
        n = len(nums)
        total = (n * (n + 1)) // 2
        arraySum = 0
        for num in nums:
            arraySum += num

        return total - arraySum    


        # Uses a set to store the range of numbers, then check which isn't present in the array
        n = len(nums)

        hashSet = set()
        for num in nums:
            hashSet.add(num)

        for i in range(n+1):
            if i not in hashSet:
                return i
            
        # Another method would be to sort the array, then if first element is zero or last element is n, if not we have our missing element
        # if that isn't the case, start a loop from 1 up until n - 1 to check which number is missing
        # TC: O(nlogn + n) = O(nlogn)