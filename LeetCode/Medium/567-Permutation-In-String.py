class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # since permutation has to be of the same length, s1 cannot be longer than s2
        if len(s1) > len(s2): return False

        # since strings can only be lowercase letters, use index to keep count
        count1, count2 = [0] * 26, [0] * 26

        # initialize frequency
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if count1 == count2: return True

            # updating frequency as window shifts
            count2[ord(s2[r]) - ord('a')] += 1
            count2[ord(s2[l]) - ord('a')] -= 1
            l += 1
        return count1 == count2 # used to check for last window cos when last character frequency gets updated
                                # it never gets to check if counts were same, as loop is done

            

                                