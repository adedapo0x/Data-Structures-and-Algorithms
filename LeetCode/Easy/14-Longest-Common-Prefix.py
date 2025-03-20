class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        The approach is Horizontal scanning, came up with this implementation myself. The approach here is to take the first element in order to compare
        it with the rest of the strings in the array, so we loop through each of the element strings in the array and check it against corresponding index of the first element,
        once it is not equal, we break out. so up until that index is equal for that particular string, then we go to the next and repeat
        We check for the one with the minimum length between the first element and the string element we are currently comparing against, because further strings we
        come across can be shorter than the first element, so we don't need to loop beyond that
        We also check the minimum of the indexes with matching character, cos they can be elements that have lesser to no characters matching the first, down the line
        TC: O(m * n) where m is the size of the input array and n is the length of the shortest string 
        '''
        res = strs[0]
        index = len(res)
        for i in range(1, len(strs)):
            matches = 0
            for j in range(min(len(res), len(strs[i]))):
                if strs[i][j] == res[j]:
                    matches += 1
                else: 
                    break
            index = min(index, matches)        

        return "".join(strs[0][:index])

