class Solution:
    def minimumPushes(self, word: str) -> int:
        dc=defaultdict(int)
        for letter in word:
            dc[letter]+=1

        ls=[]
        for value in dc.values():
            ls.append(value)
        ls.sort(reverse=True)

        total=0
        
        for i in range(len(ls)):

            total+=ls[i]*(1+i//8)
        
        return total