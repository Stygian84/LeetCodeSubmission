class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        prefix = []
        
        n = math.inf
        for s in strs:
            n = min(n,len(s))
        
        while i<n:

            prefix.append(strs[0][i])

            for s in strs:
                if s[i]!=prefix[-1]:
                    prefix.pop()
                    return "".join(prefix)
            i+=1
        
        return "".join(prefix)