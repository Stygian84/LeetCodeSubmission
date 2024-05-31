class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0]!=sentence[-1]:
            return False
        ls=sentence.split()
        for i in range(len(ls)-1):
            if ls[i+1][0]!=ls[i][-1]:
                return False
        return True