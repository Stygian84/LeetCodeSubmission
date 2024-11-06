class Solution:
    def countVowels(self, word: str) -> int:
        vowels='aeiou'

        n = len(word)
        total = 0
        for i in range(n):
            if word[i] in vowels:
                total += (i+1)*(n-i)
        return total
        