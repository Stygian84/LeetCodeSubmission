class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        

        res=[words[0]]
        
        for i in range(1,len(words)):
            str1="".join(sorted(list(words[i-1])))
            str2="".join(sorted(list(words[i])))

            if str1!=str2:
                res.append(words[i])

        return res