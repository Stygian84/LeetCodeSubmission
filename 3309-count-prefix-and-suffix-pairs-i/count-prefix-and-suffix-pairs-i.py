class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1,str2):
            length=len(str1)
            if str2[:length]==str1 and str2[-length:]==str1:
                return True
            return False
        count=0
        for idx in range(len(words)):
            for i in range(idx+1,len(words)):
                if isPrefixAndSuffix(words[idx],words[i]):
                    count+=1
        return count