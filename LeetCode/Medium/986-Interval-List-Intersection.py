class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
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
                

        