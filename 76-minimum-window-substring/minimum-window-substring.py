class Solution:
    def minWindow(self, s: str, t: str) -> str:

        dc=defaultdict(int)
        for letter in t:
            dc[letter]+=1

        n=len(s)
        min_length=math.inf
        i=0
        res=""

        
        for j in range(n):
            if s[j] in dc:
                dc[s[j]]-=1

            while all(value<=0 for value in dc.values()):
                if j-i+1<min_length:
                    min_length=j-i+1
                    res=s[i:j+1]
                if s[i] in dc:
                    dc[s[i]]+=1
                i+=1
            

        return res
        