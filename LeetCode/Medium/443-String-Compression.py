class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        Logic is to use two pointers, the read pointer, traverses through the entire array. The write is to modify the array
        TC: O(N), SC: O(1)
        '''
        read, write = 0, 0
        while read < len(chars):
            start = read # To know the beginning of each repeating consecutive characters
            # still need to check for read < len(chars) cos of something like [a,a,a,a] so we don't get an out of bounds error
            while read < len(chars) and chars[read] == chars[start]: 
                read += 1

            chars[write] = chars[start]
            write += 1

            # used to add to the array the length of each sequence if greater than one 
            if read - start > 1:
                for digit in str(read - start):
                    chars[write] = digit
                    write += 1
        
        return write  
