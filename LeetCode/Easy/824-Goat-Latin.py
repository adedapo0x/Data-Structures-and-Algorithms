class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        '''
        TC: O(N) where N is the number of characters in the sentence, SC: O(N)
        '''
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        words = sentence.split()
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                words[i] = word + "ma" + ("a" * (i + 1))
            else:
                words[i] = word[1:] + word[0] + "ma" + ("a" * (i + 1))

        return " ".join(words)