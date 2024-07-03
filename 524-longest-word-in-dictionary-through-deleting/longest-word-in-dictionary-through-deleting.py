class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))

        def check(word):
            i,j=0,0
            while i<len(s) and j<len(word):
                if s[i]==word[j]:
                    j+=1
                i+=1
                
            return j==len(word)
        
        res=""
        for item in dictionary:
            if check(item):
                return item
        return res