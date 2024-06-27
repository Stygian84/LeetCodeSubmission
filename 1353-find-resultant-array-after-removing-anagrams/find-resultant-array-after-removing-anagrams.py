class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        

        res=[words[0]]
        
        for i in range(1,len(words)):
            if (sorted(list(words[i-1]))) != (sorted(list(words[i]))):
                res.append(words[i])

        return res