class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        Optimal way to solve this is to use two pointers, we keep an index on firstList and another on the secondList

        so first we get our start and end elements for the indexes we are in at both p1 and p2
        for this question, there can be 3 conditions:
        1. if the start of the inner array in second list is bigger than the end of the inner array of the first list, then there is obvs no intersection and we need to 
            shift our pointer of the inner arrays of the first list to the right, bigger elements on the right since it is sorted
        2. if the start of the inner array in first list is bigger than the end of the inner array of the second list, so we obvs no intersection here again and we need to shift the 
            pointer for the inner arrays of our second list
        3. third option, there is an intersection, so we need to basically catch all the intersections, so we pick the highest between the start numbers
            and the lowest between the end numbers
            then after that, to determine which pointer shifts, we check which has the higher value at the end, and shift the one with the lower value, in case if the one
            with the higher end value still has an array that it has an intersection with

        TC: O(M + N) where M is the length of first list, N is length of second list
        SC: O(1) if we do not consider the output list, O(N) if we do
        '''
        if not firstList or not secondList:
            return []

        ans = []

        p1 = p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            if start2 > end1:
                p1 += 1
            elif start1 > end2:
                p2 += 1
            else:
                ans.append([ max(start1, start2), min(end1, end2) ])

                if end1 > end2:
                    p2 += 1
                else:
                    p1 += 1

        return ans

        """
        Here, we use two for loops to run through list 1 and list 2. we then compare the start and stop of the arrays to determine the intersection between them.

        TC: O(M * N) where M and N is the length of first and second list respectively
        SC: O(1) if we do not consider the ans array needed to return our answer

        """
        ans = []

        for a1, a2 in firstList:
            for b1, b2 in secondList:
                if b1 > a2: # no need to check further along second list since it is sorted and there is no way there is an interception down the line
                    break

                if max(a1, b1) <= min(a2, b2):
                    ans.append([ max(a1, b1) , min(a2, b2)])

        return ans
                

        