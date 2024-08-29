class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n==k:
            return 0

        n = bin(n)[2:]
        k = bin(k)[2:]
        
        length = max(len(n),len(k))
        n=n.zfill(length)
        k=k.zfill(length)
        
        count=0
        for s,t in zip(n,k):
            if s!=t:
                if s=="1" and t=="0":
                    count+=1
                else:
                    return -1
        return count