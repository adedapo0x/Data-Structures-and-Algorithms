class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # used mergesort here, could have also used quick sort, better SC I suppose

        def mergeSort(nums, l, r):
            if l >= r:
                return
            mid = (l + r) // 2
            mergeSort(nums, l, mid)
            mergeSort(nums, mid + 1, r)
            return merge(nums, l, mid, r)

        def merge(nums, l, mid, r):
            temp = []

            p1, p2 = l, mid + 1
            while p1 <= mid and p2 <= r:
                if nums[p1] <= nums[p2]:
                    temp.append(nums[p1])
                    p1 += 1
                else:
                    temp.append(nums[p2])
                    p2 += 1

            while p1 <= mid:
                temp.append(nums[p1])
                p1 += 1

            while p2 <= r:
                temp.append(nums[p2])
                p2 += 1

            for i in range(l, r + 1):
                nums[i] = temp[i - l]

        mergeSort(nums, 0, len(nums) - 1)
        return nums
            


        