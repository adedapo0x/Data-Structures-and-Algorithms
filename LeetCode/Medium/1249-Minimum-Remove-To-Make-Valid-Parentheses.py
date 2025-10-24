class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Here, we use a count variable to keep track of the count of open and closed brackets we see. when we come across a ( we increment count, and when 
        we come across a ) we decrement count, while appending to our buildUp. Note that we only decrement count after seeing a ) if count is above 0 ie there is still an unmatched ( that is preceding it
        if count is not 0, we skip it as including a closing that doesn't have an opening would make our string invalid

        by adding characters and valid parentheses to buildUp list, we would have gotten rid of invalid ), remains invalid openings that is if the openings are more 
        than the (, we now need to start our iteration from the back and remove the ( we see while decrementing until count becomes zero.
        we start from the back because it is safer, for example, if we have (()(), we could remove any of the ( and it'll be valid right, but what if we have this, (())(
        now here we cannot just remove any ( to make count of ( and ) balanced, we need to remove the last (, so in both cases remove from the end is better and that is what we try to do
        in the second loop while building our filtered.

        note that because we start from the back, the characters would be in reverse order in filtered, and we need to bring them to their right order before
        we join then return

        TC: O(N) also, SC: O(N)
        '''
        count = 0
        buildUp = []

        for c in s:
            if c == "(":
                buildUp.append(c)
                count += 1
            elif c == ")":
                if count > 0:
                    buildUp.append(c)
                    count -= 1
            else:
                buildUp.append(c)
        
        filtered = []
        for i in range(len(buildUp) - 1, -1 , -1):
            if buildUp[i] == "(" and count > 0:
                count -= 1
                continue
            filtered.append(buildUp[i])

        filtered = filtered[::-1]
        return "".join(filtered)
    


        '''
        The approach here is that for a string to be balanced the number of ( and ) must be the same, and there must not be a ) without a ( preceding it
        so not only count, but also order of the parentheses matter. we skip the letters in our iterations as they do not matter

        Here we keep track of the indexes we want to remove from. as we come across a ( we put in the stack, but if we come across a ) and there is no preceding ( ie there is nothing
        in the stack then we want to get rid of that ), so we put its index in our set, if we come across a ) for which there is something that is in the stack, then we can just pop as the ) would have matched
        with the (. so if at the end of the string, there is still something in the stack, that is the number of ( in the stack are in excess and those whose indexes are still in the stack didn't find any ) to match with
        so they also have to go

        we take a union of the indexes in our set which are indexes of unmatched ), and indexes in our stack which are indexes of unmatched ( and put them together in 
        our set, then we then iterate over the string again skipping characters at those indexes we intend to remove, we use a list to keep the characters before joining because if we used a string 
        and was concatenating each time that would be O(N) as strings are immutable and new strings would have been formed each time

        TC: O(4N) = O(N), union is also O(N) since we are potentially adding all the characters indexes to the set
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


