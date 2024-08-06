class Solution:
    def minimumPushes(self, word: str) -> int:
        dc=defaultdict(int)
        for letter in word:
            dc[letter]+=1

        ls = sorted(dc.values())

        total=0
        
        n=len(ls)
        for i in range(n):
            total+=ls[i]*(1+(n-1-i)//8)
        
        return total