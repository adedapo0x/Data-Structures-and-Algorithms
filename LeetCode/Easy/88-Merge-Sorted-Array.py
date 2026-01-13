class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

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