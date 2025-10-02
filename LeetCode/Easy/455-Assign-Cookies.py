class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        We use the greedy approach here. The idea is that we can only give a child a cookie of the size he wants or greater than that size, so how do we do that in 
        an optimal way. greedy!

        for each child, we want to pick a cookie that the child would be content with. the best way to do this is to pick a cookie nearest to the greed of the child so the cookies
        of larger sizes can reach other children with larger greed values, and hence we maximize the number of children satisfied

        best way of doing this is to sort both the greed array and the size array, so we use two pointers, one on each to go across both. we can only move from a child greed index if we come across a
        cookie that is of size greater than equal to it. since both arrays are sorted, this ensures that we are giving that child the minimum size of cookie that can satisfy him.
        we keep our pointers within the length of their respective arrays as either of the arrays could end before the other, either too many cookies or too less children.

        we return r, as this is the pointer we keep on the children greed array, wherever the pointer is by the time the loop ends, that is the number of children that we have satisfied
        say greed = [10, 12, 13, 14], and loop ends with r on index 2, ie at value 13. that is we are yet to satisfy that kid with greed index 13, but r is 2. which corresponds to the number of kids we have satisfied
        kids with index [10, 12]

        TC: O(NlogN + MlogM + min(M, N)) since we sort both lists and the loop runs for the minimum length of the two arrays
        SC: O(1)
        '''
        l = r = 0
        g.sort()
        s.sort()

        while l < len(s) and r < len(g):
            if s[l] >= g[r]:
                r += 1
            l += 1

        return r
