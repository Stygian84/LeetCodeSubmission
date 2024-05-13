class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for letter in word1:
            if abs(word1.count(letter)-word2.count(letter))>3:
                return False
        
        for letter in word2:
            if abs(word1.count(letter)-word2.count(letter))>3:
                return False
        return True
        