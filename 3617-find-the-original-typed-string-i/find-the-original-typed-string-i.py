class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        n = len(word)
        total = 1
        count = 1
        for i in range(1,n):
            if word[i]==word[i-1]:
                count+=1
            else:
                total+=count-1
                count=1
        total+=count-1
        return total