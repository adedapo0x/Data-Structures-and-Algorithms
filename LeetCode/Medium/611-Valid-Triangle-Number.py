class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        Better approach, here we sort, since the numbers are sorted we no longer need to check all the conditions, we only need to check that a + b > c
        no need to check b + c > a or a + c > b because c would be greater than a and b, or worse equal to them and the sum with it would definitely be greater than either a or b on its own

        so we use two loops to pick a and b, i is the index for a, j is the index for b, so to find c, rather than checking all the numbers one by one, we can use binary search since the 
        elements are sorted, what we need to find using binary search is the first element where a + b < c (break point), so we will then know that all the elements before that index,
        a + b > c. the BS function takes in our search range for c which is from k = i + 2 the first time and the ending of the array, and also x (the sum of a and b)

        once we find the first index where a + b < c, we return that index, use examples it will be our index l. then to get the count of triplets formed by a, b and 
        all the valid c that we found, we do k - j - 1, the minus 1 is because the index we returned is actually not valid since at that l, c > a + b. so we get the number of triplets
        with fixed a, b then multiple valid c.
         
        then we go to the next j, note that we do not want to start the search for the breakpoint from j + 1 here, we want to start from the last k we got since we know that all to the left
        of that k would be valid, just search to the right, and that is why in our implementation, we do k = i + 2 before the j loop starts, because for subsequent j we do not want k to start from j + 1
        because that would have been the case if we set k initially inside the loop to j + 1

        TC: O(N^2logN)
        SC: O(1)
        '''
        count = 0
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i+1, len(nums) - 1):
                k = self.binarySearch(nums, k, len(nums) - 1, nums[i] + nums[j])
                count += (k - j - 1)     
        return count

    def binarySearch(self,nums, l, r, x):
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= x:
                r = mid - 1
            else:
                l = mid + 1
        return l


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
                
        