class Solution:
    def countHomogenous(self, s: str) -> int:
        
        ls = []
        n = len(s)
        i=0

        while i<n:
            j=i+1
            while j<n and s[i]==s[j]:
                j+=1
            ls.append(s[i:j])
            i=j
        
        total = 0
        for item in ls:
            total += math.comb(len(item)+1,2)

        return total % (10**9+7)