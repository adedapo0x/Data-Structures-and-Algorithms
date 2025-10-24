class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        The approach here is that for a string to be balanced the number of ( and ) must be the same, and there must not be a ) without a ( preceding it
        so not only count, but also order of the parentheses matter

        Here we keep track of the indexes we want to remove from. as we come across a ( we put in the stack, but if we come across a ) and there is no preceding ( ie there is nothing
        in the stack then we want to get rid of that ), so we put its index in our set, if we come across a ) for which there is something that is in the stack, then we can just pop as the ) would have matched
        with the (. so if at the end of the string, there is still something in the stack, that is the number of ( in the stack are in excess and those whose indexes are still in the stack didn't find any ) to match with
        so they also have to go

        we take a union of the indexes in our set which are indexes of unmatched ), and indexes in our stack which are indexes of unmatched ( and put them together in 
        our set, then we then iterate over the string again skipping characters at those indexes we intend to remove, we use a list to keep the characters before joining because if we used a string 
        and was concatenating each time that would be O(N) as strings are immutable and new strings would have been formed each time

        TC: O(2N) = O(N)
        SC: O(N)
        
        '''
        stack = []
        indexesToRemove = set()
        
        for i in range(len(s)):
            if s[i] not in "()":
                continue

            if s[i] == "(":
                stack.append(i)
            elif not stack:
                indexesToRemove.add(i)
            else:
                stack.pop()

        res = []
        indexesToRemove = indexesToRemove.union(stack)
        for i in range(len(s)):
            if i not in indexesToRemove:
                res.append(s[i])

        return "".join(res)


