class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Optimal solution TC: O(N) + O(K) + O(N-K) = O(2N) = O(N), SC: O(1)
        # We initially reverse the entire array, then we reverse the array for k elements, then we reverse the rest of the array
        # so this is three reversals in total and we find out that the resultant array is exactly how we want it after k rotations

        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)



        # Uses extra memory to store the initial n - k elements, then we put the remaining k elements at the end of the array to the beginning of the array
        # then the initial temp array created, we add it to fill the rest of the array
        #  TC: O(K) + O(N-k) + O(K) = O(N+K) , SC: O(K)

        n = len(nums)
        k = k % n

        temp = []
        for i in range(n-k):
            temp.append(nums[i])
        j = 0
        for i in range(n-k, n):
            nums[j] = nums[i]
            j += 1
        j = 0
        for i in range(k, n):
            nums[i] = temp[j]
            j += 1