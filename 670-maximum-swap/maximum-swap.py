class Solution:
    def maximumSwap(self, num: int) -> int:
        ls = list(str(num))
        #find maximum, swap iwth num[0] if maximum>num[0]
        #else,
        maximum=[]
        for i in range(len(ls)-1):
            if ls[i]<=ls[i+1]:
                maximum.append((ls[i+1],i+1))
        
        maximum.sort(reverse=True)

        for a,b in maximum:
            i=0
            while i<len(ls):
                if a>ls[i] and b>i:
                    ls[i],ls[b]=ls[b],ls[i]
                    return int("".join(ls))
                i+=1
        return num