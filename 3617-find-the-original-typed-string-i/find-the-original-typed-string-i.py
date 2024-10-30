class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        n = len(word)
        ls = []
        count = 1
        for i in range(1,n):
            if word[i]==word[i-1]:
                count+=1
            else:
                ls.append(count-1)
                count=1
        ls.append(count-1)
        return sum(ls)+1