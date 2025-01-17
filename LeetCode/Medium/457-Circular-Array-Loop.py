class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        '''
        The approach is to use two pointers, normal Floyd's hare tortoise algorithm also known as Fast and slow pointer algorithm, once fast equals slow we can return True
        we basically loop through the array, since each element denotes by how much index we are moving, also storing the indexes we have encountered in a set in order to prevent redundant checks
        our currDir and nextDir is to make sure the condition of all the elements in the cycle either being all positive or all negative, say we start with currDir as positive once we get a nextDir as negative, we return -1 knowing that cannot work
        we do the modulo operator because of the ends of the array, if we move beyond the last element we want to be at the first, if beyond first, we come to the end of the array and keep on counting
        we check for index not to be equal to nextIndex since that would mean that our cycle contains just one element which is not acceptable
        we do the fast pointer twice, since for everytime slow moves once, fast is to move twice
        if we get a -1 at any point we want the inner loop to break and we start checking from the next index and element in the array if it is not already in our set
        else once fast == slow, we return True

        Yt solution link: https://www.youtube.com/watch?v=cEuJEEbIuJg
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