class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        '''
        for this approach, we use pointers to manipulate the nums1, that way there is no need for extra memory
        we keep pointers p1 and p2 at the end of the elements to be arranged in nums1, nums2 respectively
        and an extra pointer named back is put at the end of nums1

        so we start from behind, since the arrays are sorted, we take the bigger element between the two elements at the back and we are guaranteed
        that that would be the biggest elements, then we shift the pointers leftward comparing each time, 

        after one of the arrays get depleted, we check through the other to know if it is also donee. we do not necessarily need to do anything if it is p1 for nums1
        that remains as the array nums1 would be as we want it already. we do need to check and do the needful if it is nums2 that remains

        TC: O(M + N)
        SC: O(1)

        '''
        
        back = len(nums1) - 1
        p1, p2 = m - 1, n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[back] = nums1[p1]
                p1 -= 1
                back -= 1
            else:
                nums1[back] = nums2[p2]
                p2 -= 1
                back -= 1

        # we do not necessarily need this check, works without it. since num1 is still the array we are mutating in place
        # while p1 >= 0:
        #     nums1[back] = nums1[p1]
        #     p1 -= 1
        #     back -= 1

        while p2 >= 0:
            nums1[back] = nums2[p2]
            p2 -= 1
            back -= 1



        '''
        This approach uses an extra memory to store the sorted result before populating nums1 back
        we use two pointers to step through and pick minimum each time from the two arrays
        '''

        temp = []

        p1 = p2 = 0

        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                temp.append(nums1[p1])
                p1 += 1
            else:
                temp.append(nums2[p2])
                p2 += 1

        while p1 < m:
            temp.append(nums1[p1])
            p1 += 1

        while p2 < n:
            temp.append(nums2[p2])
            p2 += 1

        for i in range(len(nums1)):
            nums1[i] = temp[i]