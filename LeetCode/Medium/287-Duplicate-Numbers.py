class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Approach is to use Floyd's cycle detection algorithm
        Naive way is to use two loops, check if duplicates occur by checking if nums[i] == nums[j], get TLE I think
        Other way is to use hashing to store it to know if duplicates occur (can't use, don't use extra memory)
        Or sort, then check if duplicates exists from adjacent elements (can't do, told not to modify array)

        Right way to do this is a linked-list approach. Since there is always a duplicate, there is going to be a cycle in the LL
        You can keep 0 <since array starts from 0) and no node points to it, so check val at index 0 go to the val index in the array to keep building the LL and so on
        Keep one slow pointer and one fast, slow moves once, fast moves twice. keep it going till they meet. then start another again till they meet again, this gives the duplicate

        (Copied from a Yt comment) Why does this work? Consider the distance each pointer travels:

        - When the tortoise enters the cycle, the hare is somewhere within the cycle (since it moves faster). They will eventually meet inside the cycle, but not necessarily at the start of the cycle (the duplicate number).

        - By the time they meet, both pointers have traveled a distance that is a multiple of the cycle's length. The hare has traveled twice the distance of the tortoise.

        - The distance from the start of the array to the start of the cycle (let's call this distance "a"), plus the distance from the start of the cycle to the point where the two pointers meet within the cycle (let's call this distance "b"), is equal to the total distance the tortoise has traveled.

        - Therefore, the distance from the start of the array to the start of the cycle ("a") is equal to the distance from the point where the two pointers meet within the cycle to the start of the cycle if you continue moving in the direction of the cycle.

        That's why, when you reset the tortoise to the start of the array and move both pointers one step at a time, they will meet at the start of the cycle (the duplicate number).
        '''
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
