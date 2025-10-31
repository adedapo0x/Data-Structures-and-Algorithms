class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Here, the approach is to use two stacks. one for letters, one for the numbers, when we come across a letter, we add it to currentString variable, 
        when we come across digit, add it to the variable k, then when we come across a "[", we append what is in our k and currentString to countStack and stringStack
        respectively, and reset both k and currentString.

        when we come across a "]", the decoding begins, we pop from both stacks, we take what we popped from countStack and multiply it with whatever our currentString 
        is, add that to what we popped from stringStack and reassign it back to currentString, and in the end we return currentString, as it would have everything we want

        TC: O(maxK * n) where n is len of s , and maxK is the largest number k in s
        because we iterate over s and we duplicate strings for every k[str] in the loop, so worst case is the largest number of K
        '''
        countStack = []
        stringStack = []

        k = ""
        currentString = ""

        for c in s:
            if c.isdigit():
                k += c
            elif c == '[':
                countStack.append(int(k))
                stringStack.append(currentString)
                k = ""
                currentString = ""
            elif c == "]":
                decodedString = stringStack.pop()
                currentK = countStack.pop()
                currentString = decodedString + currentString * currentK
            else:
                currentString += c
        return currentString
    


        '''
        More intuitive approach to me, we basically loop through and append the characters we come across to our stack, when we come across "]", it is time to decode
        so we pop from our stack strategically, we get the string from stack by popping, make sure we arrange them in the correct order, get rid of the "[" that would have
        preceded by the pop outside the loop, then get the number, store it in k, make sure to get the correct order too as there might be multiple digits, then duplicate the word k times
        then append to the stack again.

        when we are doing going over s, we can then join all what is in stack together, and that would give us our decoded string

        TC: O(N + M) where N is the length of the input string and M is the length of the decoded string, 
        because we go through the entire string, and for each decoding of a section, we are creating new string taking time relative to the length of the entire decoded string
        also the final .join call also takes O(M), so total is O(N + M)
        
        SC: max(N, M), it , the stack may hold near about the entire input string, so O(N) and it can also hold output string that we generate is O(M)
        it is not straight up O(M) because say we have 1[k]1[ee], the decoded string kee is shorter than the input string
        '''
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                word = ""
                while stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(word * int(k))
        return "".join(stack)
