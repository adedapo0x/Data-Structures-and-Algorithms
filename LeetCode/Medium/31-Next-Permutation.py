class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        Optimal Approach:
        For permuations, take English words for example, abbx, abfk, aysc. these are like three words that are going lexicographically larger.
        we notice that for permutations that are next to each other, there is a possibility of them having similar prefixes. that is something we capitalize on

        take this array as an example: [2, 1, 5, 4, 3, 2]
        if we take from the starting 2 to 3 ie 21543 as the similar prefix, can we get any other lexicographically greater permutations, no, what of 2154 as leading prefix, no, the only other
        permutation would be 215423 and that is not lexicoographically greater since 2 is less than 3. what about, 215 as prefix for both, there can be no lexicigraphically greater permutation.
        what of 21 as prefix, still no valid permutation, but if we have 2 as the prefix, we can get lexicographicaly greater permmutation such as 254321 or 245321 or 234512 and a lot more others, 
        the reason why we are able to get a valid lexicographically higher permutation for prefix as 2, and we were not able to get for others as 2 is because, for 2 as prefix, the next element was 1, looking at all the other 
        elements of the array, is there anything greater than 1, that could replace it, yes, hence we were able to get valid greater permuations, whereas in taking 215 as the prefix, the next element was 4, and after 4 there was nothing in the array that was bigger than 4
        that we could use to create a larger permutation. same for 21, after 21 was 5, nothing after 5 that was greater than it that we could use

        so we notice that this index where we can get a valid lexicographically greater permuation was where a dip occured, going from right to left, like where nums[i] < nums[i+1], since 1 was less than 5
        so we use this to get where the next element after the prefix would be, the earliest place where a dip can occur is the element before the last element, eg take array = [1, 2, 3, 4, 5] the dip occurs at 4 so that is
        n - 2 in terms of index, where n is len(array), so we check for dip from n - 2 up until the first element. If no dip is found, that means there is no lexicographically greater permuatation and we need to return it in the lowest possible order
        e.g for array [5, 4, 3, 2, 1], no dip occurs here, so what we just need is the reverse of the array 

        if we find the dip, now we need an element to replace that element but we can't just pick any random element greater than it in the array, we need something greater but still closest to the dip value since we are not
        just looking for something greater, but the next greater, so since we know that from the end of the array up until the dip, elements have been increasing, we can loop from end of the array, and the first element
        we come across that is greater than the element at the dip is the closest number greater than it, so we then swap the values, after swapping, we have our prefix and one more value that makes it lexicographically greater,
        so we need the rest of the array to be in a sorted version, since we need the exactly next permutation, and we know they are sorted right to left, so we just need them sorted left to right, so we use two pointers, one at the index next to dip,
        the other at the end of the array, and we swap until the pointers meet

        at this point, we have our next permutation.
        TC: O(N), SC: O(1)

        '''
        indx = -1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                indx = i
                break

        if indx == -1:
            nums.reverse()
            return

        for i in range(n - 1, indx, -1):
            if nums[i] > nums[indx]:
                nums[i], nums[indx] = nums[indx], nums[i]
                break

        l, r = indx + 1, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

