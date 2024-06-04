class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter=0
        ls1=list(word1)
        ls2=list(word2)
        result=""
        if len(ls1)>=len(ls2):
            for idx in range(len(ls1)):
                if idx<len(word2):
                    result+=word1[idx]+word2[idx]
                else:
                    result+=word1[idx]
        else:
            for idx in range(len(ls2)):
                if idx<len(word1):
                    result+=word1[idx]+word2[idx]
                else:
                    result+=word2[idx]

        return result
        