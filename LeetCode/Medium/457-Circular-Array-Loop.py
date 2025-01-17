class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        '''
        '''
        n = len(nums)
        visitedIndex = set() 

        def getNextIndex(index, currDir):
            nextIndex = (index + nums[index]) % n
            nextDir = 1 if nums[nextIndex] > 0 else -1
            if currDir != nextDir or index == nextIndex:
                return -1
            return nextIndex

        for i in range(n):
            if i in visitedIndex:
                continue
            slow = fast = i
            currDir = 1 if nums[i] > 0 else -1
            while True:
                visitedIndex.add(slow)
                visitedIndex.add(fast)

                slow = getNextIndex(slow, currDir)
                fast = getNextIndex(fast, currDir)

                if slow == -1 or fast == -1:
                    break
                
                fast = getNextIndex(fast, currDir)
                if fast == -1:
                    break

                if fast == slow:
                    return True
        return False